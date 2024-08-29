import cv2

# Kullanıcıdan hangi takip algoritmasını kullanmak istediğini alıyoruz
algorithm = input("Kullanmak istediğiniz algoritmayı giriniz: ").strip().lower()

# Video dosyasını okuyoruz
video = cv2.VideoCapture("videos/traffic.mp4")
ret, frame = video.read()

# Video okunamazsa hata mesajı verip çıkıyoruz
if not ret:
    print("Video başarılı şekilde okunamadı!")
    exit()

# İlgi alanı (ROI) seçimi: Kullanıcıdan izlenecek bölgeyi seçmesini istiyoruz
bbox = cv2.selectROI(frame, False)

# Kullanıcının seçtiği algoritmaya göre takipçi oluşturuyoruz
if algorithm == "csrt":
    tracker = cv2.TrackerCSRT_create()
elif algorithm == "kcf":
    tracker = cv2.TrackerKCF_create()
elif algorithm == "mil":
    tracker = cv2.TrackerMIL_create() 
elif algorithm == "medianflow":
    tracker = cv2.legacy.TrackerMedianFlow_create() 
elif algorithm == "mosse":
    tracker = cv2.legacy.TrackerMOSSE_create()
elif algorithm == "boosting":
    tracker = cv2.legacy.TrackerBoosting_create()
else:
    # Geçersiz bir algoritma adı girildiyse hata mesajı verip çıkıyoruz
    print("Geçersiz algoritma girildi!")
    video.release()
    cv2.destroyAllWindows()
    exit()

# Takip algoritmasını seçilen alan ve ilk kare ile başlatıyoruz
tracker.init(frame, bbox)

# Video boyunca takip işlemini gerçekleştiriyoruz
while True:
    # Her bir kareyi okuyoruz
    ret, frame = video.read()
    
    # Video sonuna geldiğimizde döngüden çıkıyoruz
    if not ret:
        break
    
    # Takip algoritmasını güncel kareye uyguluyoruz
    success, bbox = tracker.update(frame)
    
    if success:
        # Takip başarılıysa, takip edilen objenin etrafına bir dikdörtgen çiziyoruz
        p1 = (int(bbox[0]), int(bbox[1])) # Sol üst köşe
        p2 = (int(bbox[0]) + int(bbox[2]), int(bbox[1]) + int(bbox[3])) # Sağ alt köşe
        cv2.rectangle(frame, p1, p2, (0, 255, 0), 2) # Yeşil renkli dikdörtgen çiziyoruz
    else:
        # Takip başarısız olursa kullanıcıya bilgi veriyoruz
        print("Takip başarısız")
        
    # Sonucu ekranda gösteriyoruz
    cv2.imshow("frame", frame)
    
    # 'q' tuşuna basıldığında döngüyü sonlandırıyoruz
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

# Video ve tüm pencereleri kapatıyoruz
video.release()
cv2.destroyAllWindows()

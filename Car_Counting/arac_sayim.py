import cv2

cap=cv2.VideoCapture("Car_Counting\car_counting.mp4")
car_cascade=cv2.CascadeClassifier("car.xml")

while True:
    count=0
    ret,frame=cap.read()
    
    if ret==False:
        break
    
    
    frame = cv2.resize(frame,(640,480))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cars=car_cascade.detectMultiScale(gray,1.1,2)
    
    for(x,y,w,h) in cars:
        count += 1
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
    cv2.putText(frame,f"Araba sayisi:{count}",(20,50),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),1,cv2.LINE_AA)
    cv2.imshow("frame",frame)

    if cv2.waitKey(5) & 0xFF==ord('q'):
        break
    
    
cap.release()
cv2.destroyAllWindows()    

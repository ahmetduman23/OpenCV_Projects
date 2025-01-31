import cv2

cap = cv2.VideoCapture(0)

haar_cascade=cv2.CascadeClassifier("cascade_files\lefteye.xml")

while True:
    ret,frame=cap.read()
    
    if ret==False:
        break
    
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    eyes_rect=haar_cascade.detectMultiScale(gray_frame,1.1,9)
    
    for (x,y,w,h) in eyes_rect:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    
    
    cv2.imshow("frame",frame)
    
    
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break
    
    
cap.release()
cv2.destroyAllWindows()
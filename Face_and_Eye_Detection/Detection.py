import cv2

cap = cv2.VideoCapture(0)

haar_cascade_face = cv2.CascadeClassifier('Face_and_Eye_Detection\haarcascade_frontalface_default.xml')
haar_cascade_eye=cv2.CascadeClassifier("Face_and_Eye_Detection\eye.xml")

while True:
    ret,frame=cap.read()
    
    if ret==False:
        break
    
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces_rect=haar_cascade_face.detectMultiScale(gray_frame,1.1,9)
    
    for (x,y,w,h) in faces_rect:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        
        roi = frame[y:y+h,x:x+w]
        roi_gray=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
        eyes_rect=haar_cascade_eye.detectMultiScale(roi_gray,1.1,9)
        
        
        
        
        for (x1,y1,w1,h1) in eyes_rect:
            cv2.rectangle(frame,(x+x1,y+y1),(x+x1+w1,y+y1+h1),(0,255,0),2)
            


    cv2.imshow("frame",frame)
    
    
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break
    
    
cap.release()
cv2.destroyAllWindows()
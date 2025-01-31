import cv2 
import numpy as np
import imutils

def process_frame(frame):
    vid_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    vid_blur = cv2.blur(vid_gray, (3, 3))
    
    vid_edges = cv2.Canny(vid_blur, 75, 140)
    
    h, w, _ = frame.shape

    roi_alan = [(0, h), (w/2, h/1.85), (w, h)]

    mask = np.zeros_like(vid_gray)
    cv2.fillPoly(mask, np.int32([roi_alan]), 255)

    masked_img = cv2.bitwise_and(vid_edges, mask)
    

    lines = cv2.HoughLinesP(masked_img, 1, np.pi/100, threshold=50, minLineLength=50, maxLineGap=50)

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    
    return frame, vid_edges, mask, masked_img

cap = cv2.VideoCapture("Lane_Detection\lane5.mp4")

while True:
    ret, frame = cap.read()
    
    if ret == False:
        break
    
    frame, vid_edges, mask, masked_img = process_frame(frame)
    
    frame = imutils.resize(frame, width=600)
    vid_edges = imutils.resize(vid_edges, width=600)
    mask = imutils.resize(mask, width=600)
    masked_img = imutils.resize(masked_img, width=600)

    cv2.imshow("frame", frame)
    cv2.imshow("vid_edges", vid_edges)
    cv2.imshow("mask", mask)
    cv2.imshow("masked_img", masked_img)
    
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break 

cap.release()
cv2.destroyAllWindows()

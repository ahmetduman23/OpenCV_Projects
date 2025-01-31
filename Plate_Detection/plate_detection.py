import cv2
import numpy as np 
import matplotlib.pyplot as plt
import imutils
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"D://tesseract//tesseract.exe"

image_path = "Plate_Detection\plate.jpg"

img = cv2.imread(image_path)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

filtered = cv2.GaussianBlur(img_gray, (5, 5), 0)

edged = cv2.Canny(filtered, 50, 150)

#cv2.imshow("Edged Image", edged)

contours = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(contours)

cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]

screen = None

for cnt in cnts:
    epsilon = 0.018 * cv2.arcLength(cnt, True)
    
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    
    if len(approx) == 4:
        screen = approx
        break

if screen is None:
    print("Dört köşeli kontur bulunamadı.")
else:
    mask = np.zeros(img_gray.shape, np.uint8)
    
    new_img = cv2.drawContours(mask, [screen], 0, (255, 255, 255), -1)
    
    new_img = cv2.bitwise_and(img, img, mask=mask)

    (x, y) = np.where(mask == 255)
    
    (topx, topy) = (np.min(x), np.min(y))
    (bottomx, bottomy) = (np.max(x), np.max(y))

    cropped = img_gray[topx:bottomx+1, topy:bottomy+1]

    text = pytesseract.image_to_string(cropped, lang="eng")
    
    print(text)
    
    cv2.putText(img, text, (topy, topx-10), cv2.FONT_HERSHEY_PLAIN, 0.65, (255, 0, 0), 2, cv2.LINE_AA)

    # cv2.imshow("img", img)
    cv2.imshow("img_cropped", cropped)
    #cv2.imshow("new_img", new_img)

    cv2.waitKey(0)
    
    cv2.destroyAllWindows()

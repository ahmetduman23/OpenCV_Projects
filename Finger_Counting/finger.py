import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

mpHand = mp.solutions.hands
hands = mpHand.Hands()
mpDraw = mp.solutions.drawing_utils

tipIds = [4, 8, 12, 16, 20]

while True:
    succes, img = cap.read()
    
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    
    
    lmList = []
    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handlms, mpHand.HAND_CONNECTIONS)
    
            for id, lm in enumerate(handlms.landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmList.append([id, cx, cy])
                
                                  
    #print(lmList)
    
    if len(lmList) != 0:
        
        fingers = []
        
        # bas parmak (sağ ve sol ele göre farklı)
        
        if lmList[tipIds[0]][1] < lmList[tipIds[4]][1]:
        
            if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            
            else:
                fingers.append(0)
        
        else: 
            
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            
            else:
                fingers.append(0)
                
        # Diğer 4 parmak
        for id in range(1, 5):
            
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)

            else:
                fingers.append(0)
                
        print(fingers)
    
        totalF = fingers.count(1)
        #print(totalF)
        
        cv2.putText(img, str(totalF), (30, 125), cv2.FONT_HERSHEY_PLAIN, 10, (255,0,0),8)
    
    cv2.imshow("img",img)
    
    cv2.waitKey(1)
    
    
        
    
"""
makaleden yola çıkarak iyi atıflar yapmak 
kaggledan yola çıkarak oradakilere atıf yapmak
Yöntemde lgbm yazcaz 

"""
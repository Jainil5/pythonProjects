import cv2
import time
import mediapipe as mp
import HandTrackingModule as htm
cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

detector=htm.handDetector(detectionCon=0.75)
tipIds=[4,8,12,16,20]

while True:
    success, img = cap.read()
    img=detector.findHands(img)
    lmList =detector.findPosition(img,draw=False)
    #print(lmList)

    if len(lmList) !=0:
        """
        if lmList[8][2] < lmList[6][2]:
            print("Index f open")
        if lmList[12][2] < lmList[10][2]:
            print("Middle f open")
        if lmList[16][2] < lmList[14][2]:
            print("Ring f open")
        if lmList[20][2] < lmList[18][2]:
            print("Pinky f open")
        if lmList[4][1] > lmList[5][1] and lmList[4][1] > lmList[6][1] :
            print("Thumb open")
        """
        fingers=[]
        #Thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1] and lmList[4][1]>lmList[3][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # 4 Fingers
        for id in range(1,5):
            if lmList[tipIds[id]][2] <lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        print(fingers)
        cv2.rectangle(img, (20, 255), (170, 425), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(fingers.count(1)), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 20)






    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

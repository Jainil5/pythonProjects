import random
import time

import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.9, maxHands=2)


def getCount(ar):
    if ar == [0, 0, 0, 0, 0]:
        return 0
    elif ar == [0, 1, 0, 0, 0]:
        return 1
    elif ar == [0, 1, 1, 0, 0]:
        return 2
    elif ar == [0, 1, 1, 1, 0]:
        return 3
    elif ar == [0, 1, 1, 1, 1]:
        return 4
    elif ar == [1, 1, 1, 1, 1]:
        return 5
    elif ar == [0, 1, 0, 0, 1]:
        return 6
    elif ar == [0, 1, 0, 1, 1]:
        return 7
    elif ar == [1, 1, 0, 0, 0]:
        return 8


listq=["1+1=?","2+2=?"]
lista=[2,4]
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)  # With Draw
    # hands = detector.findHands(img, draw=False)  # No Draw


    if hands:
        global h1c
        global h2c
        global total

        if len(hands) == 2:
            hand1 = hands[0]
            lmList1 = hand1["lmList"]
            bbox1 = hand1["bbox"]
            centerPoint1 = hand1["center"]
            handType1 = hand1["type"]
            h1f = detector.fingersUp(hand1)
            h1c = getCount(h1f)
            # cv2.putText(img, str(h1c), (10, 40), cv2.FONT_ITALIC, 1, (0, 255, 98), 3)

            hand2 = hands[1]
            lmList2 = hand2["lmList"]
            bbox2 = hand2["bbox"]
            centerPoint2 = hand2["center"]
            handType2 = hand2["type"]
            h2f = detector.fingersUp(hand2)
            h2c = getCount(h2f)
            # cv2.putText(img, str(h2c), (400, 400), cv2.FONT_ITALIC, 1, (0, 255, 98), 3)
            if h1c == "None":
                h1c = 0
            if h2c == "None":
                h2c = 0
            listCount = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            if h1c and h2c in listCount:
                total = h1c + h2c
            cv2.putText(img, str(total), (200, 400), cv2.FONT_ITALIC, 1, (0, 255, 98), 3)

        if len(hands) == 1:
            hand1 = hands[0]
            lmList1h = hand1["lmList"]
            bbox1 = hand1["bbox"]
            centerPoint1 = hand1["center"]
            handType1 = hand1["type"]
            h1f = detector.fingersUp(hand1)
            h1c = getCount(h1f)
            # cv2.putText(img, str(h1c), (400, 400), cv2.FONT_ITALIC, 1, (0, 255, 98), 3)
            listCount = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            if h1c in listCount:
                total=h1c
            cv2.putText(img, str(total), (200, 400), cv2.FONT_ITALIC, 1, (0, 255, 98), 3)
        for i in range(0,2):
            cv2.putText(img, listq[i], (200, 40), cv2.FONT_ITALIC, 1, (0, 255, 98), 3)




    cv2.imshow("Quiz", img)
    if cv2.waitKey(1) & 0xff == ord(' '):
        break

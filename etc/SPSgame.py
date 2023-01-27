import random
import time

import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.9, maxHands=2)
global h1c
global h2c


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


dict1 = {
    0:"Stone",
    2:"Scissors",
    5:"Paper"
}


def game(a, b):
    if a == 0 and b == 0:
        print("Draw")
    if a == 2 and b == 2:
        print("Draw")
    if a == 5 and b == 5:
        print("Draw")
    if a == 0 and b == 2:
        print("You win")
    if a == 0 and b == 5:
        print("Bot win")
    if a == 2 and b == 0:
        print("Bot win")
    if a == 2 and b == 5:
        print("You win")
    if a == 5 and b == 2:
        print("bot win")
    if a == 5 and b == 0:
        print("You win")


while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)  # With Draw
    # hands = detector.findHands(img, draw=False)  # No Draw

    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmarks points
        bbox1 = hand1["bbox"]  # Bounding Box info x,y,w,h
        centerPoint1 = hand1["center"]  # center of the hand cx,cy
        handType1 = hand1["type"]  # Hand Type Left or Right
        h1f = detector.fingersUp(hand1)
        h1c = getCount(h1f)
        # cv2.putText(img, str(h1c), (10, 40), cv2.FONT_ITALIC, 1, (0, 255, 98), 3)
        if len(hands) == 2:
            cv2.putText(img, str("2 hands"), (400, 400), cv2.FONT_ITALIC, 1, (0, 255, 98), 3)
        else:
            for i in [0,2,5]:
                if h1c==i:
                    cv2.putText(img, str(dict1[i]), (300, 30), cv2.FONT_ITALIC, 1, (0, 255, 98), 3)

    cv2.imshow("SPS", img)
    if cv2.waitKey(1) & 0xff == ord(' '):
        break

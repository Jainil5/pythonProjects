import random
import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np

import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.9, maxHands=2)
global h1c
global h2c

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

volMin, volMax = volume.GetVolumeRange()[:2]

'''
listV=[]
for i in range(0,11):
    listV.append(-6.35*i)
    #print(listV)
    #[-0.0, -6.35, -12.7, -19.049999999999997, -25.4, -31.75, -38.099999999999994, -44.449999999999996, -50.8, -57.15,-63.5]
print(listV)
listV.reverse()
print(listV)
#[-63.5, -57.15, -50.8, -44.449999999999996, -38.099999999999994, -31.75, -25.4, -19.049999999999997, -12.7, -6.35, -0.0]
'''


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


while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)  # With Draw
    # hands = detector.findHands(img, draw=False)  # No Draw

    if hands:

        if len(hands) == 2:
            hand1 = hands[0]
            lmList1 = hand1["lmList"]
            bbox1 = hand1["bbox"]
            centerPoint1 = hand1["center"]
            handType1 = hand1["type"]
            h1f = detector.fingersUp(hand1)
            h1c = getCount(h1f)
            cv2.putText(img, str(h1c), (10, 40), cv2.FONT_ITALIC, 1, (0, 255, 98), 3)

            hand2 = hands[1]
            lmList2 = hand2["lmList"]
            bbox2 = hand2["bbox"]
            centerPoint2 = hand2["center"]
            handType2 = hand2["type"]
            h2f = detector.fingersUp(hand2)
            h2c = getCount(h2f)
            cv2.putText(img, str(h2c), (400, 40), cv2.FONT_ITALIC, 1, (0, 255, 98), 3)
            print(handType1, handType2)

            listV1 = [-63.5, -57.15, -50.8, -44.449999999999996, -38.099999999999994, -31.75, -25.4,
                      -19.049999999999997, -12.7, -6.35, -0.0]

            if handType1 == "Left" and h1c == 6 and h2c != 6:  # Left Host
                fc = h2c
                for i in range(1, 6):
                    if i == fc:
                        vol = listV1[i + 5]
                        print(vol)
                volume.SetMasterVolumeLevel(vol,None)
            if handType2 == "Left" and h2c == 6 and h1c != 6:  # Left Host
                fc = h1c
                for i in range(1, 6):
                    if i == fc:
                        vol = listV1[i + 5]
                        print(vol)
                volume.SetMasterVolumeLevel(vol, None)
            if handType1 == "Right" and h1c == 6 and h2c != 6:  # Right Host
                fc = h2c
                for i in range(1,6):
                    if i==fc:
                        vol=listV1[i]
                        print(vol)
            if handType2 == "Right" and h2c == 6 and h1c != 6:  # Right Host
                fc = h1c
                for i in range(1, 6):
                    if i == fc:
                        vol = listV1[i]
                        print(vol)
                volume.SetMasterVolumeLevel(vol, None)
            if handType1 == 6 and handType2==8:
                volume.SetMasterVolumeLevel(0,None)

    cv2.imshow("MuHandGes", img)
    if cv2.waitKey(1) & 0xff == ord(' '):
        break

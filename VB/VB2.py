import random
import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np
import cv2
from cvzone.HandTrackingModule import HandDetector
import screen_brightness_control as sbc

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.9, maxHands=2)
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volMin, volMax = volume.GetVolumeRange()[:2]


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
        global h1c
        global h2c
        global bri
        global vol
        global vs
        global bs

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

            listV1 = [-65.25, -33.23651123046875, -23.654823303222656, -17.829605102539062, -10.329694747924805,
                      -7.626824855804443, -5.290315628051758, -3.4243249893188477, -1.6639597415924072, 0, 0]
            listV3 = [-65.25, -23.654823303222656, -10.329694747924805,
                      -5.290315628051758,  -1.6639597415924072, 0]

            listB = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            listB1 = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
            listB2 = [0, 20, 40, 60, 80, 100]

            listV2 = []
            # Volume
            vs = 1
            bs = 2
            if h1c == vs and h2c == vs:
                volume.SetMasterVolumeLevel(-63.5, None)
            if handType1 == "Left" and h1c == vs and h2c != vs:  # Left Host
                fc = h2c
                for i in range(0, 6):
                    if i == fc:
                        vol = listV3[i]
                        print(vol)
                        volume.SetMasterVolumeLevel(vol, None)
            if handType2 == "Left" and h2c == vs and h1c != vs:  # Left Host
                fc = h1c
                for i in range(0, 6):
                    if i == fc:
                        vol = listV3[i]
                        print(vol)
                        volume.SetMasterVolumeLevel(vol, None)
            if handType1 == "Right" and h1c == vs and h2c != vs:  # Right Host
                fc = h2c
                for i in range(0, 6):
                    if i == fc:
                        vol = listV3[i]
                        print(vol)
                        volume.SetMasterVolumeLevel(vol, None)
            if handType2 == "Right" and h2c == vs and h1c != vs:  # Right Host
                fc = h1c
                for i in range(0, 6):
                    if i == fc:
                        vol = listV3[i]
                        print(vol)
                        volume.SetMasterVolumeLevel(vol, None)

            # Brightness
            if h1c == bs and h2c == bs:
                sbc.set_brightness(0)
            if handType1 == "Left" and h1c == bs and h2c != bs:  # Left Host
                fc = h2c
                for i in range(0, 6):
                    if i == fc:
                        bri = listB2[i]
                        print(bri)
                        sbc.set_brightness(bri)

            if handType2 == "Left" and h2c == bs and h1c != bs:  # Left Host
                fc = h1c
                for i in range(0, 6):
                    if i == fc:
                        bri = listB2[i]
                        print(bri)
                        sbc.set_brightness(bri)

            if handType1 == "Right" and h1c == bs and h2c != bs:  # Right Host
                fc = h2c
                for i in range(0, 6):
                    if i == fc:
                        bri = listB2[i]
                        print(bri)
                        sbc.set_brightness(bri)
            if handType2 == "Right" and h2c == bs and h1c != bs:  # Right Host
                fc = h1c
                for i in range(0, 6):
                    if i == fc:
                        bri = listB2[i]
                        print(bri)
                        sbc.set_brightness(bri)

    cv2.imshow("VolumeBrightness", img)
    if cv2.waitKey(1) & 0xff == ord(' '):
        break

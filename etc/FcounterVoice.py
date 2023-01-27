import time
from cvzone.HandTrackingModule import HandDetector
from playsound import playsound
import cv2

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.7, maxHands=2)


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
    elif ar == [1, 1, 0, 0, 0]:
        return 6
    elif ar == [1, 1, 1, 0, 0]:
        return 7
    elif ar == [1, 1, 1, 1, 0]:
        return 8
    elif ar == [0, 1, 0, 0, 1]:
        return 9
    elif ar == [1, 1, 0, 0, 1]:
        return 10


def getSound(n):
    try:
        if n == 0:
            return playsound('D:\Pycharm Projects\pythonProject\Sounds\S0.mp3')
        elif n == 1:
            return playsound('D:\Pycharm Projects\pythonProject\Sounds\S1.mp3')
        elif n == 2:
            return playsound('D:\Pycharm Projects\pythonProject\Sounds\S2.mp3')
        elif n == 3:
            return playsound('D:\Pycharm Projects\pythonProject\Sounds\S3.mp3')
        elif n == 4:
            return playsound('D:\Pycharm Projects\pythonProject\Sounds\S4.mp3')
        elif n == 5:
            return playsound('D:\Pycharm Projects\pythonProject\Sounds\S5.mp3')
        elif n == 6:
            return playsound('D:\Pycharm Projects\pythonProject\Sounds\S6.mp3')
        elif n == 7:
            return playsound('D:\Pycharm Projects\pythonProject\Sounds\S7.mp3')
        elif n == 8:
            return playsound('D:\Pycharm Projects\pythonProject\Sounds\S8.mp3')
        elif n == 9:
            return playsound('D:\Pycharm Projects\pythonProject\Sounds\S9.mp3')
        elif n == 10:
            return playsound('D:\Pycharm Projects\pythonProject\Sounds\S10.mp3')
        else:
            print("Error in func gsound")
    except:
        print("Error")


while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    # hands = detector.findHands(img, draw=False)  # No Draw

    if hands:

        if len(hands) == 1:
            hand1 = hands[0]
            lmList1 = hand1['lmList']
            handType1 = hand1['type']
            h1f = detector.fingersUp(hand1)
            h1c = getCount(h1f)
            if h1c is not None:
                cv2.putText(img, str(h1c), (300, 50), cv2.FONT_ITALIC, 1, (0, 255, 98), 3)
                getSound(h1c)
            time.sleep(0.2)
        if len(hands) == 2:
            hand1 = hands[0]
            lmList1 = hand1['lmList']
            handType1 = hand1['type']
            h1f = detector.fingersUp(hand1)
            h1c = getCount(h1f)
            cv2.putText(img, str(h1c), (10, 50), cv2.FONT_ITALIC, 1, (0, 255, 98), 3)
            hand2 = hands[1]
            lmList2 = hand2['lmList']
            bbox2 = hand2['bbox']
            centerPoint2 = hand2['center']
            handType2 = hand2['type']
            h2f = detector.fingersUp(hand2)
            h2c = getCount(h2f)
            print(handType1, handType2)
            cv2.putText(img, str(h2c), (600, 50), cv2.FONT_ITALIC, 1, (0, 255, 98), 3)
            listT = [11, 12, 13]

            if h1c is not None and h2c is not None:
                if h1c == 5 or h2c == 5:
                    total = h1c + h2c
                    if h1c == 5 or h2c == 5:
                        cv2.putText(img, str(total), (300, 50), cv2.FONT_ITALIC, 1, (0, 255, 98), 3)
                        getSound(total)
                    if h1c == 0 or h2c == 0:
                        cv2.putText(img, str(total), (300, 50), cv2.FONT_ITALIC, 1, (0, 255, 98), 3)
                        getSound(total)
                elif h1c == 0 and h2c == 0:
                    listSound = ["D:\Pycharm Projects\pythonProject\Sounds\Virtualife intro for finger count.mp3",
                                 "D:\Pycharm Projects\pythonProject\Sounds\1-5.mp3",
                                 "D:\Pycharm Projects\pythonProject\Sounds\6-10intro.mp3",
                                 "D:\Pycharm Projects\pythonProject\Sounds\6-10.mp3"]
                    for i in listSound:
                        print(i)
                        playsound(i)

            # print(handType1, handType2)

    cv2.imshow('FcounterVoice', img)
    if cv2.waitKey(1) & 0xff == ord(' '):
        break

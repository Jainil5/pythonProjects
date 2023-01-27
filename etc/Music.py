import os
import time
import cv2
import youtube3
from cvzone.HandTrackingModule import HandDetector
import webbrowser
import pychrome


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
    else:
        return 'None'


def playVideo(n:int):
    try:
        if n == 0:
            pass
        elif n == 1:
            # Until I found You
            return "https://music.youtube.com/watch?v=znvky0Uq8qc"
        elif n == 2:
            # Often Kygo Remix
            return "https://music.youtube.com/watch?v=qsDfFE2i0Ws"
        elif n == 3:
            # Starboy
            return "https://music.youtube.com/watch?v=3_g2un5M350"
        elif n == 4:
            # YT playlist 1
            return "https://music.youtube.com/watch?v=AJL_aVxqMEc&list=PLEZtw9WFgxhtTxc69kE2SGay-ixhRsrFv"
        elif n == 5:
            # YT playlist 2
            return "https://music.youtube.com/watch?v=TA1W-pHNKl8&list=PLEZtw9WFgxhvRWyo3Soz_rwJv8A9QvzNj"


    except:
        print("Error")


while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)  # With Draw
    # hands = detector.findHands(img, draw=False)  # No Draw

    if hands:
        global h1c
        global h2c
        global url

        if len(hands) == 2:
            hand1 = hands[0]
            lmList1 = hand1["lmList"]
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
            #print(handType1, handType2)
            vs=8
            if h1c!=h2c:
                listU = []
                # Left Host
                if handType1=="Left" and h1c==8:
                    fc = h2c
                    for i in range(1, 6):
                        if i == fc:
                            url = playVideo(i)
                            webbrowser.open(url)
                            if url:
                                listU.append(url)
                            time.sleep(5)
                if handType2 == "Left" and h2c==8:
                    fc = h1c
                    for i in range(1, 6):
                        if i == fc:
                            url = playVideo(i)
                            webbrowser.open(url)
                            if url:
                                listU.append(url)
                            time.sleep(5)
            elif h1c==8 and h2c==8:
                os.system("taskkill /im chrome.exe /f")



    cv2.imshow('Fcounter', img)
    if cv2.waitKey(1) & 0xff == ord(' '):
        break

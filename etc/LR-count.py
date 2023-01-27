# Importing Libraries
import cv2
import mediapipe as mp
from google.protobuf.json_format import MessageToDict
import HandTrackingModule as htm

mpHands = mp.solutions.hands
hands = mpHands.Hands()
cap = cv2.VideoCapture(0)
detector = htm.handDetector(detectionCon=0.75)


def getNumber(ar):
    if ar == [0,0,0,0,0]:
        return 0
    elif ar == [0,1,0,0,0]:
        return 1
    elif ar == [0,1,1,0,0]:
        return 2
    elif ar == [0,1,1,1,0]:
        return 3
    elif ar == [0,1,1,1,1]:
        return 4
    elif ar == [1,1,1,1,1]:
        return 5
    elif ar == [0,1,0,0,1]:
        return 6
    elif ar == [0,1,0,1,1]:
        return 7


while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = detector.findHands(img, draw=True)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for i in results.multi_handedness:
            if len(results.multi_handedness) == 2:
                cv2.putText(img, 'Both Hands', (250, 50), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 255, 0), 2)

            else:
                for i in results.multi_handedness:
                    label = MessageToDict(i)['classification'][0]['label']
                    if label == 'Left':
                        lmList = detector.findPosition(img, draw=False)
                        cv2.putText(img, label + ' Hand', (20, 20), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 255, 0), 2)
                        if len(lmList) != 0:
                            fl = []
                            tipId = [4, 8, 12, 16, 20]
                            if lmList[tipId[0]][1] > lmList[tipId[0] - 1][1]:  # thumb
                                fl.append(1)
                            else:
                                fl.append(0)
                            # print(fl)
                            for id in range(1, len(tipId)):  # 4 fingers
                                if lmList[tipId[id]][2] < lmList[tipId[id] - 2][2]:
                                    fl.append(1)
                                else:
                                    fl.append(0)
                            print(fl)
                            cv2.putText(img, str(getNumber(fl)), (20, 300), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 255, 0), 2)
                    if label == 'Right':
                        lmList2 = detector.findPosition(img, draw=False)
                        cv2.putText(img, label + ' Hand', (500, 20), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 255, 0), 2)
                        if len(lmList2) != 0:
                            fr = []
                            tipId = [4, 8, 12, 16, 20]
                            if lmList2[tipId[0]][1] < lmList2[tipId[0] - 1][1]:  # thumb
                                fr.append(1)
                            else:
                                fr.append(0)
                            # print(fr)
                            for id in range(1, len(tipId)):  # 4 fingers
                                if lmList2[tipId[id]][2] < lmList2[tipId[id] - 2][2]:
                                    fr.append(1)
                                else:
                                    fr.append(0)
                            print(fr)
                            cv2.putText(img, str(getNumber(fr)), (500, 300), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 255, 0), 2)


    cv2.imshow('LRCount', img)
    if cv2.waitKey(1) & 0xff == ord(' '):
        break

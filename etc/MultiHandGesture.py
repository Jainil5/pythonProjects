import cv2
from cvzone.HandTrackingModule import HandDetector
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)


def getCount(ar):
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
    hands, img = detector.findHands(img)  # With Draw
    # hands = detector.findHands(img, draw=False)  # No Draw

    if hands:
        # Hand 1
        global h1c
        global h2c

        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmarks points
        bbox1 = hand1["bbox"]  # Bounding Box info x,y,w,h
        centerPoint1 = hand1["center"]  # center of the hand cx,cy
        handType1 = hand1["type"]  # Hand Type Left or Right
        h1f=detector.fingersUp(hand1)
        h1c=getCount(h1f)
        print(handType1)


        # print(len(lmList1),lmList1)
        # print(bbox1)
        # print(centerPoint1)
        fingers1 = detector.fingersUp(hand1)
        # length, info, img = detector.findDistance(lmList1[8], lmList1[12], img) # with draw
        # length, info = detector.findDistance(lmList1[8], lmList1[12])  # no draw

        if len(hands) == 2:
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # List of 21 Landmarks points
            bbox2 = hand2["bbox"]  # Bounding Box info x,y,w,h
            centerPoint2 = hand2["center"]  # center of the hand cx,cy
            handType2 = hand2["type"]  # Hand Type Left or Right
            h2f=detector.fingersUp(hand2)
            h2c=getCount(h2f)
            print(handType2)

            # print(fingers1, fingers2)
            # length, info, img = detector.findDistance(lmList1[8], lmList2[8], img) # with draw
            #length, info, img = detector.findDistance(centerPoint1, centerPoint2, img)  # with draw

            cv2.putText(img, str(h1c), (10, 40), cv2.FONT_ITALIC, 1, (0, 255, 98), 3)
            cv2.putText(img, str(h2c), (600, 40), cv2.FONT_ITALIC, 1, (0, 255, 98), 3)


    cv2.imshow("MuHandGes", img)
    if cv2.waitKey(1) & 0xff == ord(' '):
        break
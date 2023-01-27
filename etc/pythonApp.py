import tkinter as tk
import cv2
from PIL import Image, ImageTk
from cvzone.HandTrackingModule import HandDetector
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc
import mediapipe as mp

width, height = 800, 600
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
detector = HandDetector(detectionCon=0.9, maxHands=2)
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volMin, volMax = volume.GetVolumeRange()[:2]

root = tk.Tk()
root.bind('<Escape>', lambda e: root.quit())
lmain = tk.Label(root)
lmain.pack()


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


def show_frame():
    success, img = cap.read()
    img = cv2.flip(img, 1)
    cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)

    # code
    hands, img = detector.findHands(img)  # With Draw
    # hands = detector.findHands(img, draw=False)  # No Draw

    if hands:
        if len(hands) == 2:
            hand1 = hands[0]
            handType1 = hand1["type"]
            h1f = detector.fingersUp(hand1)
            h1c = getCount(h1f)
            hand2 = hands[1]
            handType2 = hand2["type"]
            h2f = detector.fingersUp(hand2)
            h2c = getCount(h2f)
            listV1 = [-65.25, -23.654823303222656, -10.329694747924805, -5.290315628051758,
                      -3.4243249893188477, 0, 0]
            listB1 = [0, 20, 40, 60, 80, 100, 100]
            vs = 2  # volume
            bs = 1  # Brightness
            # Volume and Brightness
            if handType1 == "Left":  # Left Host
                if h1c == vs:
                    fc = h2c
                    for i in range(0, 6):
                        if i == fc:
                            vol = listV1[i]
                            volume.SetMasterVolumeLevel(vol, None)
                if h1c == bs:
                    fc = h2c
                    for i in range(0, 6):
                        if i == fc:
                            bri = listB1[i]
                            sbc.set_brightness(bri)
            if handType2 == "Left":  # Left Host
                if h2c == vs:
                    fc = h1c
                    for i in range(0, 6):
                        if i == fc:
                            vol = listV1[i]
                            volume.SetMasterVolumeLevel(vol, None)
                if h2c == bs:
                    fc = h1c
                    for i in range(0, 6):
                        if i == fc:
                            bri = listB1[i]
                            sbc.set_brightness(bri)

    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)
    if cv2.waitKey(1) & 0xff == ord(' '):
        breakpoint()


show_frame()
root.mainloop()

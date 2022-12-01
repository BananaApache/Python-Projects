
import sys
sys.path.append("/Library/Python/3.8/site-packages")
import sys
import os
conf_path = os.getcwd()
sys.path.append(conf_path)
sys.path.append(conf_path + '\scripts\Setup') 
import time as t
from HandTrack import *
import pyautogui as pg
from screeninfo import get_monitors
import cv2 as cv
import sys
import os
sys.path.append('/Users/dli/Documents/python_proj/opencv/hand_detect')


if __name__ == "__main__":
    prevTime = 0
    currentTime = 0
    webcam = cv.VideoCapture(0)
    detector = HandTrack()

    safari_path = "/Applications/Safari.app"

    while True:
        isTrue, frame = webcam.read()

        m = get_monitors()
        height = int(str(m).split(",")[3][8:])  # IS THE HEIGHT
        width = int(str(m).split(",")[2][7:])  # IS THE WIDTH
        frame = cv.resize(frame, (width, height))
        frame = cv.flip(frame, 1)

        frame = detector.findHands(frame)
        lmList = detector.findPosition(frame)
        if len(lmList) != 0:
            pg.moveTo(x=lmList[0][1], y=lmList[0][2])
            if lmList[12][2] > lmList[10][2] and lmList[16][2] > lmList[14][2] and lmList[20][2] > lmList[18][2]:
                pg.click()
                t.sleep(1)
            elif lmList[16][2] > lmList[14][2] and lmList[20][2] > lmList[18][2]:
                pg.click(button="right")
                t.sleep(1)
            elif lmList[8][2] > lmList[5][2] and lmList[12][2] > lmList[10][2] and lmList[16][2] > lmList[14][2]:
                os.system(f"open {safari_path}")
            elif lmList[4][2] < lmList[18][2]:
                break

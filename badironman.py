import time
import serial
from tkinter import *
import cv2
import imutils
import sys
import numpy as np
import asyncio

# open cv variables
frameWidth = 1000
frameHeight = 1000
camera = cv2.VideoCapture(0)
camera.set(3, frameWidth)
camera.set(4, frameWidth)
camera.set(10, 130)
handCascade = cv2.CascadeClassifier('hand.xml')


# serial stuff
ser = serial.Serial(
    port = "COM3",
    baudrate=9600,
)

if ser.isOpen == False:
    ser.open()

def writeToPort(coords):
    if ser.isOpen:
        try:
            ser.write(coords)
        except:
            ser.close()
            time.sleep(0.015)
            ser.open()
    

def motion(x, y):
    nX = round(180 - x / (1000 / 180))
    nY = round(180 - y / (1000 / 180))
    if x > 0 and y > 0 and ser.isOpen:
        try:
            mouseCoords = bytes(("X" + str(nX) + "Y" + str(nY)), encoding='utf-8')
            writeToPort(mouseCoords)
        except:
            print("fuck")

def home(event):
    coords = bytes(("X90Y30"), encoding='utf-8') 
    writeToPort(coords)

# image processing loop to look for hands



# main while loop
while camera.isOpened(): 
    success, img = camera.read()
    greyImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hands = handCascade.detectMultiScale(greyImg, 1.1, 4)
    i = 0
    if (str(hands) != "()"):
        hand = hands[0]
        for i in hand:
            (x, y, w, h) = hand
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            motion(x, y)
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        camera.release()
        cv2.destroyAllWindows()
        break
        

camera.release()
sys.exit(1)
cv2.destroyAllWindows()        
        


            
            




import time
import serial
from tkinter import *

window = Tk()
window.geometry("600x600")
window.title("Laser Turret")

ser = serial.Serial(
    port = "COM3",
    baudrate=9600,
    timeout = 0,
    writeTimeout = 0,
)

def writeToPort(coords):
        try:
            ser.write(coords)
        except:
            ser.close()
            ser.open()
            print('ah fuck')
            print(coords)

def motion(event):
    stopTime = time.time()
    if stopTime % 0.000005 == 0:
        x, y = event.x, event.y
        nX = round(180 - x / (600 / 180))
        nY = round(180 - y / (600 / 180))
        mouseCoords = bytes(("X" + str(nX) + "Y" + str(nY)), encoding='utf-8')
        writeToPort(mouseCoords)
        print(stopTime)


stopTime = 0

window.bind('<Motion>', motion)
window.mainloop()




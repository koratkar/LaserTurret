import time
import serial
from tkinter import *

window = Tk()
window.geometry("600x600")
window.title("Laser Turret")

ser = serial.Serial(
    port = "COM3",
    baudrate=9600,
)

if ser.isOpen == False:
    ser.open()

def writeToPort(coords):
    try:
        ser.write(coords)
    except:
        ser.close()
        ser.open()
    

def motion(event):
    x, y = event.x, event.y
    nX = round(180 - x / (600 / 180))
    nY = round(180 - y / (600 / 180))
    if x > 0 and y > 0:
        mouseCoords = bytes(("X" + str(nX) + "Y" + str(nY)), encoding='utf-8')
        writeToPort(mouseCoords)
        time.sleep(0.015)

window.bind('<Motion>', motion)
window.mainloop()
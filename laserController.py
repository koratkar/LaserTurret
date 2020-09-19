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
            window.unbind('<Motion>')
            ser.open()
            window.bind('<Motion>', motion)

def motion(event):
    x, y = event.x, event.y
    if x > 0 and y > 0:
        nX = round(180 - x / (600 / 180))
        nY = round(180 - y / (600 / 180))
        time.sleep(0.015)
        mouseCoords = bytes(("X" + str(nX) + "Y" + str(nY)), encoding='utf-8')
        writeToPort(mouseCoords)

def home(event):
    coords = bytes(("X90Y30"), encoding='utf-8') 
    writeToPort(coords)

window.bind('<Motion>', motion)
ser.close()
ser.open()
window.mainloop()
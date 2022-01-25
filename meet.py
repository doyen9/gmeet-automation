from operator import truediv
import sys
import pyautogui as pg
import webbrowser
import time
import datetime
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
from time import strftime
import win32gui, win32con
import os

link = input("your link :  ")

timenow = datetime.datetime.now().strftime("%H : %M : %S")
print(timenow)

hr1 = 23
mn1 = 30
hr2 = 22
time.sleep(3)
p1 = pg.position()
print((p1))
pmic = 409, 567
pvid = 488, 571
pjoin = 980, 426

while True:
    if hr1 == datetime.datetime.now().hour :
        #  os.system("taskkill/f /im chrome.exe")
         print("leaving the meet")

    elif hr2 == datetime.datetime.now().hour:
        print("class time bro")

        webbrowser.get(chrome_path).open(link)
        time.sleep(4)
        pg.click(pmic)
        time.sleep(1)
        pg.click(pvid)
        time.sleep(1)
        pg.click(pjoin)
        print("joined the class bro")

        time.sleep(71998)
        print("leaving the class man")
        os.system("ttaskkill/f /im chrome.exe")


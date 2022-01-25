
import sys
import pyautogui as pg
import webbrowser
import time
import datetime
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s' #---->standard path for chrome
from time import strftime
import win32gui, win32con
import os

link = input("your link :  ") #-----> ur link will be entered here

timenow = datetime.datetime.now().strftime("%H : %M : %S") #---->current time
print(timenow)

hr1 = 23  #---> afternnoon break time hour, mention the hour in 24 hrs format - 1pm
mn1 = 30  #----> afternoon break time minute --> 30 mins
hr2 = 22 #---> afternnon class time, hour ->2pm
time.sleep(3)
p1 = pg.position() #------>used to find coordinates of pointer

print((p1))
pmic = 409, 567
pvid = 488, 571
pjoin = 980, 426 # ----> coordinates of the mic , cam , join button on chrome

while True:
    if hr1 == datetime.datetime.now().hour :
        #  os.system("taskkill/f /im chrome.exe") #----> exits ur class at 1 30 pm
         print("leaving the meet")

    elif hr2 == datetime.datetime.now().hour:
        print("class time bro")

        webbrowser.get(chrome_path).open(link) # -----> rejoins the meeting at 2 pm
        time.sleep(6)             #turns off ur mic, cam and joins the class
        pg.click(pmic)
        time.sleep(1)
        pg.click(pvid)
        time.sleep(1)
        pg.click(pjoin)
        print("joined the class bro")

        time.sleep(15) # ---> ur total class time in seconds, type in ur class time in seconds in place of x , like, .sleep(x)
        print("leaving the class man")
        os.system("taskkill/f /im chrome.exe")
        break


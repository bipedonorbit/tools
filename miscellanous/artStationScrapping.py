import pyautogui
from pyautogui import *
import win32api, win32con
import time
import cv2
import os
import time 

from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)



def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


def nextPage():
    pyautogui.press('right') 


def makeACircle():
    position=pyautogui.position()
    radius=10
    time=0.05
    pyautogui.moveTo(position[0]+radius/2,position[1],time)
    pyautogui.moveTo(position[0]+radius/2.5,position[1]+radius/2.5,time)
    pyautogui.moveTo(position[0],position[1]+radius/2,time)
    pyautogui.moveTo(position[0]-radius/2.5,position[1]+radius/2.5,time)
    pyautogui.moveTo(position[0]-radius/2,position[1],time)
    pyautogui.moveTo(position[0]-radius/2.5,position[1]-radius/2.5,time)
    pyautogui.moveTo(position[0],position[1]-radius/2,time)
    pyautogui.moveTo(position[0]+radius/2.5,position[1]-radius/2.5,time)
    pyautogui.moveTo(position[0]+radius/2.5,position[1]+radius/2.5,time)


def checkForImg(img):
    try:
        location = pyautogui.locateCenterOnScreen(img,confidence=0.9)
        if location:
            print(f'{os.path.basename(img)} found on the screen!')
        else:
            print(f'{os.path.basename(img)} not found')
        return(location)
    
    except pyautogui.ImageNotFoundException:
        print(f'{os.path.basename(img)} not found on the screen :(')
        return("imgNotFound")


def ClickOnArtstationWindow():
    previousLocation=checkForImg(previousButton)
    if previousLocation == "imgNotFound":
        print("artstation windows not detected")
        return False
    else:
        click(previousLocation[0],previousLocation[1])
        return True


def findPostFrame():
    scrollStep=-300
    scrollScore=0
    postFrame=[]
    condition=False

    while not condition:
        likeLocation=checkForImg(likeButton)
        likedLocation=checkForImg(likedButton)
        if likedLocation=="imgNotFound" and likeLocation=="imgNotFound":
            condition=False
            pyautogui.scroll(scrollStep)
            scrollScore=+1
            print("I scroll ...")
        else :
            condition=True
            print(f'i found the like button ! i needed to scroll {scrollScore} times {scrollStep}px')
    
    likeLocation=checkForImg(likeButton)
    if likeLocation=="imgNotFound":
        likeLocation=checkForImg(likedButton)

    print(f'{likeLocation} is the likeLocation')
    print(f'i add {scrollScore} times 300px to the y value of the like button:')
    likeLocation=Point(likeLocation.x, likeLocation.y + scrollScore*scrollStep)
    print(f'so the like location is in reel :{likeLocation}')
    
    previousLocation=checkForImg(previousButton)
    if previousLocation == "imgNotFound":
        return "previous Location not found"

    top=previousLocation[1]+22
    bot=likeLocation[1]-70
    left=likeLocation[0]-230
    right=likeLocation[0]+228

    topLeftCorner=[left,top]
    topRightCorner=[right,top]
    botRightCorner=[right,bot]
    botLeftCorner=[left,bot]

    pyautogui.moveTo(topLeftCorner[0], topLeftCorner[1], 0.3) 
    pyautogui.moveTo(topRightCorner[0], topRightCorner[1], 0.3) 
    pyautogui.moveTo(botRightCorner[0], botRightCorner[1], 0.3) 
    pyautogui.moveTo(botLeftCorner[0], botLeftCorner[1], 0.3) 

    postFrame.append(top)
    postFrame.append(bot)
    postFrame.append(left)
    postFrame.append(right)

    return postFrame


def downloadPostImages(downloadButtons):
    for button in downloadButtons:
        pyautogui.moveTo(button) 
        makeACircle()


def findDownloadButtons(postFrame):
    top=postFrame[0]
    bot=postFrame[1]
    downloadButtonsLocations=[]
    artStationMid=-870
    print(f'the top of the frame is {top}')
    print(f'the bot of the frame is {bot}')
    distance=top-bot
    print(f'the distance between them is {distance}')
    stepCount=10
    stepDistance=distance/stepCount
    print(f'if I divide it by stepCount({stepCount}) i obtain {stepDistance} ')
    print(f'so i will move the cursor {stepCount} times {stepDistance} ')
    pyautogui.moveTo(artStationMid, top) 
    for step in range(stepCount):
        mousePostion=pyautogui.position()
        print(f'i move it :{str(mousePostion[1]-stepDistance)} {str(step)}')
        pyautogui.moveTo(artStationMid, mousePostion[1]-stepDistance)
        dowloadLocation=checkForImg(domnloadIcon)
        print(dowloadLocation)
        downloadButtonsLocations.append(dowloadLocation)
    downloadButtonsLocations = list(set(downloadButtonsLocations))
    for point in downloadButtonsLocations:
        if point == 'imgNotFound':
            downloadButtonsLocations.remove(point)
        else:
            pass
    print(f'the position of the buttons detected is: {downloadButtonsLocations}')
    return downloadButtonsLocations

# force use of ImageNotFoundException
#pyautogui.useImageNotFoundException()

artStationRegion = (-1080, -433, -540, 1455)
domnloadIcon = r"C:\Users\Biiiped\Documents\Current projects\mes codes edit\artStationScrapping\img\downloadIcon.png"
likeButton = r"C:\Users\Biiiped\Documents\Current projects\mes codes edit\artStationScrapping\img\likeButton.png"
likedButton= r"C:\Users\Biiiped\Documents\Current projects\mes codes edit\artStationScrapping\img\likedButton.png"
previousButton = r"C:\Users\Biiiped\Documents\Current projects\mes codes edit\artStationScrapping\img\previousButton.png"
dragon = r"C:\Users\Biiiped\Documents\Current projects\mes codes edit\artStationScrapping\img\red eyes dragon.png"
postCount=10


artStationWindow=ClickOnArtstationWindow()
if artStationWindow==True:
    for _ in range(postCount):
        postFrame =findPostFrame()
        downloadButtons=findDownloadButtons(postFrame)
        downloadPostImages(downloadButtons)
        nextPage()

        print("___________")
        print("next post !")
        print("___________")
        time.sleep(1)
else:
    pass


#pyautogui.displayMousePosition()


#time.sleep(3)
"""for _ in range(30):
    checkForImg(dragon)
    time.sleep(1)"""

#downloadLocation=checkForImg(domnloadIcon)
#if downloadLocation == "imgNotFound":
#    return "framingFailed"
import pyautogui
import time as t
import cv2
from bs4 import BeautifulSoup

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# myScreenshot = pyautogui.screenshot()
# myScreenshot.save('detectedImage.png')

# src = cv2.imread("detectedImage.png", cv2.IMREAD_GRAYSCALE)
# templit = cv2.imread("downloadButton.png", cv2.IMREAD_GRAYSCALE)
# dst = cv2.imread("detectedImage.png")

# result = cv2.matchTemplate(src, templit, cv2.TM_SQDIFF_NORMED)

# minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
# x, y = minLoc
# h, w = templit.shape

# dst = cv2.rectangle(dst, (x, y), (x +  w, y + h) , (0, 0, 255), 1)

# print("x:{0} y:{1} width:{2} height:{3}", x,y,w,h )
# pyautogui.click(x+w/2,y+h/2) 
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# browser.execute_script("window.scrollTo(0, Y)")


# print(pyautogui.position())

# # s = pyautogui.size()

# pyautogui.click(920,685)
# t.sleep(2)
# pyautogui.click(1475,1185) 
# t.sleep(2)
# pyautogui.click(1280,685)
# t.sleep(2)
# pyautogui.click(1475,1185) 
# t.sleep(2)
# pyautogui.click(1640,685)
# t.sleep(2)
# pyautogui.click(1475,1185) 
# t.sleep(2)

# pyautogui.scroll(-350)   
# t.sleep(2)

# for i in range(5):
#     pyautogui.click(920,1220)
#     t.sleep(2)
#     pyautogui.click(1436,1160) 
#     t.sleep(2)
#     pyautogui.click(1280,650)
#     t.sleep(2)
#     pyautogui.click(1436,1160) 
#     t.sleep(2)
#     pyautogui.click(1640,650)
#     t.sleep(2)
#     pyautogui.click(1436,1160) 
#     t.sleep(2)
#     pyautogui.scroll(-324)    
#     t.sleep(2)

# pyautogui.scroll(-1440)   
# t.sleep(5)


# pyautogui.click(1272,900) #click load more button
# t.sleep(2)
# pyautogui.click(920,1040)
# t.sleep(2)
# pyautogui.click(1480,992)
# t.sleep(2)
# pyautogui.click(1280,500)
# t.sleep(2)
# pyautogui.click(1480,992)
# t.sleep(2)
# pyautogui.click(1640,500)
# t.sleep(2)
# pyautogui.click(1480,992)
# t.sleep(2)
# pyautogui.scroll(-119)   
# t.sleep(2)

# for i in range(True):    
#     pyautogui.click(920,1220)
#     t.sleep(2)
#     pyautogui.click(1436,1160) 
#     t.sleep(2)
#     pyautogui.click(1280,650)
#     t.sleep(2)
#     pyautogui.click(1436,1160) 
#     t.sleep(2)
#     pyautogui.click(1640,650)
#     t.sleep(2)
#     pyautogui.click(1436,1160) 
#     t.sleep(2)
#     pyautogui.scroll(-324)    
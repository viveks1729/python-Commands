import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service('D:\selenium webdrivers\chromedriver.exe')

browser = webdriver.Chrome(service=s)
browser.maximize_window()
browser.get("https://demo.automationtesting.in/Frames.html")

#browser.find_element(By.LINK_TEXT,"Iframe with in an Iframe").click()
browser.switch_to.frame(0)
#browser.switch_to.frame(0)


browser.find_element(By.XPATH, "/html/body/section/div/div/div/input").send_keys("Commander")
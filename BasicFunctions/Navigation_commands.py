import time
import robot
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s=Service('D:\selenium webdrivers\chromedriver.exe')

browser = webdriver.Chrome(service=s)

browser.get("https://www.nike.com/in/")
print(browser.title)
time.sleep(5)
browser.get("https://www.adidas.co.in/")
print(browser.title)
time.sleep(5)
browser.back()
print(browser.title)
time.sleep(5)
browser.forward()
print(browser.title)
time.sleep(5)

browser.quit()
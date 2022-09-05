import time

from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service('D:\selenium webdrivers\chromedriver.exe')

browser = webdriver.Chrome(service=s)
browser.get("https://demo.guru99.com/test/simple_context_menu.html")

action= ActionChains(browser)
action.double_click(browser.find_element(By.XPATH, "//button[@ondblclick='myFunction()']")).perform()
time.sleep(2)
browser.switch_to.alert.accept()
time.sleep(3)

browser.close()


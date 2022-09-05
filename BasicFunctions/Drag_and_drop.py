import time

from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service('D:\selenium webdrivers\chromedriver.exe')

browser = webdriver.Chrome(service=s)
browser.maximize_window()
#browser.execute_script("window.scrollBy(0,200)","")
browser.get("https://demo.guru99.com/test/drag_drop.html")
time.sleep(3)
sourc= browser.find_element(By.XPATH, "//li[@id='fourth'][2]")
destn= browser.find_element(By.ID, "amt7")

action= ActionChains(browser)
action.drag_and_drop(sourc,destn).perform()
time.sleep(3)

browser.quit()

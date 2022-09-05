import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service('D:\selenium webdrivers\chromedriver.exe')

browser = webdriver.Chrome(service=s)
browser.get("https://demo.automationtesting.in/Windows.html")

browser.find_element(By.LINK_TEXT, "Open Seperate Multiple Windows").click()
browser.find_element(By.XPATH, "//button[@onclick='multiwindow()']").click()

windowList= browser.window_handles
for windows in windowList:
    browser.switch_to.window(windows)
    time.sleep(2)
    print("{} - {}".format(browser.title,windows) )

browser.quit()
from selenium.common import NoSuchElementException

import XLUtils
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service('D:\selenium webdrivers\chromedriver.exe')

browser = webdriver.Chrome(service=s)
browser.maximize_window()
#browser.get("https://practice.automationtesting.in/my-account/")
path= "D:\Data1.xlsx"

rows = XLUtils.getRowCount(path, "Sheet1")
columns = XLUtils.getColumnCount(path, "Sheet1")

for r in range(2,rows+1):
    browser.get("https://practice.automationtesting.in/my-account/")
    user= XLUtils.readData(path, "Sheet1", r, 1)
    password= XLUtils.readData(path, "Sheet1", r, 2)
    browser.find_element(By.ID, "username").send_keys(user)
    browser.find_element(By.ID, "password").send_keys(password)
    #time.sleep(3)
    browser.find_element(By.NAME, "login").click()
    #print(user, "   ", password)
    time.sleep(2)
    try:
        browser.find_element(By.LINK_TEXT, "Orders").is_enabled()

    except NoSuchElementException:
        print("Fail")
        XLUtils.writeData(path, "Sheet1", r, 3, "Fail")

    else:
        print("Pass")
        XLUtils.writeData(path, "Sheet1", r, 3, "Pass")
        browser.find_element(By.LINK_TEXT, "Logout").click()

time.sleep(5)
browser.quit()

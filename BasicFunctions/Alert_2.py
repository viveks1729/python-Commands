import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service('D:\selenium webdrivers\chromedriver.exe')

browser = webdriver.Chrome(service=s)
browser.get("https://dev01-amastore-lsco.demandware.net/s/LeviAU")
time.sleep(3)
#print(browser.switch_to.alert.text)
#browser.implicitly_wait(10)
#time.sleep(3)
#browser.switch_to.alert.send_keys("storefront\tinfy123")
#time.sleep(3)
#browser.switch_to.alert.dismiss()

browser.quit()

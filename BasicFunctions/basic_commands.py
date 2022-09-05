import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service('D:\selenium webdrivers\chromedriver.exe')

browser = webdriver.Chrome(service=s)

browser.get("https://demo.automationtesting.in/Windows.html")

print(browser.title)

browser.find_element(By.XPATH,"//*[@id='Tabbed']/a/button").click()

time.sleep(5)

#browser.close()
browser.quit()


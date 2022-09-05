import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service('D:\selenium webdrivers\chromedriver.exe')

browser = webdriver.Chrome(service=s)
browser.get("https://demo.automationtesting.in/Register.html")

check_count= browser.find_elements(By.CLASS_NAME, "checks")
print(len(check_count))

cricket=browser.find_element(By.ID, "checkbox1")
print(cricket.is_selected())
cricket.click()
print(cricket.is_selected())

browser.quit()

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

s=Service('D:\selenium webdrivers\chromedriver.exe')

browser = webdriver.Chrome(service=s)
browser.get("https://demo.automationtesting.in/Register.html")

drpdwn= Select(browser.find_element(By.CLASS_NAME, "select2-hidden-accessible"))

for opt in drpdwn.options:
    print(opt.text)

drpdwn.select_by_visible_text("India")
time.sleep(3)
drpdwn.select_by_index(9)
time.sleep(3)
drpdwn.select_by_value("Denmark")
time.sleep(3)
browser.quit()


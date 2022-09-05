import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service('D:\selenium webdrivers\chromedriver.exe')

browser = webdriver.Chrome(service=s)

browser.get("https://demo.automationtesting.in/Register.html")

browser.implicitly_wait(15)
assert "Register" in browser.title

browser.find_element(By.XPATH, "//input[@type='text' and @placeholder='First Name']").send_keys("Luka")
browser.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Modric")
browser.find_element(By.NAME, "signup").click()

time.sleep(3)

browser.close()
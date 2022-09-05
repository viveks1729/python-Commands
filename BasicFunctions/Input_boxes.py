import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service('D:\selenium webdrivers\chromedriver.exe')

browser = webdriver.Chrome(service=s)
browser.get("https://demo.automationtesting.in/Register.html")

browser.find_element(By.XPATH, "//input[@type='text' and @placeholder='First Name']").send_keys("Jim")

browser.find_element(By.XPATH, "//input[@type='text' and @placeholder='Last Name']").send_keys("Halpert")

#browser.find_element(By.XPATH, "//textarea[@rows='3']").send_keys("The Office")
browser.execute_script("document.find_element(By.XPATH,'//textarea[@rows='3']').value='Home'")


browser.find_element(By.XPATH, "//input[@type='email']").send_keys("Jim@assistant.com")
time.sleep(10)
browser.find_element(By.XPATH, "//input[@type='radio' and @value='FeMale']").click()
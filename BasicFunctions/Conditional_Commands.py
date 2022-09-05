import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service('D:\selenium webdrivers\chromedriver.exe')

browser = webdriver.Chrome(service=s)

browser.get("https://demo.automationtesting.in/SignIn.html")
browser.maximize_window()

username= browser.find_element(By.XPATH,"/html/body/div/div/div[2]/input")
password= browser.find_element(By.XPATH, "/html/body/div/div/div[3]/input")

print("Username box displayed: ", username.is_displayed())
print("Password box displayed: ", password.is_displayed())

print("Username box enabled: ", username.is_enabled())
print("Password box enabled: ", password.is_enabled())

username.send_keys("Dwayne")
password.send_keys("Johnson")

browser.get("https://demo.automationtesting.in/Register.html")
male_radio= browser.find_element(By.XPATH, "//input[@type='radio' and @value='Male']")
male_radio.click()

print("Radio button selected: ", male_radio.is_selected())
browser.quit()
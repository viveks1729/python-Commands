from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service('D:\selenium webdrivers\chromedriver.exe')

browser = webdriver.Chrome(service=s)
browser.get("https://www.nike.com/in/")
browser.get_screenshot_as_file(r"C:\Users\vivek.s07\Desktop\SSes\A3.png")
print(browser.get_screenshot_as_base64())
print(browser.get_screenshot_as_png())
browser.save_screenshot(r"C:\Users\vivek.s07\Desktop\SSes\A4.png")

browser.quit()
import time

from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service('D:\selenium webdrivers\chromedriver.exe')

browser = webdriver.Chrome(service=s)
browser.get("https://demo.guru99.com/test/simple_context_menu.html")

btn= browser.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
action= ActionChains(browser)
action.context_click(btn).perform()

time.sleep(5)
browser.quit()

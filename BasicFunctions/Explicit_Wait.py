import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service('D:\selenium webdrivers\chromedriver.exe')

browser = webdriver.Chrome(service=s)
browser.maximize_window()
browser.get("https://automationtesting.in/about/")

place=browser.find_element(By.PARTIAL_LINK_TEXT, 'Selenium Webdriver Appium Complete Tutoria')
place.click()

wait= WebDriverWait(browser,10)
element= wait.until(EC.presence_of_element_located((By.NAME, 'EMAIL')))

browser.find_element(By.NAME, 'EMAIL').send_keys("jonathan@mail.com")
browser.find_element(By.XPATH, "//input[@type='submit']").click()

time.sleep(3)
browser.quit()
#browser.find_element(By)







import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service('D:\selenium webdrivers\chromedriver.exe')

browser = webdriver.Chrome(service=s)
browser.get("https://demo.automationtesting.in/Alerts.html")
browser.implicitly_wait(30)

firstoption= browser.find_element(By.XPATH,"//button[@onclick='alertbox()']")
browser.maximize_window()

firstoption.click()
time.sleep(3)
print(browser.switch_to.alert.text)
browser.switch_to.alert.dismiss()

browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a").click()
thirdoption=browser.find_element(By.XPATH, "//button[@onclick='promptbox()']")

thirdoption.click()
time.sleep(3)
print(browser.switch_to.alert.text)
browser.switch_to.alert.send_keys("Boss")
browser.switch_to.alert.accept()

time.sleep(5)
browser.quit()
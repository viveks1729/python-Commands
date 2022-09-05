import time

from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service('D:\selenium webdrivers\chromedriver.exe')

browser = webdriver.Chrome(service=s)
browser.maximize_window()
browser.get("https://demo.automationtesting.in/FileUpload.html")

path= "D:/wall/ferrari_red_novitec_ferrari_sf90_stradale_2022_car_road_8_4k_5k_hd_cars.jpg"
browser.find_element(By.NAME, "input4[]").send_keys(path)
time.sleep(3)
browser.find_element(By.XPATH, "//button[@title='Clear selected files']").click()
time.sleep(3)
browser.quit()

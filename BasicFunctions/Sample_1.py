import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service('D:\selenium webdrivers\chromedriver.exe')

browser = webdriver.Chrome(service=s)
browser.get('https://www.amazon.in/')
links = browser.find_elements(By.CSS_SELECTOR, 'a')
link_list=[]

for link in links:
    link_list.append(link.get_attribute('href'))

for url in link_list:
    print("-",url)
#print(link_list)
browser.quit()
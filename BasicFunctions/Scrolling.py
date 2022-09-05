import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service('D:\selenium webdrivers\chromedriver.exe')

browser = webdriver.Chrome(service=s)
browser.maximize_window()
browser.get("https://time.com/5553690/marvel-cinematic-universe-villains-ranked/")

ego= browser.find_element(By.XPATH, "//*[@id='article-body']/div/div[20]/div/div/figure/picture/img")
browser.execute_script("arguments[0].scrollIntoView();",ego)    #scroll to view a particular element
time.sleep(3)

i=0
while(i<10):
    browser.execute_script("window.scrollBy(0,200)","")
    time.sleep(1)
    i+=1

browser.execute_script("window.scrollBy(0,document.body.scrollHeight)")




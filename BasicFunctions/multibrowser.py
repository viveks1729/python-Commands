from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s=Service('D:\selenium webdrivers\chromedriver.exe')

browser = webdriver.Chrome(service=s)
url='https://www.google.com'
browser.get(url)

print(browser.title)

#print(browser.page_source)

browser.close()

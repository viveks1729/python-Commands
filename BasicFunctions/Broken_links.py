import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#import ssl
#ssl._create_default_https_context = ssl.create_default_context()

s=Service('D:\selenium webdrivers\chromedriver.exe')

browser = webdriver.Chrome(service=s)

browser.get('https://www.amazon.in/')
time.sleep(5)
links = browser.find_elements(By.CSS_SELECTOR, "a")
images = browser.find_elements(By.CSS_SELECTOR,"img")
link_count,image_count=0,0
link_store=[]
none_code=0
for link in links:
    url = link.get_attribute('href')
    link_store.append(url)
    x = requests.get(url)
    if(x is not None):
        print(x.status_code)
    else:
        none_code+=1

#    print(link)
    link_count+=1
for picture in images:
#    print(picture)
    image_count+=1
print("links={} and images={}".format(link_count,image_count))



browser.quit()

#for link in links:
#    r = requests.head(link.get_attribute('href'))
#    print(r.status_code == 200)

for url in link_list:
    if(url is not None):
        x= requests.get(url)
        print("{}  : {}".format(url,x.status_code))
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service('D:\selenium webdrivers\chromedriver.exe')

browser = webdriver.Chrome(service=s)
browser.get("https://www.eurogamer.net/pokemon-go-type-chart-effectiveness-weaknesses")


r= len(browser.find_elements(By.TAG_NAME, "tr"))
c= len(browser.find_elements(By.TAG_NAME, "td"))//(r-1)
print("No. of rows= {} and no. of columns= {}".format(r,c))

for row in range(1,r):
    for column in range(1,c+1):
        data=browser.find_element(By.XPATH,"//tr[{}]/td[{}]".format(row,column)).text
        if(len(data)>20):
            data=data[0:20]
        else:
            data=data+" "*(20-len(data))
        print(data,end="   |  ")
    print()

browser.quit()
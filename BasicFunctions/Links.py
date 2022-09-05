import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

s=Service('D:\selenium webdrivers\chromedriver.exe')

browser = webdriver.Chrome(service=s)
browser.get("https://en.wikipedia.org/wiki/Avengers:_Endgame")

links= browser.find_elements(By.TAG_NAME, "a")
print("No. of links: ",len(links))

print("Links are:")
i=0
for link in links:
    i+=1
    if(i==516):
        print("{}. {}".format(i,link.text))
        break

browser.find_element(By.LINK_TEXT, "Power Stone").click()
wait= browser.implicitly_wait(10)
browser.find_element(By.PARTIAL_LINK_TEXT, "Strange").click()
time.sleep(5)

browser.quit()

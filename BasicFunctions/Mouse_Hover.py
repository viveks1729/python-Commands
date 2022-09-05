import time

from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service('D:\selenium webdrivers\chromedriver.exe')

browser = webdriver.Chrome(service=s)
browser.get("https://www.flipkart.com/")
time.sleep(3)

browser.find_element(By.XPATH, "/html/body/div[2]/div/div/button").click()

electronics= browser.find_element(By.XPATH, "//div[@class='_1mkliO']/div[@class='CXW8mj']/img[@alt='Electronics']")
#gaming= browser.find_element(By.LINK_TEXT, "Gaming")
time.sleep(2)
action=ActionChains(browser)
action.move_to_element(electronics).perform()
time.sleep(5)

gaming= browser.find_element(By.XPATH, "//*[@id='container']/div/div[2]/div/div/div[5]/a/div[2]/div[2]/div[2]/div/div/div[1]/a[5]")
time.sleep(5)
#games= browser.find_element(By.LINK_TEXT, "Games")
games= browser.find_element(By.XPATH, "//*[@id='container']/div/div[2]/div/div/div[5]/a/div[2]/div[2]/div[2]/div/div/div[2]/a[6]")

#action=ActionChains(browser)
action.move_to_element(electronics).move_to_element(gaming).move_to_element(games).click().perform()
time.sleep(7)

browser.quit()



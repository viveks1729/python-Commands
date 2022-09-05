from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s=Service('D:\selenium webdrivers\chromedriver.exe')

browser = webdriver.Chrome(service=s)
browser.get("https://www.nike.com/in/")

cookies= browser.get_cookies()
the_cookie= browser.get_cookie("value")
length= len(cookies)
print(cookies,'\n',the_cookie,'\n',length)

cook= ({'name':'Namor', 'value':'Ocean'})
browser.add_cookie(cook)
print(browser.get_cookies())
print(len(browser.get_cookies()))

browser.delete_cookie('Namor')
print(browser.get_cookies())
print(len(browser.get_cookies()))

browser.quit()
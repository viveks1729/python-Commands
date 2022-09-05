from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

opt= Options()
opt.add_experimental_option("prefs", {"download.default_directory" : "D:\Japan\ipad images JP"})

s=Service('D:\selenium webdrivers\chromedriver.exe')

browser = webdriver.Chrome(service=s,options=opt)
browser.maximize_window()
browser.get("https://demo.automationtesting.in/FileDownload.html")

browser.find_element(By.ID, "textbox").send_keys("Proxima Midnight was Thanos' adoptive daughter and a member of the Black Order. She joined her father in his quest for the six Infinity Stones, initially attacked the Statesman with her brothers and helped to kill the Asgardians aboard and retrieve the Space Stone.")
browser.find_element(By.ID, "createTxt").click()
browser.find_element(By.ID, "link-to-download").click()
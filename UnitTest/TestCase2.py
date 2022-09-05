import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class SearchEngineTest(unittest.TestCase):
    def test_Ookla(self):
        self.s = Service('D:\selenium webdrivers\chromedriver.exe')
        self.browser = webdriver.Chrome(service=self.s)
        self.browser.get("https://www.speedtest.net/")
        print("Title of page is: "+self.browser.title)
        self.browser.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]").click()
        time.sleep(10)
        self.browser.find_element(By.NAME).send_keys()
        self.browser.close()

    def test_Fast(self):
        self.s = Service('D:\selenium webdrivers\chromedriver.exe')
        self.browser = webdriver.Chrome(service=self.s)
        self.browser.get("https://fast.com/")
        print("Title of page is: " + self.browser.title)
        time.sleep(10)
        self.browser.close()

if __name__ == "__main__":
    unittest.main()








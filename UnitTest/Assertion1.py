from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import unittest

class AssertTest(unittest.TestCase):
    def test_Assert(self):
        self.s = Service('D:\selenium webdrivers\chromedriver.exe')
        self.browser = webdriver.Chrome(service=self.s)
        self.browser.get("https://fast.com/")
        title= self.browser.title
        self.assertEqual("Internet Speed Test | Fast.com", title, "Titles are not equal")

if __name__ == "__main__":
    unittest.main()
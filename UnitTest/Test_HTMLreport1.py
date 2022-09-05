import unittest
import HtmlTestRunner

class CaptainAmerica(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("CaptainAmerica villains are: ")

    def test_RedSkull(self):
        print("Red Skull")
        self.assertTrue(True)

    def test_Zemo(self):
        print("Zemo")
        self.assertTrue(True)

    @classmethod
    def tearDownClass(cls):
        print(":) :) :) :)")

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\vivek.s07\\PycharmProjects\\pythonProject\\UnitTest\\Report1'))
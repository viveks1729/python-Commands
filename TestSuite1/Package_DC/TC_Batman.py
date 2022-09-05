import unittest

class Batman_Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Batman villains are: ")

    def test_Bane(self):
        print("Bane")
        self.assertTrue(True)

    def test_Joker(self):
        print("Joker")
        self.assertTrue(True)

    def test_Penguin(self):
        print("Penguin")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
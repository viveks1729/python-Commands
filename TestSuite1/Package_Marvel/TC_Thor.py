import unittest

class Thor_Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Thor villains are: ")

    def test_Loki(self):
        print("Loki")
        self.assertTrue(True)

    def test_Gorr(self):
        print("Gorr")
        self.assertTrue(True)

    def test_Hela(self):
        print("Hela")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
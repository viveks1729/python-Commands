import unittest

class Superman_Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Superman villains are: ")

    def test_LexLuthor(self):
        print("LexLuthor")
        self.assertTrue(True)

    def test_Brainiac(self):
        print("Brainiac")
        self.assertTrue(True)

    def test_Doomsday(self):
        print("Doomsday")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
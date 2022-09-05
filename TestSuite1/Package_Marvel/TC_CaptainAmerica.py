import unittest


class CaptainAmerica_Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("CaptainAmerica villains are: ")

    def test_RedSkull(self):
        print("Red Skull")
        self.assertTrue(True)

    def test_Zemo(self):
        print("Zemo")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
import unittest

def setUpModule():
    print("Set Up Module")

def tearDownModule():
    print("Tear Down Module ")

class TestingOrder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("SetUp Class ")

    @classmethod
    def tearDownClass(cls):
        print("Teardown Class ")

    @classmethod
    def setUp(self):
        print("Setup")

    @classmethod
    def tearDown(self):
        print("Teardown")

    def test_1(self):
        print("-- Test Case 1 --")

    def test_2(self):
        print("-- Test Case 2 --")

if __name__ == "__main__":
    unittest.main()
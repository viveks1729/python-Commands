import unittest

class Skipping(unittest.TestCase):
    @unittest.SkipTest
    def test_1(self):
        print("-- Test Case 1 --")

    @unittest.skip("Skipping with reason message")
    def test_2(self):
        print("-- Test Case 2 --")

    @unittest.skipIf(1==True,"Skipping with condition")
    def test_3(self):
        print("-- Test Case 3 --")

    def test_4(self):
        print("-- Test Case 4 --")
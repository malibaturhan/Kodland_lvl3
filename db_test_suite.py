import unittest
from unittest import TestLoader
import time

class DelayBetweenTests(unittest.TextTestRunner):
    def run(self, test):
        result = super().run(test)
        print("Interval due to conflict")
        time.sleep(0.8)
        return result
    

if __name__ == "__main__":
    suite = unittest.TestSuite()
    TestLoader().discover("tests")
    runner = unittest.TextTestResult()
    runner.run(suite)

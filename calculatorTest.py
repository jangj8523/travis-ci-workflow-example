import unittest
import numpy
from calculator import Calculator

# Please refer to the following link to see more details
# about 'unittest' module:
# https://docs.python.org/3/library/unittest.html


class CalculatorTest(unittest.TestCase):

    def test_add(self):
        x = 1
        y = 1
        testCalculator = Calculator()
        testSum = testCalculator.add(x, y)

        # Test the correctness of your code against the ground truth
        self.assertEqual(testSum, 2)

    def test_subtract(self):
        x = 10
        y = 5
        testCalculator = Calculator()
        testSum = testCalculator.subtract(x, y)
        self.assertEqual(testSum, 5)
    
    def test_multiply(self):
        x = 3
        y = 2
        testCalculator = Calculator()
        testSum = testCalculator.multiply(x, y)
        self.assertEqual(testSum, 6)


if __name__ == '__main__':
    unittest.main()

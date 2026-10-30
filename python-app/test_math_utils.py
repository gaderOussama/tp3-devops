import unittest
import xmlrunner
from math_utils import factorial


class TestFactorial(unittest.TestCase):

    def test_factorial_5(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_0(self):
        self.assertEqual(factorial(0), 1)


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))

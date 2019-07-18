import unittest

from my_script import factorial


class TestFactorial(unittest.TestCase):
    def test_calc_fac(self):
        """
        Test that it can calc factorial
        """
        num = 4
        result = factorial(num)
        self.assertEqual(result, 24)

if __name__ == '__main__':
    unittest.main()

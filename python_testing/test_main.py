import unittest
from main import add, divide


class TestCalc(unittest.TestCase):

    def test_add(self):
        a = 1
        b = 5
        expected_result = 6
        actual_result = add(a, b)
        self.assertEqual(expected_result, actual_result)

    def test_divide(self):
        a = 4
        b = 2
        expected_result = 2
        self.assertEqual(expected_result, divide(a, b))

    def test_divide2(self):
        a = 6
        b = 0
        self.assertRaises(ZeroDivisionError, divide, a, b)

    
            


if __name__ == '__main__':
    unittest.main()



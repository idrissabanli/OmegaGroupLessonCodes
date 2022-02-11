import unittest
from main2 import Calc


class TestCalc(unittest.TestCase):

    def setUp(self):
        a = 4
        b = 2
        self.calc = Calc(a, b)
        print('setUp')

    def test_add(self):
        expected_result = 6
        print('test_add')
        actual_result = self.calc.add()
        self.assertEqual(expected_result, actual_result)

    def test_divide(self):
        print('test_divide')
        expected_result = 2
        self.assertEqual(expected_result, self.calc.divide())

    def tearDown(self):
        print('tearDown')
        del self.calc

    # def test_divide2(self):
    #     a = 6
    #     b = 0
    #     calc = Calc(a, b)
    #     self.assertRaises(ZeroDivisionError, calc.divide)

if __name__ == '__main__':
    unittest.main()



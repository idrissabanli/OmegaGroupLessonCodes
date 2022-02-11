import unittest
from main2 import Calc


class TestCalc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        a = 4
        b = 2
        cls.calc = Calc(a, b)

        cls.calc2 = Calc(4, 0)
        print('setUpClass')

    def test_add(self):
        expected_result = 6
        print('test_add')
        actual_result = self.calc.add()
        self.assertEqual(expected_result, actual_result)

    def test_divide(self):
        print('test_divide')
        expected_result = 2
        self.assertEqual(expected_result, self.calc.divide())
    
    def test_divide_by_zero(self):
        print('test_divide_by_zero')
        self.assertRaises(ZeroDivisionError, self.calc2.divide)

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')
        del cls.calc



if __name__ == '__main__':
    unittest.main()




import unittest


def addition(self, first_num, second_num):
    return first_num + second_num


class TestSuite(unittest.TestCase):

    def test_addition_pass_return_values_set1(self):
        self.assertEqual(addition(self, 2, 2), 4)

    def test_addition_pass_return_values_set2(self):
        self.assertEqual(addition(self, 12, 7), 19)

    def test_addition_pass_return_values(self):
        self.assertRaises(TypeError, addition, self, "not a number", 2)


if __name__ == '__main__':
    unittest.main()
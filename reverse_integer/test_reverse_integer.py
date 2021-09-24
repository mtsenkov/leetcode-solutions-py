import unittest

from solution import Solution

sol = Solution()

class TestReverseInteger(unittest.TestCase):
    def test_reverse_integer_positive(self):
        x = 123
        result = sol.reverse(x)
        self.assertEqual(result, 321)

    def test_reverse_integer_negative(self):
        x = -123
        result = sol.reverse(x)
        self.assertEqual(result, -321)

    def test_reverse_integer_contains_zero(self):
        x = 120
        result = sol.reverse(x)
        self.assertEqual(result, 21)

    def test_reverse_integer_zero(self):
        x = 0
        result = sol.reverse(x)
        self.assertEqual(result, 0)

    def test_reverse_integer_upper_constraint(self):
        x = 1534236469
        result = sol.reverse(x)
        self.assertEqual(result, 0)

    def test_reverse_integer_lower_constraint(self):
        x = -2147483648
        result = sol.reverse(x)
        self.assertEqual(result, 0)

    def test_reverse_integer_big_number(self):
        x = 1463847412
        result = sol.reverse(x)
        self.assertEqual(result, 2147483641)

if __name__ == "__main__":
    unittest.main()

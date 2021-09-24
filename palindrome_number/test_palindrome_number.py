import unittest

from solution import Solution

pn = Solution()

class TestPalindromeNumber(unittest.TestCase):

    def test_is_palindrome(self):
        num = 121
        result = pn.isPalindrome(num)
        self.assertTrue(result)

    def test_is_not_palindrome_negative(self):
        num = -121
        result = pn.isPalindrome(num)
        self.assertFalse(result, False)

    def test_is_not_palindrome(self):
        num = 10
        result = pn.isPalindrome(num)
        self.assertFalse(result, False)
    
    def test_is_not_palindrome_negative2(self):
        num = -101
        result = pn.isPalindrome(num)
        self.assertFalse(result, False)

if __name__ == '__main__':
    unittest.main()

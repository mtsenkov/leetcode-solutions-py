class Solution:
    def isPalindrome(self, x: int) -> bool:
        return True if str(x)[::-1] == str(x)[::] else False
        
    def isPalindrome_another_solution(self, x: int) -> bool:
        s = str(x)
        l = len(s)-1
        for c in range(l+1):
            if s[c] != s[l]:
                return False
            l -= 1
        return True
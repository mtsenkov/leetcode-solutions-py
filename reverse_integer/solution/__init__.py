class Solution:
    def reverse(self, x: int) -> int:
        result = str(x)[::-1]
        num = 0
        if "-" in result:
            result = result.replace("-","")
            num = int(result)*-1
        else:
            num = int(result)
        return 0 if num <= (2**31)*-1 or num >= 2**31-1 else num
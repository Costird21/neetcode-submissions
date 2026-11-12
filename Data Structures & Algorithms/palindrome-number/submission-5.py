class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)[::-1]
        y = int(y)
        if x != y:
            return False
        return True
class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)[::-1]
        if x != y:
            return False
        return True
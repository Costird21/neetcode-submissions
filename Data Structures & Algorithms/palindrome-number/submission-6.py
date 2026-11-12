class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = int(str(x)[::-1])
        if x != y:
            return False
        return True
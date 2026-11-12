class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = int(str(x)[::-1])
        if x != rev:
            return False
        return True
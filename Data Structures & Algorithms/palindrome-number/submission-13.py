class Solution:
    def isPalindrome(self, x: int) -> bool:

        rev = int(str(x)[::-1].split("-"))
        if x < 0:
            rev -= rev*2
        if x != rev:
            return False
        return True
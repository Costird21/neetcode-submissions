class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        if x < 0:
            x += x*2
            rev = int(str(x)[::-1])
            rev -= rev*2
        else:
            rev = int(str(x)[::-1])
            
        if x != rev:
            return False
        return True
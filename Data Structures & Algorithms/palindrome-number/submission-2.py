class Solution:
    def isPalindrome(self, x: int) -> bool:
        x.sort()
        x_reversed = x.sort(reverse=True)
        if x != x_reversed:
            return False
        return True
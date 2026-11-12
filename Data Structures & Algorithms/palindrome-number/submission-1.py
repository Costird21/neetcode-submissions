class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_sorted = x.sort()
        x_reversed = x.sort(reverse=True)
        if x_sorted != x_reversed:
            return False
        return True
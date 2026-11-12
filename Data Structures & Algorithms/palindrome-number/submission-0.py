class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x.sort() != x.sort(reverse=True):
            return False
        return True
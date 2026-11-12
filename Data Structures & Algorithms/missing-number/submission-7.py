class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        nums.sort()
        for n in nums:
            if n != i:
                return i
            elif n+1 not in nums:
                return n+1
            else:
                i += 1
                
        return -1
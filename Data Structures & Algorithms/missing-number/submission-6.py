class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        nums.sort()
        for n in nums:
            if n != i:
                return i
            else:
                i += 1
        return -1
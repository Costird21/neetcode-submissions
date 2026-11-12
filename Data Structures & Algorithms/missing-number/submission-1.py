class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0;
        for n in nums:
            if n != nums[i]:
                return n
            i += 1
        return 0
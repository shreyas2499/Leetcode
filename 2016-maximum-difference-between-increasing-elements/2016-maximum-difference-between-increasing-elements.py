class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        l = 0
        r = 1
        maxDiff = -1
        
        while r<len(nums):
            if(nums[l]<nums[r]):
                maxDiff = max(maxDiff, nums[r]-nums[l])
                r = r + 1
            else:
                l = r
                r = r + 1
        return maxDiff
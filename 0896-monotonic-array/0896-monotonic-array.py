class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        l, r = 0, 1
        
        if(nums[-1]-nums[0] < 0):
            nums.reverse()
        
        while r<len(nums):
            if not nums[l] <= nums[r]:
                return False
            l = l + 1
            r = r + 1
        return True
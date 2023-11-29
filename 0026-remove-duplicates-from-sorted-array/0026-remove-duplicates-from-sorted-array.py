class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 1
        
        while(l<len(nums) and r<len(nums)):
            if(nums[r] == nums[l]):
                nums.remove(nums[r])
                
            else:
                r = r+1
                l = l + 1
        
        return len(nums)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        # for i in range(len(nums)):
        #     if(val in nums):
            
        return len(nums)
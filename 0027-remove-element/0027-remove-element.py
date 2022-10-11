class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # for i in range(len(nums)):
        #     if(nums[i] == val):
        #         nums.replace(nums[i],"_")
        test = []
        
        for i in range(len(nums)):
            if(val in nums):
                nums.remove(val)
        
        # for i in nums:
        #     if(i==val):
        #         # nums[index(i)]="_"
        #         nums.remove(i)
        #         # if(i<len(nums)-1):
        #         #     nums[i] = nums[i+1]
        #         # nums.pop(index(nums[i]))
        # nums.remove(val)
        
        return len(nums)
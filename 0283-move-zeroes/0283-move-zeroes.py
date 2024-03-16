class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums = nums.sort()
        # print(nums[0])
        
        writer = 0
        
        for reader in range(len(nums)):
            if(nums[reader]!=0):
                nums[writer] = nums[reader]
                writer+=1
                
        while(writer < len(nums)):
            nums[writer]=0
            writer += 1
            
        return nums
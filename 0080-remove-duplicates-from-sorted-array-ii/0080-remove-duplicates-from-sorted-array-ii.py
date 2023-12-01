class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # values = collections.Counter(nums)
        
        l=0
        r=1
        
        count = 0
        while(r<len(nums)):
            if(nums[l]==nums[r]):
                count = count + 1
                if(count>1):
                    nums.remove(nums[r])
                    r = r - 1
                r = r + 1
                
            else:
                
                l = r
                r = r + 1
                count = 0
                
        
        # print(values)
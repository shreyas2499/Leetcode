class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        
        count={}
        res = 0
        
        for r in range(len(nums)):
            count[nums[r]] = count.get(nums[r], 0) + 1
            # if(((r-l+1) - count.get(1, 0) > k)):
            while(count.get(0, 0) > k):
                count[nums[l]] -= 1
                l = l + 1
            
            res = max(res, r-l+1)
        return res
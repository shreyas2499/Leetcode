class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dupHash = {}
        
        for i in nums:
            if i in dupHash:
                return i
            else:
                dupHash[i] = 1
         
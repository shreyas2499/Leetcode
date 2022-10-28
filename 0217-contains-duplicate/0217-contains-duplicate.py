class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
#         nums = nums[::-1]
#         for i in range(len(nums)-1):
#             if(nums[i] in nums[i+1:]):
#                 return True
#         return False
        
        return ( len(list(set(nums))) != len(nums))
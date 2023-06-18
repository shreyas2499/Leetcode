class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         Pointer approach
        l, r = 0, len(numbers)-1
    
        while(l<=r):
            if(numbers[l]+numbers[r] > target):
                r = r - 1
            if(numbers[l]+numbers[r] < target):
                l = l + 1
            if(numbers[l]+numbers[r] == target):
                return [l+1,r+1]
        return []
        
        
    
#         Brute force approach
#         dummy = target
#         nums = numbers
#         ad = []
#         for i in list(set(nums)):
#             print(i, nums.index(i))
#             ad.append(nums.index(i)+1)
#             dummy = dummy - i

#             nums[nums.index(i)] = ''
#             if(dummy in list(set(nums))):
#                 ad.append(nums.index(dummy)+1)
#                 return sorted(ad)
#             else:
#                 ad = []
#                 dummy = target
#         return sorted(ad)
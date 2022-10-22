class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dummy = target
        ad = []
        for i in nums:
            ad.append(nums.index(i))
            dummy = dummy - i
            # print(dummy)
            nums[nums.index(i)] = ''
            # print(nums)
            if(dummy in nums):
                ad.append(nums.index(dummy))
                # print(ad)
                return ad
            else:
                ad = []
                dummy = target
        return ad
            
#         sum = 0
#         ad = []
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 sum = nums[i]+nums[j]
#                 if(sum == target):
#                     ad.append(nums.index(nums[i]))
#                     ad.append(nums.index(nums[j]))
#         return ad
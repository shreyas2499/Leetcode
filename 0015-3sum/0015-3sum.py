class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sums = []
        nums = sorted(nums)
        # print(nums)
        for i, a in enumerate(nums):
            if(i>0 and nums[i-1] == a):
                continue
            else:
                init = nums[i] # -1
                l = i+1
                r = len(nums)-1
                while(l<r):
                    midSum = init+nums[l]+nums[r]
                    if(midSum>0):
                        r = r-1
                    elif(midSum < 0):
                        l = l+1
                    else:
                        sums.append([init, nums[l], nums[r]])
                        l = l + 1
                        while(nums[l] == nums[l-1] and l<r):
                            l = l+1
        return sums            
#         finalSum = []
#         for i in sums:
#             if(i not in finalSum):
#                 finalSum.append(i)
#         return finalSum
            
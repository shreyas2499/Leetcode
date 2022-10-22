class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dummy = target
        ad = []
        for i in nums:
            ad.append(nums.index(i))
            dummy = dummy - i
            nums[nums.index(i)] = ''
            if(dummy in nums):
                ad.append(nums.index(dummy))
                return ad
            else:
                ad = []
                dummy = target
        return ad
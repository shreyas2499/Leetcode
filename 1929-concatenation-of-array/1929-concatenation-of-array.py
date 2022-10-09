class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums2=nums
        for i in range(len(nums)):
            nums2 = nums.append(nums[i])
        return nums
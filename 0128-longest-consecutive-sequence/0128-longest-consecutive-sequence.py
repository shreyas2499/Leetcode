class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortedNums = set(nums)
        longest = 0
        
        for n in nums:
            if (n-1) not in sortedNums:
                length = 0
                while (n+length) in sortedNums:
                    length = length + 1
                longest = max(length, longest)
        return longest
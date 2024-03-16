class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        ans = {}
        for i, val in enumerate(nums):
            if val in ans:
                ans[val].append(i)
            else:
                ans[val] = [i]
                
        for i, j in ans.items():
            for idx, k in enumerate(j):
                for new in range(idx+1, len(j)):
                    count = count + 1
        return count
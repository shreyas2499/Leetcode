class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        arr = []
        maxS = 0
        while r<len(s):
            if(s[r] not in arr):
                arr.append(s[r])
                maxS = max(maxS, len(arr))
                r = r + 1
            else:
                arr = []
                l = l + 1
                r = l
        print(arr)
        print(maxS)
        return maxS
        
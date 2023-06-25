class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        count = {}
        res = 0
        
        for r in range(len(s)):
            
#             To get count of each value in the window
            count[s[r]] = 1 + count.get(s[r], 0)
            if ((r-l+1)-max(count.values()) > k):
                count[s[l]] = count[s[l]] - 1
                l = l + 1
                                
            res = max(res, r - l + 1)
        return res
            
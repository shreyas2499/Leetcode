class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = ""
        
        for i in range(len(strs[0])):
#             flower looping
            for s in strs:
#                 all str looping
                if(i >= len(s) or s[i] != strs[0][i] ):
                    return res
            res = res + strs[0][i]
            
        return res
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        
        for i in range(len(s) -1, -1, -1):
            for w in wordDict:
                if(i+len(w) <= len(s) and s[i:i+len(w)] == w):
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]
        
        
        # for word in wordDict:
        #     if word in s:
        #         ind1 = s.index(word[0])
        #         ind2 = s.index(word[-1])
        #         newS = s[:ind1]+s[ind2:] 
        #         s = newS
        #         continue
        #     else:
        #         return False
        # return True
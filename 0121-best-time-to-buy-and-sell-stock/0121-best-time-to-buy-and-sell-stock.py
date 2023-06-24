class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        res = []
        while r<len(prices):
            print(l,r)
            if(prices[l]<prices[r]):
                res.append(prices[r]-prices[l])
                r = r + 1
                
            else:
                l = r
                r = r + 1
        
        if(len(res)>0):
            return max(res)
        else:
            return 0
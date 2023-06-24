class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 1
        maxP = 0
        
        while (r<len(prices)):
            if(prices[l]<prices[r]):
                maxP =maxP + (prices[r]-prices[l])
                l = l + 1
            else:
                l = l + 1
            r = r + 1
        print(maxP)
        
        return maxP
                
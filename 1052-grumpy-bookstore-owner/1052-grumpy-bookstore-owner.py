class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        
        happyCust = 0
        
        l = 0
        window = 0
        maxWindow = 0
        satisfied = 0
        for r in range(len(customers)):
            if grumpy[r]:
                window += customers[r]
            else:
                
                satisfied += customers[r]
            
            if r-l+1 > minutes:
                if grumpy[l]:
                    window -= customers[l]
                l += 1
            
            maxWindow = max(window, maxWindow)
            
        return satisfied + maxWindow
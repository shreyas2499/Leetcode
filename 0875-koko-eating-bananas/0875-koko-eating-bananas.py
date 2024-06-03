class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        """
        The rates of the K can be anything from 1 till the max value in the piles list. 
        So what we do is, take two pointers and use binary search to get the most optimal K value
        We take math.ceil because all the rates of eating need to be rounded up
        """
        
        l, r = 1, max(piles)
        res = r
        
        while(l<=r):
            k = (l+r)//2
            hours = 0
            for i in piles:
                hours = hours + math.ceil(i/k)
            
            if(hours<=h):
                res = min(res, k) 
                r = k - 1
            elif(hours > h):
                l = k + 1
                
        return res
        
        
        
        
        
        
#         TimeOut Error
#         speed = 1
#         while True:
#             s = 0
#             for i in piles:    
#                 s = s + math.ceil(i/speed)
            
#             if(s<=h):
#                 return speed
#             else:
#                 speed += 1
        
        
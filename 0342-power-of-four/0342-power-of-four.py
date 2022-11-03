class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if(n==1):
            return True
        i=0
        while(4**i<=n):
            i=i+1
            if(4**i == n):
                return True
            
        return False
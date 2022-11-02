class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if(n==1):
            return True
        sum=0
        i=0
        while(2**i<=n):
            i=i+1
            if(2**i == n):
                return True
            
        return False
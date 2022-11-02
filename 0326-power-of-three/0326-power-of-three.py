class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if(n==1):
            return True
        i=0
        while(3**i<=n):
            i=i+1
            if(3**i == n):
                return True
            
        return False
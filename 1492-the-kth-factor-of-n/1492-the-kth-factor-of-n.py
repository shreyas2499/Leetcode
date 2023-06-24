class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        fact = []
        for i in range(1, n+1):
            if(n%i == 0):
                fact.append(i)
                if(len(fact) == k):
                    break
                
        try:
            fac = fact[k-1]
            return fac
        except:
            return -1
                
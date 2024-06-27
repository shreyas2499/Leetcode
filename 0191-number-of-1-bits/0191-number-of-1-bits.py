class Solution:
    def hammingWeight(self, n: int) -> int:
        
        temp = n
        a = ""
        while(temp!=0):
            a = a + str(temp%2)
            temp = temp//2
        
        
        return a.count("1")
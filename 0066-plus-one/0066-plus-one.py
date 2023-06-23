class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # s = ''
        n = 0
        for i in digits:
            n = n*10 + i
        
        # n = int(s)
        n = n + 1
        b = str(n)
        c = list(b)
        for i in range(len(c)):
            c[i] = int(c[i])
        return c
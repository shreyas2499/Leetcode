class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # s = ''
        n = 0
        for i in digits:
            n = n*10 + i
        
        # n = int(s)
        n = n + 1
        b = str(n)
        return list(b)
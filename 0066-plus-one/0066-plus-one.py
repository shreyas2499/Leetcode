class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        for i in digits:
            s = s + str(i)
        
        n = int(s)
        n = n + 1
        b = str(n)
        return list(b)
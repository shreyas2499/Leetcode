class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if(len(s)!=len(t)):
            return False
        
        s = sorted(list(s))
        t = sorted(list(t))
        
        for i, val in enumerate(s):
            if(t[i]!=val):
                return False
        return True
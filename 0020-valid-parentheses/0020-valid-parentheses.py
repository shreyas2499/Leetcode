class Solution:
    def isValid(self, s: str) -> bool:
        
        invalid = [")", "}", "]"]
        valid = ["(", "{", "["]
        
        if(len(s)%2 != 0):
            return False
        
        if(s[0] in invalid):
            return False
        
        stack = []
        
        for c in s:
            if c in valid:
                stack.append(c)
            elif c in invalid:
                try:
                    ele = stack.pop()
                    if(ele == valid[invalid.index(c)]):
                        continue
                    else:
                        return False
                except: 
                    return False
        
        if(len(stack)>0):
            return False
        
        return True
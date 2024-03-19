class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        res = 0
        for i in tokens:
            if(i in ["+", "-", "/", "*"]):
                a = stack.pop()
                b = stack.pop()
                
                if(i == "+"):
                    res = int(b) + int(a)
                if(i == "-"):
                    res = int(b) - int(a)
                if(i == "/"):
                    res = int(b) / int(a)
                if(i == "*"):
                    res = int(b) * int(a)
            
                stack.append(res)
            else:
                stack.append(i)
        
        return int(stack[0])
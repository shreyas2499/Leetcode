class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ans = []
        count=0
        while(digit in number and count<len(number)):    
            n = number.replace(digit, '',1)
            number = number.replace(digit,'X',1)
            count = count+1
            # number = n 
            ans.append(n)
        return check(ans, digit)
    
def check(ans: list, digit: str):
    b = []
    for i in ans:
        b.append(i.replace('X', digit))
    
    return max(b)
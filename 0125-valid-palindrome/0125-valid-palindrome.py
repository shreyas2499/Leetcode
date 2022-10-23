class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = ''
        for i in s:
            
            if i.isalnum():
                # print(i)
                l = l + i
        print(l)
        
        return (l.lower() == l.lower()[::-1])
class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        print(str(x))
        
        z = str(x)[::-1]
        print(z==y)
        return (y==z)
        # if(y == z):
        #     print('true')
        # else:
        #     return 'false'
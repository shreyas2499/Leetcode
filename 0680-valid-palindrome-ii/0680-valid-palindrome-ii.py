class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        
        skip = 1
        
        while l<=r:
            if(s[l] == s[r]):
                l+=1
                r-=1
            else:
                if(skip == 1):
                    # print(s[l+1: r])
                    # print(s[l+1: r][::-1])
                    # print(s[l])
                    # print(s[r])
                    # print(s[l:r-1])
                    # print(s[l:r-1][::-1])
                    if(s[l+1: r+1] == s[l+1: r+1][::-1]):
                        l+=1
                        skip = 0
                    elif(s[l:r-1+1] == s[l:r-1+1][::-1]):
                        r-=1
                        skip = 0
                    else:
                        return False
                else:
                    return False
                        
        return True
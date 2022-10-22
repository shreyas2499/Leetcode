class Solution:
    def repeatedCharacter(self, s: str) -> str:
        ad=[]
        for i in s:
            if i not in ad:
                ad.append(i)
                print(ad)
            else:
                return i
            
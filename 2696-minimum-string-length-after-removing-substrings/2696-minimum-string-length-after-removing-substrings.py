class Solution:
    def minLength(self, s: str) -> int:
        for i in range(len(s)):
            print(i,"AB" in s)
            print(i, "CD" in s)
            if("AB" in s):
                s = s.replace("AB", "")
            elif("CD" in s):
                s = s.replace("CD", "")
            else:
                break

        print(s)
        print(len(s))
        return len(s)
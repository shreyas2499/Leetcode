class Solution:
    def minLength(self, s: str) -> int:
        for i in range(len(s)):
            if("AB" in s):
                s = s.replace("AB", "")
            elif("CD" in s):
                s = s.replace("CD", "")
            else:
                break

        return len(s)
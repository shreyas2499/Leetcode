class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        data = s.split(" ")
        for i in range(len(data)):
            data[i] = data[i].strip()
        
        return len(data[-1])
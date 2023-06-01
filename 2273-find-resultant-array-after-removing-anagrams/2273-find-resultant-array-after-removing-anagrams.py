class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = []
        ans.append(words[0])
        for i in range(1, len(words)):
            res = self.anagram(words[i-1],words[i])
            if(not res):
                ans.append(words[i])
                
        return ans

    def anagram(self, s1: str, s2: str):
        if(sorted(s1) == sorted(s2)):
            return True
        else:
            return False
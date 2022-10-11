class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        words = []
        for i in sentences:
            words.append(len(i.split(" ")))
            
        return max(words)
class Solution:
    def frequencySort(self, s: str) -> str:
        freqDict = {}
        
        for c in s:
            if c in freqDict:
                freqDict[c] += 1
            else:
                freqDict[c] = 1
                
        
        result = ""
        newFreqDict = dict(sorted(freqDict.items(), key=lambda item: item[1], reverse=True))
        
        for key in newFreqDict.keys():
            result = result + (key)*newFreqDict[key]
            
    
        print(result)
        
        return result
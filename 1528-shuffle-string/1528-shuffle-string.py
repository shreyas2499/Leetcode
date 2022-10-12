class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dict = {}
        for i in range(len(indices)):
            dict[indices[i]] = s[i]
        l = [0]*len(indices)
        print(dict)
        for i in dict.keys():
            l[i] = dict[i]
        ans = ''
        for i in l:
            ans = ans+i
            
        print(l)
        return ans
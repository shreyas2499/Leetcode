class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = {}
        for i in nums:
            if i in dict.keys():
                dict[i]=dict[i]+1
            else:
                dict[i]=1
        for i in dict.keys():
            if(dict[i] == 1):
                return i                
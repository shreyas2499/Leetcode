class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict={}
        for i in nums:
            if i not in dict.keys():
                dict[i]=1
            else:
                dict[i]=dict[i]+1
        print(max(dict))
        for i in dict.keys():
            print(dict[i],'asdad')
            if(dict[i]>len(nums)/2):
                return i
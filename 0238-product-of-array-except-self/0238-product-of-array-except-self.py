class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodList = []
        pre = 1
        post = 1
        for i in range(len(nums)):
            prodList.append(pre)
            pre = pre * nums[i]
        for j in range(len(nums)-1,-1, -1):
            prodList[j] = prodList[j]*post
            post = post * nums[j]
        
        return prodList
        
        
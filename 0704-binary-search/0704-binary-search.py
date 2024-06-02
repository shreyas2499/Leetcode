class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        mid = int((low+high)/2)
        
        while (low <= high):
            if(nums[mid] > target):
                high = mid - 1
                mid = int((low+high)/2)
            elif(nums[mid] < target):
                low = mid + 1
                mid = int((low+high)/2)
            else:
                return mid
        return -1
            
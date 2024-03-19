class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        for i in nums2:
            nums1.append(i)
            
        nums1 = sorted(nums1)
        
        m = (len(nums1)-1)/2
        
        return (nums1[math.ceil(m)] + nums1[math.floor(m)])/2
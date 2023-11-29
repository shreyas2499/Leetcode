class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1 = nums1[:m]
        # print(nums1)
        # nums1.append(nums2)
        for i in range(n):
            # nums1.append(i)
            nums1[i+m] = nums2[i]
        # print(nums1)
        nums1.sort()
        # print(nums1)
        # return nums1
        a= 0


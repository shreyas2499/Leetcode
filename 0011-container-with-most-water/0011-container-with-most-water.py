class Solution:
    def maxArea(self, height: List[int]) -> int:
#         I need second heightest index - heightest index for width
#         I need second heightest index
        
        l = 0
        r = len(height) - 1
        area = []
        while l<r:
            # print(height[l], height[r])
            area.append((r - l) * min(height[l], height[r]))
            if(height[l]<height[r]):
                l = l + 1
            elif(height[l]>height[r]):
                r = r - 1
            elif(height[l]==height[r]):
                l = l + 1
        print(area)
        return max(area)
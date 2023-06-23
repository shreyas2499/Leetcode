class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height: return 0
        l = 0
        r = len(height) - 1
        maxL, maxR = height[l], height[r]
        res = 0
        
        while l<r:
            if(maxL <= maxR):
                l = l + 1
                maxL = max(maxL, height[l])
                if(maxL-height[l]>0):
                    res = res + (maxL-height[l])
            else:
                r = r - 1 
                maxR = max(maxR, height[r])
                if(maxR-height[r]>0):
                    res = res + (maxR-height[r])
                    
        return res
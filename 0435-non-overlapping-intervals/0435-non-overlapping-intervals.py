class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
#         intervals = sorted(intervals, key=lambda x: x[0])
#         print(intervals)
#         rem = []
        
#         l = 0
#         r = 1

#         while(l<len(intervals) and r<len(intervals)):
#             if(intervals[l][1] <= intervals[r][0]):
#                 l += 1
#                 r += 1
#                 continue
#             else:
#                 rem.append(intervals[l])
#                 r += 1
                
                
#         return len(rem)
    
    
        intervals.sort(key = lambda x: x[1])
        ans = 0
        k = -inf
        
        for x, y in intervals:
            if x >= k:
                # Case 1
                k = y
            else:
                # Case 2
                ans += 1
        
        return ans
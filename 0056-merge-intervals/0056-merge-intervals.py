class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        l = 0
        r = 1
        intervals = sorted(intervals, key=lambda x: x[0])
        newIntervals = [intervals[0]]
        
        for start, end in intervals[1:]:
            lastEnd = newIntervals[-1][1]
            
            if(start <= lastEnd):
                newIntervals[-1][1] = max(newIntervals[-1][1], end)
                
            else:
                newIntervals.append([start, end])
                
        
        # while(l<len(intervals) and r<len(intervals)):
        #     if(intervals[l][1]>=intervals[r][0]):
        #         if(intervals[l][0] <= intervals[r][0]):
        #             intervals[0] = [intervals[l][0], intervals[r][1]]
        #         else:
        #             intervals[0] = [intervals[l][0], intervals[l][1]]
        #         del intervals[1]
        #         # newIntervals.append([intervals[l][0], intervals[r][1]])
        #         # r = r + 1
        #     else:
        #         # newIntervals.append(intervals[r])
        #         l = l + 1
        #         r = r + 1
                
        return newIntervals
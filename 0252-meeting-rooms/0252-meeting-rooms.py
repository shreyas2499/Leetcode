class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        meeting = True
        
        intervals = sorted(intervals, key=lambda x: x[0])
        
        # for i, val in enumerate(intervals):
        #     sub = intervals[0]
        #     if i==0:
        #         continue
            
            # if(sub[0] > val[0])
            
        print(intervals)
        
        if len(intervals)==0:
            return True
        elif(len(intervals) == 1):
            return True
        else:
            l = 0
            r = 1
            
            while(l<len(intervals) and r<len(intervals)):
                if(intervals[l][1]<= intervals[r][0]):
                    l += 1
                    r += 1
                    continue
                else:
                    return False
                
        return True
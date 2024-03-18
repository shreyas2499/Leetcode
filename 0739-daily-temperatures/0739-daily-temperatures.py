class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        
#         for i in range(len(temperatures)):
#             for j in range(i+1, len(temperatures)):
#                 if(res[i]==0):
#                     if(temperatures[j]>temperatures[i]):
#                         res[i] = j - i
#                     else:
#                         continue
        
#         return res


        stack = []
        
        for i, t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                val, idx = stack.pop()
                res[idx] = i - idx
            
            stack.append([t, i])
        
        return res

        
                
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        
        """
            Create a pair of position, speed for each car. 
            We sort the pair and traverse it in decreasing order.
            Calculate the time it would take to reach the target. and append this time to the stack
            
            Compare the top 2 values in the stack and if the top < less than top[-2], then pop that value. 
            The popping indicates that these two values are now a fleet
            
            In the end return the length of the stack
        """
        
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []
        
        
        for p, s in sorted(pair)[::-1]:
            stack.append((target-p)/s)
            
            if (len(stack)>=2 and stack[-1] <= stack[-2]):
                stack.pop()
        
        return len(stack)
        
        
#         dicti = {}
        
#         for i, val in enumerate(position):
            
#             if(val+speed[i] in dicti):
#                 dicti[val+speed[i]]+=1
#             else:
#                 dicti[val+speed[i]] = 1
           
#         count = 0
#         for i in dicti.keys():
#             count+=1
        
#         return count
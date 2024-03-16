class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        a = {}
        
        for i, val in enumerate(nums):
            if val in a.keys():
                a[val].append(i)
            else:
                a[val] = [i]
                
                
        for key in a.keys():
            if(len(a[key])>=2):
                for i in range(len(a[key])):
                    for j in range(i+1, len(a[key])):
                    
                        if(abs(a[key][i]-a[key][j]) <= k):
                            return True
                
        return False
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dummy = target
        nums = numbers
        ad = []
        # nums = []
        # for i in numbers:
            
                # nums.append(i)
        
        # print(set(nums))
        abcd = nums
        for i in list(set(nums)):
            # if(i<=target):
            print(i, nums.index(i))
            ad.append(nums.index(i)+1)
            dummy = dummy - i

            nums[nums.index(i)] = ''
            if(dummy in list(set(nums))):
                ad.append(nums.index(dummy)+1)
                return sorted(ad)
            else:
                ad = []
                dummy = target
        return sorted(ad)
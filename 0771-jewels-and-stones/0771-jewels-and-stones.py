class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewl = [*jewels]
        count = 0
        for i in [*stones]:
            if i in jewl:
                count += 1
                
        return count
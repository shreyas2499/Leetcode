class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        sum = 0
        for i in operations:
            match i:
                case '++X': sum = sum + 1
                            
                case 'X++': sum = sum + 1                            
                            
                case 'X--': sum = sum - 1
                            
                case '--X': sum = sum - 1
                            
        
        return sum
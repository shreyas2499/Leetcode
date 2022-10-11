class Solution:
    def romanToInt(self, s: str) -> int:
        lst = []
        
        for letter in s:
            lst.append(letter)
        sum = 0
        for i in lst:
            sum = sum + convertion(i)
    
        print(sum, '1')
        for i in range(len(lst)-1):
            if(lst[i] == 'I' and lst[i+1]=='V'):
                sum = sum - 2
            elif(lst[i] == 'I' and lst[i+1]=='X'):
                sum = sum - 2
            elif(lst[i] == 'X' and lst[i+1]=='L'):
                sum = sum - 20
            elif(lst[i] == 'X' and lst[i+1]=='C'):
                sum = sum - 20
            elif(lst[i] == 'C' and lst[i+1]=='D'):
                sum = sum - 200
            elif(lst[i] == 'C' and lst[i+1]=='M'):
                sum = sum - 200       
        print(sum, '2')
        return sum
    
def convertion(s:str):
    match s:
        case 'I': return 1
        case 'V': return 5
        case 'X': return 10
        case 'L': return 50
        case 'C': return 100
        case 'D': return 500
        case 'M': return 1000
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if(n>0):
#             if(n>200000):
                
            x = x
        elif(n<0 and x!=1 and x!=-1):
            if(n<-200000):
                return 0
            x = 1/x
        elif(n==0):
            return 1
        
        sum = 1.00
        # print(sum * x)
        if(x<0.0001 and x> -0.0001):
            return 0
        elif(x == 1):
            return 1
        elif(x == -1):
            if(n%2 == 0):
                return 1
            else:
                return -1
                
                
        for i in range(1,abs(n)+1):
            # print(i)
            # sum = round(sum,2)
            sum = sum * x
            # sum = round(sum,2)
            # print(sum,"inside")
        return sum
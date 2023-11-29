# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """


        num = head.val
        while(head.next):
            num = num*2 + head.next.val
            head = head.next

        return num
#         stri = ""
#         node = head
#         while(node.next!=None):
#             stri = stri + str(node.val)
#             node = node.next
        
#         stri = stri + str(node.val)
        
#         decimal = 0 
#         i=0
#         stri = int(stri)
#         while(stri != 0):
#             dec = stri % 10
#             decimal = decimal + dec* pow(2, i)
#             stri = stri//10
#             i = i +1
            
#         return decimal
    
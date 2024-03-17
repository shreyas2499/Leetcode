# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        while(head.next!=None):
            vals.append(head.val)
            head = head.next
            if(head.next == None):
                vals.append(head.val)
            

        return vals == vals[::-1]

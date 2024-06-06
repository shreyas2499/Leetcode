# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        dummy = ListNode()
        dummy = head
        
        
        while dummy:
            if("v" in str(dummy.val)):
                return True
            
            dummy.val = str(dummy.val)+'v'
            dummy = dummy.next
            
        return False
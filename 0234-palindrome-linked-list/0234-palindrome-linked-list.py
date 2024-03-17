# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ans = ""
        
        while(head.next!=None):
            ans += str(head.val)
            head = head.next
            if(head.next == None):
                ans += str(head.val)
            
        
        print(ans)
        return ans == ans[::-1]

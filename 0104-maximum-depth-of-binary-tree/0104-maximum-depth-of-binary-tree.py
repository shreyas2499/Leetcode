# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
                
        
        
#         depth = 0
        
#         if not root:
#             return None
        
#         if(root.left):
#             depth += 1   
#             self.maxDepth(root.left)
#         else:
#             depth+=1
#             self.maxDepth(root.right)
    
#         return depth
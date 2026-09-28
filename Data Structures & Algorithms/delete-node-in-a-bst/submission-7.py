# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def findNode(key, root, parent):
            if not root:
                return [None, parent]
            
            if key == root.val:
                return [root, parent]
            
            if key < root.val:
                return findNode(key, root.left, root)
            else:
                return findNode(key, root.right, root)
        
        node,parent = findNode(key, root, None)

        if not node:
            return root



            
        
        if not node.left or not node.right:
            child = node.left if node.left else node.right

            if not parent:
                return child
            
            if parent.left == node:
                parent.left = child
            else:
                parent.right = child
        
        else:
            rightSub = node.right
            leftSub = node.left

            cur = rightSub
            while cur.left:
                cur = cur.left
            cur.left = leftSub

            if not parent:
                return rightSub
            
            if parent.left == node:
                parent.left = rightSub
            else:
                parent.right = rightSub
        
        return root
        
            



        

        
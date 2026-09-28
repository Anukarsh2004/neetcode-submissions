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

        if node == root:
            if node.right:
                tmp = node.left
                root, node = node.right, node.right
                while node.left:
                    node = node.left
                node.left = tmp
            elif node.left:
                tmp = node.right
                root, node = node.left, node.left
                while node.right:
                    node = node.right
                node.right = tmp
            else:
                root = None
            return root


            
        
        if not node.left and not node.right:
            if parent.val > node.val:
                parent.left = None
            else:
                parent.right = None
        
        elif not node.left:
            if parent.val > node.val:
                parent.left = node.right
            else:
                parent.right= node.right
        elif not node.right:
            if parent.val > node.val:
                parent.left = node.left
            else:
                parent.right = node.left
        
        else:
            if parent.val > node.val:
                parent.left = node.right
                tmp = node.left
                node = node.right
                while node.left:
                    node = node.left
                node.left = tmp
            
            else:
                parent.right = node.right
                tmp = node.left
                node = node.right
                while node.left:
                    node = node.left
                node.left = tmp
        
        return root



        

        
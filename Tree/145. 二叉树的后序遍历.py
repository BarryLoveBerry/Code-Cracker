# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # res = []
        # def backorder (root):
        #     if not root:
        #         return
        #     backorder(root.left)
        #     backorder(root.right)
        #     res.append(root.val) 
            
        # backorder(root)
        # return res 
 #  迭代
        ans = []
        if not root:
            return ans

        stack =[]
        node = root
        while stack or cur:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.right
            cur = stack.pop()
            cur = cur.left
        return res[::-1]

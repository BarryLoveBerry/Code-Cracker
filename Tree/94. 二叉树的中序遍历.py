# 迭代的方法

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # ans = []
        # def inorder (root):
        #     if not root:
        #         return
        #     inorder(root.left)
        #     ans.append(root.val)
        #     inorder(root.right)
        # inorder(root)
        # return ans
        res= list()
        if not root:
            return res

        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res

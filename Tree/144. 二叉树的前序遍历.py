# 什么是二叉树
# 每个节点最多拥有俩棵子树，即二叉树中不存在度大于2的结点；并且二叉树的子树有左右之分，其次序不能任意颠倒
# 二叉树性质：
# 若二叉树的层次从0开始，则在二叉树的第i层至多2**i个结点(i>=0)
# 高度为k的二叉树最多有2^(k+1)-1个结点（k>=-1）空树的高度为-1
# 对任何一棵二叉树，如果其叶子结点（度为0）数为m，度为2的结点数为n，则m=n+1

# 二叉树的前序遍历顺序： 根 - 左 - 右

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def preorder(root:TreeNode):
            if not root:
                return
                res.append(root.val)
                preorder(root.left)
                preorder(root.right)
        res = list()
        preorder(root)
        return res

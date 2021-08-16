# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursion DFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height,right_height)+1
          
#BFS
#collections 是 python 内建的一个集合模块，里面封装了许多集合类，其中队列相关的集合只有一个：deque。
#deque 是双边队列（double-ended queue），具有队列和栈的性质，在 list 的基础上增加了移动、旋转和增删等。
#d = collections.deque([])#初始化为list
# d.append('a') # 在最右边添加一个元素，此时 d=deque('a')
# d.appendleft('b') # 在最左边添加一个元素，此时 d=deque(['b', 'a'])
# d.extend(['c','d']) # 在最右边添加所有元素，此时 d=deque(['b', 'a', 'c', 'd'])
# d.extendleft(['e','f']) # 在最左边添加所有元素，此时 d=deque(['f', 'e', 'b', 'a', 'c', 'd'])
# d.pop() # 将最右边的元素取出，返回 'd'，此时 d=deque(['f', 'e', 'b', 'a', 'c'])
# d.popleft() # 将最左边的元素取出，返回 'f'，此时 d=deque(['e', 'b', 'a', 'c'])
# d.rotate(-2) # 向左旋转两个位置（正数则向右旋转），此时 d=deque(['a', 'c', 'e', 'b'])
# d.count('a') # 队列中'a'的个数，返回 1
# d.remove('c') # 从队列中将'c'删除，此时 d=deque(['a', 'e', 'b'])
# d.reverse() # 将队列倒序，此时 d=deque(['b', 'e', 'a'])
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if  root is None:
            return 0
        queue = collections.deque([root])
        depth = 0
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth

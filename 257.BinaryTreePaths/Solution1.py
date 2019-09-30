# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root:
            total = self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)
            res = []
            if not total:
            	return [str(root.val)]
            for i in total:
            	i = (str(root.val) + '->' + i)
            	res.append(i)
            return res
        else:
        	return [ ]
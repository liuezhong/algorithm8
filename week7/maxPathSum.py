# 124. 二叉树中的最大路径和
# https://leetcode.cn/problems/binary-tree-maximum-path-sum/
class Solution:
    def __init__(self):
        self.maxSum = float('-inf')
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.getMaxSum(root)
        return self.maxSum
    def getMaxSum(self, root):
        if not root:
            return 0
        left = max(self.getMaxSum(root.left), 0)
        right = max(self.getMaxSum(root.right), 0)
        sum = left + right + root.val
        self.maxSum = max(self.maxSum, sum)
        return root.val + max(left, right)

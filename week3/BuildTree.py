from idlelib.tree import TreeNode
from typing import List, Optional


# 106. 从中序与后序遍历序列构造二叉树
# https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
class BuildTree:

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def myBuild(inorderIndexMap, inorder, postorder, inLeft, inRight, postLeft, postRight):
            if inLeft > inRight or postLeft > postRight:
                return None
            rootIndex = inorderIndexMap[postorder[postRight]]
            rightSize = inRight - rootIndex
            root = TreeNode(inorder[rootIndex])
            root.left = myBuild(inorderIndexMap, inorder, postorder, inLeft, rootIndex - 1, postLeft,
                                postRight - rightSize - 1)
            root.right = myBuild(inorderIndexMap, inorder, postorder, rootIndex + 1, inRight, postRight - rightSize,
                                 postRight - 1)
            return root

        inorderIndexMap = {value: index for index, value in enumerate(inorder)}
        return myBuild(inorderIndexMap, inorder, postorder, 0, len(inorder) - 1, 0, len(postorder) - 1)


BuildTree().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])

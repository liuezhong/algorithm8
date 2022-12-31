# https://leetcode.cn/problems/maximal-rectangle/
# 85. 最大矩形
import collections


def maximalRectangle(self, matrix: List[List[str]]) -> int:
    if not matrix:
        return 0
    m = len(matrix)
    n = len(matrix[0])
    left = [[0] * n for i in range(m)]
    result = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                left[i][j] = 1 if j == 0 else left[i][j - 1] + 1
    for j in range(n):
        stack = collections.deque()
        up = [0] * m
        down = [0] * m
        for i in range(m):
            while stack and left[stack[-1]][j] >= left[i][j]:
                stack.pop()
            up[i] = -1 if not stack else stack[-1]
            stack.append(i)
        stack.clear()
        for i in range(m)[::-1]:
            while stack and left[stack[-1]][j] >= left[i][j]:
                stack.pop()
            down[i] = m if not stack else stack[-1]
            stack.append(i)
        for i in range(m):
            height = down[i] - up[i] - 1
            area = height * left[i][j]
            result = max(result, area)
    return result

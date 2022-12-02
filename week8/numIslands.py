# 200. 岛屿数量
# https://leetcode.cn/problems/number-of-islands/
# 1.如果元素为1则把周围为一的位置连接起来
# 2、统计连通分量的个数
class Solution:
    def __init__(self):
        self.father = []
    def find(self, x):
        if x == self.father[x]:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.father[x] = y
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        self.father = [i for i in range(m * n)]
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                            self.union(self.find(i * n + j), self.find(x * n + y))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and self.find(i * n + j) == i * n + j:
                    result += 1
        return result
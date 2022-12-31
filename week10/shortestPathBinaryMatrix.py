# 1091. 二进制矩阵中的最短路径
# https://leetcode.cn/problems/shortest-path-in-binary-matrix/
import heapq


def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    if not grid or grid[0][0] == 1:
        return -1
    heap = []
    step = 0
    n = len(grid)
    dir = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    heapq.heappush(heap, (abs(n - 1) + abs(n - 1), 0))
    while heap:
        levelHeap = []
        size = len(heap)
        step += 1
        while size > 0:
            node = heapq.heappop(heap)[1]
            nodex = node // n
            nodey = node % n
            if nodex == n - 1 and nodey == n - 1:
                return step
            for x, y in dir:
                nextx = nodex + x
                nexty = nodey + y
                index = nextx * n + nexty
                if 0 <= nextx < n and 0 <= nexty < n and grid[nextx][nexty] == 0:
                    heapq.heappush(levelHeap, (abs(n - 1 - nextx) + abs(n - 1 - nexty), index))
                    grid[nextx][nexty] = 1
            size -= 1
        heap = levelHeap
    return -1




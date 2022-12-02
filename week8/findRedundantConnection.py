# 684. 冗余连接
# https://leetcode.cn/problems/redundant-connection/
# 1.如果两个元素之前不属于一个连通分量，则把两个元素连接起来，如果属于一个连通分量，则该连接为冗余连接
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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        self.father = [i for i in range( n + 2)]
        result = []
        for edge in edges:
            x = self.find(edge[0])
            y = self.find(edge[1])
            if x != y:
                self.union(edge[0], edge[1])
            else:
                result = edge
        return result

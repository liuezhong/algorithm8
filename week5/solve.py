from typing import List

# 130. 被围绕的区域
# https://leetcode.cn/problems/surrounded-regions/
def solve(self, board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    m = len(board)
    n = len(board[0])
    for i in range(m):
        self.dfs(board, i, 0)
        self.dfs(board, i, n - 1)
    for j in range(n):
        self.dfs(board, 0, j)
        self.dfs(board, m - 1, j)
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X';
            elif board[i][j] == 'A':
                board[i][j] = 'O'


def dfs(self, board, x, y):
    if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != 'O':
        return
    board[x][y] = 'A'
    self.dfs(board, x, y + 1)
    self.dfs(board, x + 1, y)
    self.dfs(board, x, y - 1)
    self.dfs(board, x - 1, y)
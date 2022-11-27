# 279. 完全平方数
# https://leetcode.cn/problems/perfect-squares/

# 优化版
def numSquares(self, n: int) -> int:
    dp = [n] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(i * i, n + 1):
            dp[j] = min(dp[j], dp[j - i * i] + 1)
    return dp[n]
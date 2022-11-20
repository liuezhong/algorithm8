# 120. 三角形最小路径和
# https://leetcode.cn/problems/triangle/
# 方法1
def minimumTotal(self, triangle: List[List[int]]) -> int:
    m = len(triangle)
    dp = [[0] * (m + 1) for i in range(m + 1)]
    for i in range(m)[::-1]:
        for j in range(len(triangle[i])):
            dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]
    return dp[0][0]

 # 方法2
 def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = [0] * (m + 1)
        for i in range(m)[::-1]:
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]
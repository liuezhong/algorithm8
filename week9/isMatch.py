# 44. 通配符匹配
# https://leetcode.cn/problems/wildcard-matching/

def isMatch(self, s: str, p: str) -> bool:
    m = len(s)
    n = len(p)
    dp = [[False] * (n + 1) for i in range(m + 1)]
    dp[0][0] = True
    for i in range(1, n + 1):
        if p[i - 1] == '*':
            dp[0][i] = True
        else:
            break
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
    return dp[m][n]
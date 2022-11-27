# 45. 跳跃游戏 II
# https://leetcode.cn/problems/jump-game-ii/
def jump(self, nums: List[int]) -> int:
    n = len(nums)
    dp = [0] * (n)
    for i in range(n):
        for j in range(1, nums[i] + 1):
            if i + j > n - 1:
                break
            if dp[i + j] == 0:
                dp[i + j] = dp[i] + 1
            else:
                dp[i + j] = min(dp[i + j], dp[i] + 1)
    return dp[n - 1]
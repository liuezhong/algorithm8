# 673. 最长递增子序列的个数
# https://leetcode.cn/problems/number-of-longest-increasing-subsequence/
def findNumberOfLIS(self, nums: List[int]) -> int:
    n = len(nums)
    dp = [1] * n
    count = [1] * n
    result = 1
    maxValue = 0
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    count[i] = count[j]
                elif dp[j] + 1 == dp[i]:
                    count[i] += count[j]
        if dp[i] > maxValue:
            maxValue = dp[i]
            result = count[i]
        elif dp[i] == maxValue:
            result += count[i]
    return result
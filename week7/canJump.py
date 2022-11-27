# 55. 跳跃游戏
# https://leetcode.cn/problems/jump-game/
# 从后往前遍历，每次记录能到达终点的i
# 时间复杂度：O(n), 空间复杂度：O(1)
def canJump(self, nums: List[int]) -> bool:
    n = len(nums)
    lastPos = n - 1
    for i in range(n - 1)[::-1]:
        if nums[i] + i >= lastPos:
            lastPos = i
    return lastPos == 0

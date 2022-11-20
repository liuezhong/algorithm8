# 70. 爬楼梯
# https://leetcode.cn/problems/climbing-stairs/
def climbStairs(self, n: int) -> int:
    pre = 0
    cur = 1
    for i in range(n):
        r = pre + cur
        pre = cur
        cur = r
    return cur
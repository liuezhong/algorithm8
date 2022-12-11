# 560. 和为 K 的子数组
# https://leetcode.cn/problems/subarray-sum-equals-k/
import collections


def subarraySum(self, nums: List[int], k: int) -> int:
    n = len(nums)
    count = 0
    pre = 0
    map = collections.defaultdict()
    map[0] = 1
    for i in range(n):
        pre += nums[i]
        if (pre - k) in map:
            count += map[pre - k]
        map[pre] = map.get(pre, 0) + 1

    return count
    
# 697. 数组的度
# https://leetcode.cn/problems/degree-of-an-array/
import collections


def findShortestSubArray(self, nums: List[int]) -> int:
    map = collections.defaultdict(list)
    n = len(nums)
    degree = 0
    minLength = 0
    for i in range(n):
        num = nums[i]
        if num not in map:
            map[num] = [1, i, i]
        else:
            map[num][0] += 1
            map[num][2] = i
    for count, first, last in map.values():
        if count > degree:
            degree = count
            minLength = last - first + 1
        elif count == degree:
            minLength = min(minLength, last - first + 1)
    return minLength



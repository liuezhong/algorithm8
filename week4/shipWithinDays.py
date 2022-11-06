# 1011. 在 D 天内送达包裹的能力
# https://leetcode.cn/problems/capacity-to-ship-packages-within-d-days/
from typing import List


def shipWithinDays(self, weights: List[int], days: int) -> int:
    right = sum(weights)
    left = max(weights)
    while left < right:
        min = (left + right) // 2
        count = self.getCount(weights, min)
        if count <= days:
            right = min
        else:
            left = min + 1
    return left


def getCount(self, weights, maxSum):
    count = 1
    sum = 0
    for weight in weights:
        if sum + weight <= maxSum:
            sum += weight
        else:
            sum = weight
            count += 1
    return count

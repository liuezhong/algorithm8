from typing import List

# 327. 区间和的个数
# https://leetcode.cn/problems/count-of-range-sum/submissions/
def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
    n = len(nums)
    sum = [0] * (n + 1)
    for i in range(n):
        sum[i + 1] = sum[i] + nums[i]
    return self.countRangeMergeSum(sum, lower, upper, 0, n)

def countRangeMergeSum(self, sum, lower, upper, left, right):
    if left >= right:
        return 0
    mid = (left + right) // 2
    result = 0
    result += self.countRangeMergeSum(sum, lower, upper, left, mid)
    result += self.countRangeMergeSum(sum, lower, upper, mid + 1, right)
    result += self.findCouple(sum, lower, upper, left, mid, right)
    print(result)
    self.merge(sum, left, mid, right)
    return result


def findCouple(self, sum, lower, upper, left, mid, right):
    count = 0
    i = left
    l = mid + 1
    r = mid + 1
    while i <= mid:
        while l <= right and sum[l] - sum[i] < lower:
            l += 1
        while r <= right and sum[r] - sum[i] <= upper:
            r += 1
        count += r - l
        i += 1
    return count


def merge(self, sum, left, mid, right):
    sorted = [0] * (right - left + 1)
    index = 0
    p1, p2 = left, mid + 1
    while p1 <= mid and p2 <= right:
        if sum[p1] <= sum[p2]:
            sorted[index] = sum[p1]
            index += 1
            p1 += 1
        else:
            sorted[index] = sum[p2]
            index += 1
            p2 += 1
    while p1 <= mid:
        sorted[index] = sum[p1]
        index += 1
        p1 += 1
    while p2 <= right:
        sorted[index] = sum[p2]
        index += 1
        p2 += 1
    for i in range(index):
        sum[left + i] = sorted[i]


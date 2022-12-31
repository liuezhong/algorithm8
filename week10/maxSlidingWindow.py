# 239. 滑动窗口最大值
# https://leetcode.cn/problems/sliding-window-maximum/
import collections


def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    if not nums:
        return []
    result = []
    deque = collections.deque()
    n = len(nums)
    for i in range(n):
        while deque and nums[deque[-1]] <= nums[i]:
            deque.pop()
        while deque and deque[0] <= i - k:
            deque.popleft()
        deque.append(i)
        if i >= k - 1:
            result.append(nums[deque[0]])
    return result
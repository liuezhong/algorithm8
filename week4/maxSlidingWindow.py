import collections
import heapq
from typing import List

# 239. 滑动窗口最大值
# https://leetcode.cn/problems/sliding-window-maximum/
# 方法1：优先队列
def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    result = list()
    heap = []
    for i, num in enumerate(nums):
        while i >= k and heap and heap[0][1] <= i - k:
            heapq.heappop(heap)
        heapq.heappush(heap, (-num, i))
        if i >= k - 1:
            result.append(-heap[0][0])
    return result

# 方法2：单调队列
def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    result = list()
    deque = collections.deque()
    for i, num in enumerate(nums):
        while deque and deque[0] <= i - k:
            deque.popleft()
        while deque and num >= nums[deque[-1]]:
            deque.pop()
        deque.append(i)
        if i >= k - 1:
            result.append(nums[deque[0]])
    return result

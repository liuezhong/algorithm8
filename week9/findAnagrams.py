# 438. 找到字符串中所有字母异位词
# https://leetcode.cn/problems/find-all-anagrams-in-a-string/
import collections
from typing import List


def findAnagrams(self, s: str, p: str) -> List[int]:
    map = collections.defaultdict()
    curMap = collections.defaultdict()
    start = 0
    result = []
    for ch in p:
        map[ch] = map.get(ch, 0) + 1
    for end in range(len(s)):
        curEnd = s[end]
        curMap[curEnd] = curMap.get(curEnd, 0) + 1
        while curMap[curEnd] > map.get(curEnd, 0):
            curLeft = s[start]
            curMap[curLeft] = curMap.get(curLeft, 0) - 1
            start += 1
        if end - start + 1 == len(p):
            result.append(start)
    return result


# 686. 重复叠加字符串匹配
# https://leetcode.cn/problems/repeated-string-match/
from math import ceil


def repeatedStringMatch(self, a: str, b: str) -> int:
    count = ceil(len(b) / len(a))
    if (a * count).find(b) != -1:
        return count
    elif (a * (count + 1)).find(b) != -1:
        return count + 1
    return -1

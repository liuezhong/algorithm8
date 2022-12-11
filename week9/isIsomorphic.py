# 205. 同构字符串
# https://leetcode.cn/problems/isomorphic-strings/
import collections


def isIsomorphic(self, s: str, t: str) -> bool:
    s2t = collections.defaultdict()
    t2s = collections.defaultdict()
    for i in range(len(s)):
        x = s[i]
        y = t[i]
        if (x in s2t and s2t[x] != y) or (y in t2s and t2s[y] != x):
            return False
        s2t[x] = y
        t2s[y] = x
    return True
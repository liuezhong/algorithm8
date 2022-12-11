# 49. 字母异位词分组
# https://leetcode.cn/problems/group-anagrams/
import collections


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    map = collections.defaultdict(list)
    for str in strs:
        arr = [0] * 26
        for ch in str:
            arr[ord(ch) - ord('a')] += 1
        map[tuple(arr)].append(str)
    return list(map.values())
# 242. 有效的字母异位词
# https://leetcode.cn/problems/valid-anagram/
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    arr = [0] * 26
    for ch in s:
        arr[ord(ch) - ord('a')] += 1
    for ch in t:
        arr[ord(ch) - ord('a')] -= 1
        if arr[ord(ch) - ord('a')] < 0:
            return False
    return True
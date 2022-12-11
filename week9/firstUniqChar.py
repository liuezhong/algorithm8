# 387. 字符串中的第一个唯一字符
# https://leetcode.cn/problems/first-unique-character-in-a-string/
def firstUniqChar(self, s: str) -> int:
    sArr = [0] * 26
    for ch in s:
        sArr[ord(ch) - ord('a')] += 1
    for i in range(len(s)):
        if sArr[ord(s[i]) - ord('a')] == 1:
            return i
    return -1
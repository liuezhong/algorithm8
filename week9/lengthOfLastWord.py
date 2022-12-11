# 58. 最后一个单词的长度
# https://leetcode.cn/problems/length-of-last-word/
def lengthOfLastWord(self, s: str) -> int:
    i = len(s) - 1
    result = 0
    while i >= 0 and s[i] == ' ':
        i -= 1
    while i >= 0 and s[i] != ' ':
        result += 1
        i -= 1
    return result
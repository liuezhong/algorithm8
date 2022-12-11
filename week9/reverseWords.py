# 151. 反转字符串中的单词
# https://leetcode.cn/problems/reverse-words-in-a-string/
def reverseWords(self, s: str) -> str:
    n = len(s)
    left = 0
    right = n - 1
    result = []
    while right >= 0 and s[right] == ' ':
        right -= 1
    while left < n - 1 and s[left] == ' ':
        left += 1
    while left <= right:
        index = right
        while index >= left and s[index] != ' ':
            index -= 1
        result.append(s[index + 1:right + 1])
        if index > left:
            result.append(' ')
        while index >= left and s[index] == ' ':
            index -= 1
        right = index
    return ''.join(result)
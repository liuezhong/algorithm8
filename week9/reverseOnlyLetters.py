# 917. 仅仅反转字母
# https://leetcode.cn/problems/reverse-only-letters/
def reverseOnlyLetters(self, s: str) -> str:
    left = 0
    right = len(s) - 1
    result = [ch for ch in s]
    while left < right:
        while left < right and not result[left].isalpha():
            left += 1
        while left < right and not result[right].isalpha():
            right -= 1
        result[left], result[right] = result[right], result[left]
        left += 1
        right -= 1
    return ''.join(result)
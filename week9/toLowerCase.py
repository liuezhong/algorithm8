# 709. 转换成小写字母
# https://leetcode.cn/problems/to-lower-case/

def toLowerCase(self, s: str) -> str:
    return "".join(chr(ord(ch) | 32) if ord('A') <= ord(ch) <= ord('Z') else ch for ch in s)
# 14. 最长公共前缀
# https://leetcode.cn/problems/longest-common-prefix/description/
def longestCommonPrefix(self, strs: List[str]) -> str:
    if len(strs) == 1:
        return strs[0]
    for i in range(len(strs[0])):
        pre = strs[0][i]
        for j in range(1, len(strs)):
            if i >= len(strs[j]) or pre != strs[j][i]:
                return strs[0][:i]
    return strs[0]
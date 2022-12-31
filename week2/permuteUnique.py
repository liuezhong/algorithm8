# 47. 全排列 II
# https://leetcode.cn/problems/permutations-ii/
def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []
    subList = []
    visited = [0] * len(nums)
    self.getPermute(result, subList, nums, visited, 0)
    return result


def getPermute(self, result, subList, nums, visited, pos):
    if pos == len(nums):
        result.append(list(subList))
        return
    for i in range(len(nums)):
        if visited[i] == 1 or (i > 0 and nums[i] == nums[i - 1] and visited[i - 1] == 0):
            continue
        subList.append(nums[i])
        visited[i] = 1
        self.getPermute(result, subList, nums, visited, pos + 1)
        subList.pop()
        visited[i] = 0

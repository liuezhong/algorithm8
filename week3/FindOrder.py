import collections
from _ast import List

# 210. 课程表 II
# https://leetcode.cn/problems/course-schedule-ii/
class FindOrder:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        relationShip = collections.defaultdict(list)
        inDag = [0] * numCourses
        result = list()
        deque = collections.deque()
        for prerequisite in prerequisites:
            relationShip[prerequisite[1]].append(prerequisite[0])
            inDag[prerequisite[0]] += 1
        for i in range(numCourses):
            if inDag[i] == 0 :
                deque.append(i)
        while deque:
            pre = deque.popleft()
            result.append(pre)
            for post in relationShip[pre]:
                inDag[post] -= 1
                if inDag[post] == 0:
                    deque.append(post)
        if numCourses != len(result):
            return list()
        return result





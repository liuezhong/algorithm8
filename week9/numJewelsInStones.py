# 771. 宝石与石头
# https://leetcode.cn/problems/jewels-and-stones/
def numJewelsInStones(self, jewels: str, stones: str) -> int:
    jewelset = set()
    count = 0
    for jewel in jewels:
        jewelset.add(jewel)
    for stone in stones:
        if stone in jewelset:
            count += 1
    return count
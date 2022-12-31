# 21. 合并两个有序链表
# https://leetcode.cn/problems/merge-two-sorted-lists/
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1 or not list2:
        return list1 if not list2 else list2
    if list1.val <= list2.val:
        list1.next = self.mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = self.mergeTwoLists(list1, list2.next)
        return list2



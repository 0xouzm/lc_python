#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            cur.next = l1
            l1 = l1.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next


# @lc code=end


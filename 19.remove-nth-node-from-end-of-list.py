#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None
        dummy = pre = ListNode(None)
        pre.next = head
        for _ in range(n - 1):
            head = head.next
        while head.next:
            pre = pre.next
            head = head.next
        pre.next = pre.next.next
        return dummy.next

# @lc code=end


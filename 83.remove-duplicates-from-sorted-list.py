#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        dummy = pre = ListNode(None)
        dummy.next = head
        while head:
            if pre.val == head.val:
                pre.next = head.next
                head = head.next
            else:
                head = head.next
                pre = pre.next
        return dummy.next

# @lc code=end


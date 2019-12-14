#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = n = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next

            v = v1 + v2 + carry
            val = v % 10
            n.next = ListNode(val)
            if v >= 10:
                carry = 1
            else:
                carry = 0
            # carry,val = divmod(v,10)
            # n.next = ListNode(val)
            n = n.next
        return root.next


# @lc code=end


#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = cur = ListNode(0)
        cur.next = head
        while cur.next and cur.next.next:
            n1 = cur.next
            n2 = cur.next.next
            next = n2.next
            cur.next = n2
            n2.next = n1
            n1.next = next
            cur = cur.next.next
        return dummy.next

        
# @lc code=end


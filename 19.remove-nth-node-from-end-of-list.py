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
        cur = head
        for _ in range(n):
            cur = cur.next
        if not cur:
            return head.next
        slow = head
        while cur.next:
            cur= cur.next
            slow = slow.next
        slow.next = slow.next.next
        return head
        
        


        
# @lc code=end


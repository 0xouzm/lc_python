#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        tmp = None
        while head:
            next = head.next
            head.next = tmp
            tmp = head
            head = next
        return tmp
        
# @lc code=end


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
        dummy = ListNode(None)
        dummy.next = head
        pre = dummy
        while pre.next and pre.next.next:
            l1 = pre.next
            l2 = pre.next.next
            nxt = l2.next
            l1.next = nxt
            l2.next = l1
            pre.next = l2
            pre = l1
        return dummy.next

            


        

        
# @lc code=end


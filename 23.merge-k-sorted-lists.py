#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def mergeTwo(l1, l2):
            dummy = cur = ListNode(0)
            while l1 and l2:
                if l1.val > l2.val:
                    l1, l2 = l2, l1
                cur.next = l1
                l1 = l1.next
                cur = cur.next
            cur.next = l1 or l2
            return dummy.next

        def merge(lists, l, r):
            if l > r:
                return None
            if l == r:
                return lists[l]
            if l + 1 == r:
                return mergeTwo(lists[l], lists[r])
            m = l + (r - l) // 2
            l1 = merge(lists, l, m)
            l2 = merge(lists, m + 1, r)
            return mergeTwo(l1, l2)

        return merge(lists, 0, len(lists) - 1)


# @lc code=end


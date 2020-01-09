#
# @lc app=leetcode id=752 lang=python3
#
# [752] Open the Lock
#

# @lc code=start
from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deads = set(deadends)
        start = "0000"
        if start in deads:
            return -1
        q = deque([(start, 0)])
        visited = set([start])
        while q:
            node, steps = q.popleft()
            for i in range(4):
                for j in [-1, 1]:
                    nxt = node[:i] + str((int(node[i]) + j + 10) % 10) + node[i + 1 :]
                    if nxt == target:
                        return steps + 1
                    if nxt in deads or nxt in visited:
                        continue
                    q.append((nxt, steps + 1))
                    visited.add(nxt)
        return -1
# @lc code=end


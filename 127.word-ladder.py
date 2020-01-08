#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordDict = set(wordList)
        if endWord not in wordList:
            return 0

        l = len(beginWord)
        steps = 0
        q = deque([beginWord])

        while q:
            steps += 1
            for _ in range(len(q)):
                w = q.popleft()
                chs = list(w)
                for i in range(l):
                    ch = chs[i]
                    for c in [chr(s) for s in range(97, 123)]:
                        if c == ch:
                            continue
                        chs[i] = c
                        t = "".join(chs)
                        if t not in wordDict:
                            continue
                        if t == endWord:
                            return steps + 1
                        wordDict.remove(t)
                        q.append(t)
                    chs[i] = ch
        return 0

# @lc code=end


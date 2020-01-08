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
        q = {beginWord}

        while q:
            steps += 1
            tmp_q = set()
            for w in q:
                chs = list(w)
                for i in range(l):
                    ch = chs[i]
                    for c in 'abcdefghikjlmnopqrstuvwxyz':
                        if c == ch:
                            continue
                        chs[i] = c
                        t = "".join(chs)
                        if t not in wordDict:
                            continue
                        if t == endWord:
                            return steps + 1
                        wordDict.remove(t)
                        tmp_q.add(t)
                    chs[i] = ch
            q = tmp_q
        return 0

# @lc code=end


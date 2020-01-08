#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        ans = []
        wordDict = set(wordList)
        if endWord not in wordDict:
            return 0
        s = {beginWord}
        l = len(beginWord)
        step = 0

        while s:
            step += 1
            tmp_s = set()
            for w in s:
                for i in range(l):
                    ch = w[i]
                    for c in string.ascii_lowercase:
                        if c == ch:
                            continue
                        tmp = w[:i] + c + w[i+1:]
                        if tmp == endWord:
                            return step + 1
                        if tmp not in wordDict:
                            continue
                        wordDict.remove(tmp)
                        tmp_s.add(tmp)
            s = tmp_s
        return 0

# @lc code=end


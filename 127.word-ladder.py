#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
import string


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordDict = set(wordList)
        if endWord not in wordDict:
            return 0
        s1 = {beginWord}
        s2 = {endWord}
        l = len(beginWord)
        step = 0

        while s1 and s2:
            step += 1
            if len(s1) > len(s2):
                s1, s2 = s2, s1
            s = set()
            for w in s1:
                for i in range(l):
                    for c in string.ascii_lowercase:
                        tmp = w[:i] + c + w[i + 1 :]
                        if tmp in s2:
                            return step + 1
                        if tmp not in wordDict:
                            continue
                        wordDict.remove(tmp)
                        s.add(tmp)
            s1 = s
        return 0


# @lc code=end


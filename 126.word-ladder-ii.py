#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#
# https://leetcode.com/problems/word-ladder-ii/description/
#
# algorithms
# Hard (20.00%)
# Likes:    1376
# Dislikes: 220
# Total Accepted:    153.3K
# Total Submissions: 765.8K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# Given two words (beginWord and endWord), and a dictionary's word list, find
# all shortest transformation sequence(s) from beginWord to endWord, such
# that:
# 
# 
# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
# 
# 
# Note:
# 
# 
# Return an empty list if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# 
# 
# Example 1:
# 
# 
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# Output:
# [
# ⁠ ["hit","hot","dot","dog","cog"],
# ["hit","hot","lot","log","cog"]
# ]
# 
# 
# Example 2:
# 
# 
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# Output: []
# 
# Explanation: The endWord "cog" is not in wordList, therefore no possible
# transformation.
# 
# 
# 
# 
# 
#

# @lc code=start
import string
from collections import defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        wordDict = set(wordList)
        wordDict.add(beginWord)
        if endWord not in wordDict:
            return []
        s = {beginWord}
        l = len(beginWord)
        found = False

        while s and not found:
            for w in s:
                wordDict.remove(w)
            tmp_s = set()
            for w in s:
                for i in range(l):
                    for c in string.ascii_lowercase:
                        tmp = w[:i] + c + w[i+1:]
                        if tmp == endWord:
                            found = True
                            ans[endWord].append(w)
                            continue
                        if tmp not in wordDict:
                            continue
                        tmp_s.add(tmp)
                        ans[tmp].append(w)
            s = tmp_s

        def dfs(k,cur):
            if ans[k][0] == beginWord:
                res.append(cur[:]+[beginWord])
                return
            for i in range(len(ans[k])):
                if i > 0 and ans[k][i] == ans[k][i-1]:
                    continue
                cur.append(ans[k][i])
                dfs(ans[k][i],cur)
                cur.pop()
        if not ans:
            return []
        res = []
        dfs(endWord,[endWord])
        for i in res:
            i.reverse()
        return res
            


                        
                    
        
# @lc code=end


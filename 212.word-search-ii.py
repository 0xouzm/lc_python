#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.is_word = True

    def find(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.is_word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ans = []
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)

        def dfs(node, i, j, cur):
            if node.is_word:
                ans.append(cur)
                node.is_word = False
            if i < 0 or i == len(board) or j < 0 or j == len(board[0]):
                return
            tmp = board[i][j]
            node = node.children.get(tmp)
            if not node:
                return
            board[i][j] = "0"
            dfs(node, i + 1, j, cur + tmp)
            dfs(node, i - 1, j, cur + tmp)
            dfs(node, i, j - 1, cur + tmp)
            dfs(node, i, j + 1, cur + tmp)
            board[i][j] = tmp

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(node, i, j, "")
        return ans


# @lc code=end


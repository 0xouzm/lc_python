#
# @lc app=leetcode id=679 lang=python3
#
# [679] 24 Game
#

# @lc code=start
from typing import List
from itertools import *
import math

#  暴力解法 共5种括号情况,熟悉itertools用法
# class Solution:
# def judgePoint24(self, nums: List[int]) -> bool:
#     operands = self.get_operands(nums)
#     ops = self.get_oprators()
#     for num in operands:
#         for op in ops:
#             s = zip_longest(num, op, fillvalue='')
#             res_s = chain.from_iterable(s)
#             s = ''.join([i for i in res_s])
#             formats = [
#                 '(({}{}{}){}{}){}{}', '({}{}({}{}{})){}{}',
#                 '{}{}(({}{}{}){}{})', '{}{}({}{}({}{}{}))',
#                 '({}{}{}){}({}{}{})'
#             ]
#             for f in formats:
#                 check_str = f.format(s[0], s[1], s[2], s[3], s[4], s[5],
#                                      s[6])
#                 print(check_str)
#                 try:
#                     if math.isclose(eval(check_str), 24):
#                         return True
#                 except ZeroDivisionError:
#                     continue
#     return False

# def get_operands(self, nums):
#     oprands = []
#     for i in permutations([str(i) for i in nums]):
#         oprands.append(i)
#     return oprands

# def get_oprators(self):
#     ops = []
#     for op in product('+-*/', repeat=3):
#         ops.append(op)
#     return ops
from operator import truediv, mul, add, sub


# 只有 4 张牌，且只能执行 4 种操作。即使所有运算符都不进行交换，最多也只有 12 * 6 * 2 * 4 * 4 * 4 = 921612∗6∗2∗4∗4∗4=9216 种可能性，这使得我们可以尝试所有这些可能。
# 具体来说，我们有 12 种方式先选出两个数字（有序），并执行 4 种操作之一（12 * 4）。然后，剩下 3 个数字，我们从中选择 2 个并执行 4 种操作之一（6 * 4）。
# 最后我们剩下两个数字，并在 2 * 4 种可能之中作出最终选择。
# 我们将对我们的数字或结果数字执行 3 次二元运算（+，-，*，/ 是运算）。因为 - 和 / 不满足交换律，我们必须仔细考虑 a / b 和 b / a。
# 对于在我们的列表中移除 a, b 这两个数字的每一种方法，以及它们可能产生的每种结果，如 a + b、a / b等，我们将采用递归的方法解决这个较小的数字列表上的问题。
# # 递归解法,回溯法
class Solution(object):
    def judgePoint24(self, A):
        if not A:
            return False
        if len(A) == 1:
            return abs(A[0] - 24) < 1e-6

        for i in range(len(A)):
            for j in range(len(A)):
                if i != j:
                    # B 为剩下的数组
                    B = [A[k] for k in range(len(A)) if i != k != j]
                    for op in (truediv, mul, add, sub):
                        # + 和 * 只算一次
                        if (op is add or op is mul) and j > i:
                            continue
                        # 避免零除错误
                        if op is not truediv or A[j]:
                            B.append(op(A[i], A[j]))
                            if self.judgePoint24(B):
                                return True
                            B.pop()
        return False


# @lc code=end


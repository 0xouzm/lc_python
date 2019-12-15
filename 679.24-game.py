#
# @lc app=leetcode id=679 lang=python3
#
# [679] 24 Game
#

# @lc code=start
from typing import List
from itertools import *
import math


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


#bool dfs(数组A){
#     if(数组A 只有1个元素 且 A[0] == 24) 返回成功;
#     for(a in 数组A){
#         for(b in 数组A){
#             if(a和b是同一个位置) continue;
#             for(op = {+,-,*,/}){
#                 if(op == + 或 op == *){
#                     if(a 和 b，已经算过1次加法和乘法) 不再重复计算,continue;
#                     c = a op b;
#                     数组left={数组A中除a和b的数字} + c;
#                     r = dfs(数组left);
#                     if(r 成功) 返回成功;
#                 }
#                 if(op == - 或者 op == /){
#                     if(op == / 并且 b为0) 除法不做，continue;
#                     c = a op b;
#                     数组left={数组A中除a和b的数字} + c;
#                     r = dfs(数组left);
#                     if(r 成功) 返回成功;
#                 }
#             }
#         }
#     }
# }
# 
# @lc code=end


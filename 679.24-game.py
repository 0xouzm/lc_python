#
# @lc app=leetcode id=679 lang=python3
#
# [679] 24 Game
#

# @lc code=start
from typing import List
from itertools import *
import math


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        operands = self.get_operands(nums)
        ops = self.get_oprators()
        for num in operands:
            for op in ops:
                s = zip_longest(num, op, fillvalue='')
                res_s = chain.from_iterable(s)
                s = ''.join([i for i in res_s])
                formats = [
                    '(({}{}{}){}{}){}{}', '({}{}({}{}{})){}{}',
                    '{}{}(({}{}{}){}{})', '{}{}({}{}({}{}{}))',
                    '({}{}{}){}({}{}{})'
                ]
                for f in formats:
                    check_str = f.format(s[0], s[1], s[2], s[3], s[4], s[5],
                                         s[6])
                    print(check_str)
                    try:
                        if math.isclose(eval(check_str), 24):
                            return True
                    except ZeroDivisionError:
                        continue
        return False

    def get_operands(self, nums):
        oprands = []
        for i in permutations([str(i) for i in nums]):
            oprands.append(i)
        return oprands

    def get_oprators(self):
        ops = []
        for op in product('+-*/', repeat=3):
            ops.append(op)
        return ops


        
# @lc code=end


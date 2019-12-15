from operator import truediv, add, sub, mul


class Solution(object):
    def judgePoint24(self, A):
        if not A:
            return False
        if len(A) == 1:
            return A[0] - 24 < 1e-6
        for i in range(len(A)):
            for j in range(len(A)):
                if i != j:
                    B = [A[k] for k in range(len(A)) if i != j != k]
                    for op in (truediv, add, mul, sub):
                        if (op is add or op is mul) and i > j:
                            continue
                        if op is not truediv or A[j]:
                            B.append(op(A[i], A[j]))
                            if self.judgePoint24(B):
                                return True
                            B.pop()
        return False

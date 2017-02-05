import itertools


class Solution(object):
    def gererateParanthesis(self, n):
        return list(self.generator('', n, n))

    def generator(self, res, left, right):
        if right >= left >= 0:
            if not right:
                yield res
            for q in self.generator(res + '(', left - 1, right): yield q
            for q in self.generator(res + ')', left, right - 1): yield q

    def iterativeGenerator(self, n):
        pass

sol = Solution()
print sol.gererateParanthesis(5)


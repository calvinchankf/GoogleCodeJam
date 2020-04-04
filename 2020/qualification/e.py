"""
    1st approach: brute-force recursive backtracking

    small dataset:      Pass
    larget dataset:     Fail
"""

class Solution(object):

    def __init__(self):
        self.template = []

    def generateAny(self, n, k):
        b = Board(n)
        self.template = [i+1 for i in range(n)]
        return self.backtracking(b, 0, n, k, 0)

    def backtracking(self, b, i, n, k, total):
        if i == n:
            trace = 0
            for i in range(n):
                trace += b.m[i][i]
            if trace == k:
                return b.m
            return None
        
        p = Permutation()
        rows = p.generate(self.template, b.ht_cols)

        for row in rows:
            if i < n-1 and (k - (total + row[i])) / ((n - i - 1) * 1.0) > n:
                continue
            b.place(i, row)
            x = self.backtracking(b, i+1, n, k, total + row[i])
            if x != None:
                return x
            b.remove(i, row)
        return None


class Permutation(object):

    def __init__(self):
        self.result = []

    def generate(self, nums, ht_cols):
        self.dfs(nums, [], ht_cols)
        return self.result
    
    def dfs(self, cands, chosen, ht_cols):
        if len(cands) == 0:
            self.result.append(chosen)
        for i in range(len(cands)):
            idx = len(chosen)
            if cands[i] in ht_cols[idx]:
                continue
            self.dfs(cands[:i] + cands[i+1:], chosen + [cands[i]], ht_cols)


class Board(object):
    def __init__(self, n):
        temp = []
        for i in range(n):
            temp.append(n * [0])
        self.m = temp
        self.ht_cols = []
        for i in range(n):
            self.ht_cols.append(set())

    def place(self, i, row):
        self.m[i] = row
        for j in range(len(row)):
            self.ht_cols[j].add(row[j])

    def remove(self, i, row):
        self.m[i] = len(self.m) * [0]
        for j in range(len(row)):
            self.ht_cols[j].remove(row[j])

# # input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# # This is all you need for most Code Jam problems.
# T = int(input())  # read a line with a single integer
# for t in range(1, T + 1):
#     N, K = [int(s) for s in raw_input().split(" ")]
#     s = Solution()
#     grid = s.generateAny(N, K)
#     if grid == None:
#         print("Case #{}: IMPOSSIBLE".format(t))
#     else:
#         print("Case #{}: POSSIBLE".format(t))
#         for row in grid:
#             print(" ".join([str(x) for x in row]))

print("-----")

s = Solution()
print(s.generateAny(3, 9))

s = Solution()
print(s.generateAny(4, 13))

s = Solution()
print(s.generateAny(4, 14))

s = Solution()
print(s.generateAny(4, 15))

s = Solution()
print(s.generateAny(4, 16))

s = Solution()
print(s.generateAny(5, 25))

# too long, should fail larget dataset
s = Solution()
print(s.generateAny(9, 81))
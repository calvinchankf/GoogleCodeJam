class Solution(object):

    def __init__(self):
        self.steps = []

    def explore(self, R, C):
        for i in range(R):
            for j in range(C):

                seen = []
                for k in range(R):
                    seen.append(C*[False])

                if self.dfs(R, C, i, j, seen) == True:
                    return self.steps
        return []

    def dfs(self, R, C, si, sj, seen):
        if len(self.steps) == R*C:
            return True
        for i in range(R):
            for j in range(C):
                if i == si:
                    continue
                if j == sj:
                    continue
                if i+j == si+sj or i-j == si-sj:
                    continue
                if seen[i][j] == True:
                    continue
                # place
                self.steps.append((i+1, j+1))
                seen[i][j] = True
                # explore
                if self.dfs(R, C, i, j, seen) == True:
                    return True
                # unplace
                self.steps.pop()
                seen[i][j] = False
        return False


# print(Solution().explore(2, 2))
print(Solution().explore(2, 5))

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    a = [int(s) for s in raw_input().split(" ")]
    try:
        steps = Solution().explore(a[0], a[1])
        if len(steps) == 0:
            print("Case #{}: IMPOSSIBLE".format(i))
        else:
            print("Case #{}: POSSIBLE".format(i))
            for s in steps:
                print("{} {}".format(s[0], s[1]))
    except:
        print("Case #{}: {}".format(i, ""))

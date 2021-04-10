"""
    1st approach:

    Time    
    Space   
"""
class Solution:
    def f(self, nums):
        self.maxMatch = 0
        self.dfs(nums, 0, 0, 1)
        return self.maxMatch
        
    def dfs(self, nums, i, curSum, curProd):
        if i == len(nums):
            if curSum == curProd:
                self.maxMatch = max(self.maxMatch, curProd)
            return
        self.dfs(nums, i+1, curSum + nums[i], curProd)
        self.dfs(nums, i+1, curSum, curProd * nums[i])

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
T = int(raw_input())  # read a line with a single integer
for t in range(1, T + 1):
    nums = []
    N = int(raw_input())
    for i in range(N):
        x, f = [int(s) for s in raw_input().split(" ")]
        nums += f * [x]
    res = Solution().f(nums)

    print("Case #{}: {}".format(t, res))

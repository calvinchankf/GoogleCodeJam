"""
    1st approach: brute force with all permutations

    Time    
    Space   
"""
def f(N, C):
    cands = [i for i in range(1, N+1)]
    
    def dfs(chosen, nums):
        if len(nums) == 0:
            if getCost(chosen[:]) == C:
                # print('done', chosen)
                return chosen
            return None
        for i in range(len(nums)): 
            x = nums[i]
            temp = dfs(chosen + [x], nums[:i] + nums[i+1:])
            if temp != None:
                return temp
        return None
    
    return dfs([], cands)
    

def getCost(nums):
    n = len(nums)
    cost = 0
    for i in range(n-1):
        x = i + 1
        if nums[i] == x:
            cost += 1
            continue
        k = -1
        for j in range(i, n):
            if nums[j] == x:
                k = j
                break
        reverseDigits(nums, i, k)
        cost += k - i + 1
    # print(nums, cost)
    return cost

def reverseDigits(nums, i, j):
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1

# print(f(4, 6))
# print(f(2, 1))
# print(f(7, 12))
# print(f(7, 2))
# print(f(2, 1000))


# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
T = int(raw_input())  # read a line with a single integer
for t in range(1, T + 1):
    N, C = [int(s) for s in raw_input().split(" ")]
    res = f(N, C)
    if res == None:
        print("Case #{}: IMPOSSIBLE".format(t))
    else:
        temp = ' '.join([str(x) for x in res])
        print("Case #{}: {}".format(t, temp))

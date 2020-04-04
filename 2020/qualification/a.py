"""
    1st approach: hashtable

    Time    
    Space   
"""
def f(grid):
    res_trace, res_row_repeated, res_col_repeated = 0, 0, 0
    for i in range(len(grid)):
        hs = set()
        for j in range(len(grid[0])):
            if i == j:
                res_trace += grid[i][j]
            hs.add(grid[i][j])
        if len(hs) < len(grid[i]):
            res_row_repeated += 1
    for j in range(len(grid[0])):
        hs = set()
        for i in range(len(grid)):
            hs.add(grid[i][j])
        if len(hs) < len(grid):
            res_col_repeated += 1
    return res_trace, res_row_repeated, res_col_repeated

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
T = int(input())  # read a line with a single integer
for t in range(1, T + 1):
    # arr = [int(s) for s in raw_input().split(" ")]
    N = int(raw_input())
    grid = []
    for s in range(N):
        arr = [int(s) for s in raw_input().split(" ")]
        grid.append(arr)
    res = f(grid)
    print("Case #{}: {} {} {}".format(t, res[0], res[1], res[2]))

print("-----")

a = [
    [1, 2, 3, 4],
    [2, 1, 4, 3],
    [3, 4, 1, 2],
    [4, 3, 2, 1],
]
print(f(a))

a = [
    [2, 3, 2, 2],
    [2, 3, 2, 2],
    [2, 2, 2, 3],
    [2, 2, 2, 2],
]
print(f(a))

a = [
    [2, 1, 3],
    [1, 3, 2],
    [1, 2, 3],
]
print(f(a))
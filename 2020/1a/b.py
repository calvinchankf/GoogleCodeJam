import math

"""
    approach: dfs

    Small Testset:      Pass
    Medium Testset:     Pass
    Larget Testset:     Fail
"""

def generatePascal(rowCount):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if rowCount <= 0:
        return []
    res = [[1]]
    for i in range(1, rowCount):
        arr = (i+1) * [1]
        for j in range(1, len(arr)-1):
            arr[j] = res[i-1][j-1] + res[i-1][j]
        res.append(arr)
    return res

# print(generatePascal(10))

def f(N):
    # root = int(math.ceil(math.sqrt(N))) + 1
    # print("----", root)
    print("----")
    triangle = generatePascal(30)
    hs = set()
    hs.add((0,0))
    result = dfs(triangle, 0, 0, N-1, [(0,0)], hs)
    for i, j in result:
        print("{} {}".format(i+1, j+1))

def dfs(triangle, i, j, remain, path, hs):
    if remain < 0:
        return None
    if remain == 0 and len(path) <= 500:
        return path
    dirs = [(-1,-1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1)]
    for di, dj in dirs:
        newI = i + di
        newJ = j + dj
        if (newI, newJ) in hs:
            continue
        hs.add((newI, newJ))
        if newI < 0 or newI == len(triangle) or newJ < 0 or newJ == len(triangle[newI]):
            continue
        b = dfs(triangle, newI, newJ, remain - triangle[newI][newJ], path + [(newI, newJ)], hs)
        hs.remove((newI, newJ))
        if b != None:
            return b
    return None

T = int(raw_input())  # read a line with a single integer
for t in range(1, T + 1):
    N = int(raw_input())
    print("Case #{}:".format(t))
    f(N)

print("-----")

f(1)
f(4)
f(19)
f(501)
f(1000)
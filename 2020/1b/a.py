"""
    1st approach: BFS + hashtable
    - our initial X and Y coordinates of (0, 0) are both even, 
        but only the first of our possible jumps (the 1-unit one) is of an odd length, 
        and all jumps after that are of even lengths. 
    - So there is no way to reach any other "even" position starting from the origin, no matter how much jumping we do.

    Small dataset   Pass
    Medium dataset  Pass
    Large dataset   Fail
"""
def f(X, Y):
    if (X + Y) % 2 == 0:
        return 'IMPOSSIBLE'
    ht = set()
    q = [(0, 0, 0, '')]
    dirs = {
        'N': (0, 1),
        'S': (0, -1),
        'E': (1, 0),
        'W': (-1, 0)
    }
    while len(q) > 0:
        i, j, steps, path = q.pop(0)
        if i == X and j == Y:
            return path
        if (i, j, steps) in ht:
            continue
        ht.add((i, j, steps))
        if i**2 + j**2 > X**2 + Y**2:
            continue
        for key in dirs:
            di, dj = dirs[key]
            q.append((i + di * 2**steps, j + dj * 2**steps, steps + 1, path + key))
    return 'IMPOSSIBLE'

# to observe the pattern, here we see that only odd sum coordinates are reachable
for i in range(-4, 5):
    for j in range(-4, 5):
        print(f(i, j))


# # input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# # This is all you need for most Code Jam problems.
# T = int(raw_input())  # read a line with a single integer
# for t in range(1, T + 1):
#     X, Y = [int(s) for s in raw_input().split(" ")]
#     res = f(X, Y)
#     print("Case #{}: {}".format(t, res))

print("-----")

"""
    2nd: math + hashtable
    - see a.jpeg

    Small dataset   Pass
    Medium dataset  Pass
    Large dataset   Pass
"""
def f(A, B):
    hs = set()
    def dfs(X, Y):
        if X == 0 and Y == 0:
            return ''
        if (X + Y) % 2 == 0:
            return None
        if (X, Y) in hs:
            return None
        hs.add((X, Y))
        if X%2 != 0:
            a = dfs((X-1)/2, Y/2)
            if a != None:
                return 'E' + a
            b = dfs((X+1)/2, Y/2)
            if b != None:
                return 'W' + b
        if Y%2 != 0:
            a = dfs(X/2, (Y-1)/2)
            if a != None:
                return 'N' + a
            b = dfs(X/2, (Y+1)/2)
            if b != None:
                return 'S' + b
    return dfs(A, B)


# print(f(2, 3))
# print(f(-2, -3))
# print(f(3, 0))
# print(f(-1, 1))
# print(f(7, 10))

# print(f(3, 2))
# print(f(-3, -2))

for i in range(-4, 5):
    for j in range(-4, 5):
        res = f(i, j)
        if res == None:
            print("IMPOSSIBLE")
        else:
            print(res)


# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
T = int(raw_input())  # read a line with a single integer
for t in range(1, T + 1):
    X, Y = [int(s) for s in raw_input().split(" ")]
    res = f(X, Y)
    if res == None:
        print("Case #{}: IMPOSSIBLE".format(t))
    else:
        print("Case #{}: {}".format(t, res))
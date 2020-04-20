"""
    1st approach: BFS + hashtable
    - our initial X and Y coordinates of (0, 0) are both even, 
        but only the first of our possible jumps (the 1-unit one) is of an odd length, 
        and all jumps after that are of even lengths. 
    - So there is no way to reach any other "even" position starting from the origin, no matter how much jumping we do.

    Time    
    Space   
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

for i in range(-100, 101):
    for j in range(-100, 101):
        print(i, j, '->')
        print(f(i, j))


# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
T = int(raw_input())  # read a line with a single integer
for t in range(1, T + 1):
    X, Y = [int(s) for s in raw_input().split(" ")]
    res = f(X, Y)
    print("Case #{}: {}".format(t, res))

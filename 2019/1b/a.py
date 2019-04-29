def initMap(n):
    mmap = []
    for _ in range(n+1):
        mmap.append((n+1)*[0])
    return mmap


def putDir(mmap, n, x, y, d):
    if d == 'N':
        for i in range(y+1, n+1):
            for j in range(n+1):
                mmap[i][j] += 1
    if d == 'S':
        for i in range(y-1, -1, -1):
            for j in range(n+1):
                mmap[i][j] += 1
    if d == 'W':
        for i in range(n+1):
            for j in range(x):
                mmap[i][j] += 1
    if d == 'E':
        for i in range(n+1):
            for j in range(x+1, n+1):
                mmap[i][j] += 1
    # for i in range(n+1):
    #     print(mmap[i])
    # print("---")

    # input() reads a string with a line of input, stripping the ' ' (newline) at the end.
    # This is all you need for most Code Jam problems.
t = int(input())  # read a line with a single integer
for k in range(1, t + 1):
    a = [int(s) for s in raw_input().split(" ")]
    n = a[1]
    mmap = initMap(n)
    # print(len(mmap), len(mmap[0]))
    for j in range(a[0]):
        c = [x for x in raw_input().split(" ")]
        putDir(mmap, n, int(c[0]), int(c[1]), c[2])

    resultX = 0
    resultY = 0
    maxInts = 0
    maxCell = [0, 0]
    for i in range(n+1):
        for j in range(n+1):
            if mmap[i][j] > maxInts:
                maxInts = mmap[i][j]
                maxCell = [i, j]

    print("Case #{}: {} {}".format(k, maxCell[1], maxCell[0]))

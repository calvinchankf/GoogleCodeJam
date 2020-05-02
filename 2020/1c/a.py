import sys
from collections import defaultdict

"""
    1st approach: hashtable + binary search

    Small       Pass
    Medium      Pass
    Big         Pass
"""
def lowerBsearch(nums, target):
    left = 0
    right = len(nums)
    while left < right:
        mid = (left + right)/2
        if target <= nums[mid]:
            right = mid
        else:
            left = mid + 1
    return left

def f(X, Y, M):

    dirs = {
        'N': (0, 1),
        'S': (0, -1),
        'E': (1, 0),
        'W': (-1, 0),
    }

    ht = defaultdict(list)
    cur = (X, Y)
    curSteps = 0
    ht[cur].append(curSteps)
    for m in M:
        dx, dy = dirs[m]
        x = cur[0] + dx
        y = cur[1] + dy
        cur = (x, y)
        curSteps += 1
        ht[(x, y)].append(curSteps)

    res = sys.maxsize

    for key in ht:
        x, y = key
        arr = ht[key]
        stepsFromFan = abs(x) + abs(y)
        idx = lowerBsearch(arr, stepsFromFan)
        if idx < len(arr):
            res = min(res, arr[idx])

    return 'IMPOSSIBLE' if res == sys.maxsize else res

# print(f(4, 4, 'SSSS'))
# print(f(3, 0, 'SNSS'))
# print(f(2, 10, 'NSNNSN'))
# print(f(0, 1, 'S'))
# print(f(2, 7, 'SSSSSSSS'))

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
T = int(raw_input())  # read a line with a single integer
for t in range(1, T + 1):
    X, Y, M = [s for s in raw_input().split(" ")]
    res = f(int(X), int(Y), M)
    print("Case #{}: {}".format(t, res))

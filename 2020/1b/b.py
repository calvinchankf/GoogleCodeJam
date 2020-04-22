import sys

"""
    1st approach: binary searh

    To use the interative tool:
    > python interactive_runner.py python3 testing_tool.py 0 -- python3 b.py
    > python interactive_runner.py python3 testing_tool.py 1 -- python3 b.py
    > python interactive_runner.py python3 testing_tool.py 2 -- python3 b.py

    Small Testset:      Pass
    Medium Testset:     Pass
    Larget Testset:     Fail
"""

def binarySearchTop():
    low = 0
    high = 10**9
    while low < high:
        mid = (low + high) // 2
        print("{} {}".format(0, mid))
        sys.stdout.flush()
        s = input()
        if s == 'HIT':
            low = mid + 1 # go up
        else:
            high = mid
    return low

def binarySearchBottom():
    low = 0
    high = -10**9
    while abs(low) < abs(high):
        mid = (low + high + 1) // 2
        print("{} {}".format(0, mid))
        sys.stdout.flush()
        s = input()
        if s == 'HIT':
            low = mid - 1 # go down
        else:
            high = mid
    return low

def binarySearchLeft():
    low = 0
    high = -10**9
    while abs(low) < abs(high):
        mid = (low + high + 1) // 2
        print("{} {}".format(mid, 0))
        sys.stdout.flush()
        s = input()
        if s == 'HIT':
            low = mid - 1 # go left
        else:
            high = mid
    return low

def binarySearchRight():
    low = 0
    high = 10**9
    while low < high:
        mid = (low + high) // 2
        print("{} {}".format(mid, 0))
        sys.stdout.flush()
        s = input()
        if s == 'HIT':
            low = mid + 1 # go right
        else:
            high = mid
    return low
    
def f(A, B):
    topY = binarySearchTop()
    # print('topY', topY)
    bottomY = binarySearchBottom()
    # print('topY', bottomY)
    leftX = binarySearchLeft()
    # print('leftX', leftX)
    rightX = binarySearchRight()
    # print('rightX', rightX)
    x = (leftX + rightX)//2
    y = (topY + bottomY)//2
    print("{} {}".format(x, y))
    sys.stdout.flush()
    result = input()

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
T, A, B = [int(s) for s in input().split(" ")] # read a line with a single integer
for t in range(T):
    f(A, B)

sys.exit()
import sys

"""
    1st approach: binary searh

    idea for large datatest:
     - - - -
    | | | | |
     - - - -
    | | | | |
     - - - -
    | | | | |
     - - - -
    | | | | |
     - - - -
    there are 25 corners, at least one corner must inside the dartboard, there must be a HIT
    after we get a HIT, we do binary search

    To use the interative tool:
    > python interactive_runner.py python3 testing_tool.py 0 -- python3 b.py
    > python interactive_runner.py python3 testing_tool.py 1 -- python3 b.py
    > python interactive_runner.py python3 testing_tool.py 2 -- python3 b.py

    Small Testset:      Pass
    Medium Testset:     Pass
    Large Testset:     Fail ?!?
"""

def binarySearchTop(x, y):
    low = y
    high = 10**9
    while low < high:
        mid = (low + high) // 2
        print("{} {}".format(x, mid))
        sys.stdout.flush()
        s = input()
        if s == 'CENTER': return None
        if s == 'HIT':
            low = mid + 1 # go up
        else:
            high = mid
    return low

def binarySearchBottom(x, y):
    low = y
    high = -10**9
    while abs(low) < abs(high):
        mid = (low + high + 1) // 2
        print("{} {}".format(x, mid))
        sys.stdout.flush()
        s = input()
        if s == 'CENTER': return None
        if s == 'HIT':
            low = mid - 1 # go down
        else:
            high = mid
    return low

def binarySearchLeft(x, y):
    low = x
    high = -10**9
    while abs(low) < abs(high):
        mid = (low + high + 1) // 2
        print("{} {}".format(mid, y))
        sys.stdout.flush()
        s = input()
        if s == 'CENTER': return None
        if s == 'HIT':
            low = mid - 1 # go left
        else:
            high = mid
    return low

def binarySearchRight(x, y):
    low = x
    high = 10**9
    while low < high:
        mid = (low + high) // 2
        print("{} {}".format(mid, y))
        sys.stdout.flush()
        s = input()
        if s == 'CENTER': return None
        if s == 'HIT':
            low = mid + 1 # go right
        else:
            high = mid
    return low
    
def f(A, B):

    r = (10**9) // 2

    x = 0
    y = 0

    if A != B:
        for i in range(-2, 3):
            isFound = False
            for j in range(-2, 3):
                x = i*r
                y = j*r
                # see if the circle is in this grid
                print("{} {}".format(x, y))
                sys.stdout.flush()
                s = input()
                if s == 'CENTER':
                    return x, y
                elif s == 'HIT':
                    isFound = True
                    break
            if isFound:
                break

    topY = binarySearchTop(x, y)
    if topY == None: return None
    # print('topY', topY)
    bottomY = binarySearchBottom(x, y)
    if bottomY == None: return None
    # print('bottomY', bottomY)
    leftX = binarySearchLeft(x, y)
    if leftX == None: return None
    # print('leftX', leftX)
    rightX = binarySearchRight(x, y)
    if rightX == None: return None
    # print('rightX', rightX)
    return (leftX + rightX)//2, (topY + bottomY)//2
    

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
T, A, B = [int(s) for s in input().split(" ")] # read a line with a single integer
for t in range(T):
    res = f(A, B)
    if res == None:
        continue
    print("{} {}".format(res[0], res[1]))
    sys.stdout.flush()
    result = input()

sys.exit()
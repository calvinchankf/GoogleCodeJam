"""

Input
2
2
SE
5
EESSSESE
 	
Output 
Case #1: ES
Case #2: SEEESSES
"""


def findLydiaPath(symbols):
    i = 0
    j = 0
    res = [(i, j)]
    for c in symbols:
        if c == 'E':
            i += 1
        elif c == 'S':
            j += 1
        res.append((i, j))
    return res


def findPath(n, symbols):
    lydiaPath = findLydiaPath(symbols)
    res = ""
    count = 0
    stack = [(0, 0, "")]
    while len(stack) > 0:
        i, j, c = stack.pop()
        res += c
        if (i, j) == (n-1, n-1):
            break
        if (i, j) == lydiaPath[count]:
            if symbols[count] == 'E':
                stack.append((i+1, j, 'S'))
            elif symbols[count] == 'S':
                stack.append((i, j+1, 'E'))
        else:
            stack.append((i+1, j, 'S'))
            stack.append((i, j+1, 'E'))
        count += 1
    return res


# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    a = input()
    b = raw_input()
    # print(a, b)
    c = findPath(int(a), b)
    print("Case #{}: {}".format(i, c))

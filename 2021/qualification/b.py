"""
    1st approach: greedy
    - only passed small and medium testcases

    Time    O(N)
    Space   O(N)
"""
def f(X, Y, S):
    n = len(S)
    arr = [c for c in S]
    res = 0
    for i in range(n-2, -1, -1):

        if arr[i] == '?':
            if arr[i+1] == 'C':
                arr[i] = 'C'
            elif arr[i+1] == 'J':
                arr[i] = 'J'

        if arr[i] == 'C' and arr[i+1] == 'J':
            res += X
        elif arr[i] == 'J' and arr[i+1] == 'C':
            res += Y
    return res

print(f(2, 3, 'CJ?CC?'))
print(f(4, 2, 'CJCJ?'))
print(f(1, 3, 'C?J'))
print(f(2, -5, '??JJ??'))
print(f(2, 5, '??J??CJC?'))

print('-----')

"""
    2nd: DP
    - learned from others

    ref:
    - https://www.youtube.com/watch?v=ARIV5lhdFbU
"""
def f(X, Y, S):
    n = len(S)

    # for each tuple, 0: C, 1: J
    cache = []
    for i in range(n):
        cache.append([2**32, 2**32])
    
    """
        Base cases

        case1: S[0] = 'C'
        cache[0] = [0, 2**32]

        case2: S[0] = 'J'
        cache[0] = [2**32, 0]

        case3: S[0] = '?
        cache[0] = [0, 0]
    """

    if S[0] != 'J':
        cache[0][0] = 0
    if S[0] != 'C':
        cache[0][1] = 0
    
    for i in range(1, n):
        # C or ?
        if S[i] != 'J':
            cache[i][0] = min(
                cache[i][0],        # 2**32
                cache[i-1][0],      # previous C
                cache[i-1][1] + Y   # JC
            )
        # J or ?
        if S[i] != 'C':
            cache[i][1] = min(
                cache[i][1],        # 2**32
                cache[i-1][1],      # previous J
                cache[i-1][0] + X   # CJ
            )
    return min(cache[n-1])

print(f(2, 3, 'CJ?CC?'))
print(f(4, 2, 'CJCJ?'))
print(f(1, 3, 'C?J'))
print(f(2, -5, '??JJ??'))
print(f(2, 5, '??J??CJC?'))

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
T = int(raw_input())  # read a line with a single integer
for t in range(1, T + 1):
    X, Y, S = raw_input().split(" ")
    X, Y = int(X), int(Y)
    res = f(X, Y, S)
    print("Case #{}: {}".format(t, res))

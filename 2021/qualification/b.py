"""
    1st approach: greedy

    Time    
    Space   
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

# print(f(2, 3, 'CJ?CC?'))
# print(f(4, 2, 'CJCJ?'))
# print(f(1, 3, 'C?J'))
# print(f(2, 5, '??J???'))
print("-----")
print(f(2, -5, '??JJ??')) # fail

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
T = int(raw_input())  # read a line with a single integer
for t in range(1, T + 1):
    X, Y, S = raw_input().split(" ")
    X, Y = int(X), int(Y)
    res = f(X, Y, S)
    print("Case #{}: {}".format(t, res))

from collections import defaultdict

"""
    LTE
"""


def f(arr):
    res = ""
    i = 0
    while len(arr) > 0:
        m = defaultdict(list)

        if len(arr) == 1:
            arr[0] = arr[0] + arr[0][0]

        for x in arr:
            if i < len(x):
                start = x[i]
                m[start].append(x)
        i += 1

        if len(m) == 3:
            return 'IMPOSSIBLE'
        elif len(m) == 2:
            if 'R' in m and 'S' in m:
                res += 'R'
                arr = m['R']
            elif 'P' in m and 'R' in m:
                res += 'P'
                arr = m['P']
            elif 'S' in m and 'P' in m:
                res += 'S'
                arr = m['S']
        elif len(m) == 1:
            if 'R' in m:
                res += 'P'
            elif 'S' in m:
                res += 'R'
            elif 'P' in m:
                res += 'S'
            break
    return res


a = [
    'R',
    'S',
    'P'
]
print(f(a))

a = [
    'RS',
]
print(f(a))

a = [
    'RS',
    'RS',
]
print(f(a))

a = [
    'PR',
    'RP',
]
print(f(a))

a = [
    'RS',
    'PS',
    'PRS',
    'PRP',
]
print(f(a))

print("-----")

a = [
    'RS',
    'PS',
    'PRSP',
    'PRP',
]
print(f(a))

a = [
    'RS',
    'PS',
    'PRSR',
    'PRS',
    'PRP',
]
print(f(a))

a = [
    'RS',
    'PS',
    'PRSP',
    'PRSP',
    'PRS',
    'PRP',
]
print(f(a))

a = [
    'RS',
    'PS',
    'PRSR',
    'PRSP',
    'PRS',
    'PRP',
]
print(f(a))

print("-----")

# # input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# # This is all you need for most Code Jam problems.
# t = int(input())  # read a line with a single integer
# for i in range(1, t + 1):
#     n = int(input())
#     arr = []
#     for j in range(n):
#         c = raw_input()
#         arr.append(c)
#     res = f(arr)
#     print("Case #{}: {}".format(i, res))

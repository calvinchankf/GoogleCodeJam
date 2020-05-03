"""
    1st approach: hashtabe
    
    Small       Pass
    Medium      Fail
    Large       Fail
"""
# local test
# fRead = open("b.in", "r")

# def f():
#     ht = {}
#     hs = set()
#     for line in fRead.readlines():
#         Q, R = line.split(" ")
#         R = R.replace('\n', '')
#         for c in R:
#             hs.add(c)
#         if R in ht:
#             ht[R] = min(ht[R], int(Q))
#         else:
#             ht[R] = Q
    

#     res = 10 * [None]
#     for key in ht:
#         val = ht[key]
#         if len(key) == 1:
#             res[val] = key
#             hs.remove(key)

#     cands = 10 * [None]
#     for key in ht:
#         val = ht[key]
#         if len(key) == 1:
#             cands[val] = key
#             if key in hs:
#                 hs.remove(key)

#     for i in range(len(cands)):
#         if cands[i] == None:
#             cands[i] = hs.pop()
    
#     res = ''.join(cands)
#     return res

# print(f())

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
T = int(raw_input())  # read a line with a single integer
for t in range(1, T + 1):
    U = int(raw_input())
    limit = 10**U - 1

    ht = {}
    hs = set()
    for i in range(10**4):
        Q, R = [s for s in raw_input().split(" ")]
        Q = int(Q)
        R = R.replace('\n', '')
        for c in R:
            hs.add(c)
        if R in ht:
            ht[R] = min(ht[R], Q)
        else:
            ht[R] = Q

    cands = 10 * [None]
    for key in ht:
        val = ht[key]
        if len(key) == 1:
            cands[val] = key
            if key in hs:
                hs.remove(key)

    for i in range(len(cands)):
        if cands[i] == None:
            cands[i] = hs.pop()
    
    res = ''.join(cands)

    print("Case #{}: {}".format(t, res))

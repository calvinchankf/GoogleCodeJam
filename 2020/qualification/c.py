"""
    1st approach: hashtable

    Time    
    Space   
"""
def f(raw_arr):
    arr = []
    for i in range(len(raw_arr)):
        arr.append((raw_arr[i][0], raw_arr[i][1], i))
    arr.sort()
    c_end = 0
    j_end = 0
    res_arr = []
    for start, end, idx in arr:
        if start < c_end and start < j_end:
            return "IMPOSSIBLE"
        if start >= c_end:
            res_arr.append(('C', idx))
            c_end = end
        else:
            res_arr.append(('J', idx))
            j_end = end
    res = ''
    for c, idx in sorted(res_arr, key=lambda x: x[1]):
        res += c
    return res

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
T = int(raw_input())  # read a line with a single integer
for t in range(1, T + 1):
    N = int(raw_input())
    arr = []
    for _ in range(N):
        interval = [int(s) for s in raw_input().split(" ")]
        arr.append(interval)
    res = f(arr)
    print("Case #{}: {}".format(t, res))

print("-----")

a = [
    [360, 480],
    [420, 540],
    [600, 660],
]
print(f(a))

a = [
    [0, 1440],
    [1, 3],
    [2, 4],
]
print(f(a))

a = [
    [99, 150],
    [1, 100],
    [100, 301],
    [2, 5],
    [150, 250],
]
print(f(a))

a = [
    [0, 720],
    [720, 1440],
]
print(f(a))
# Input
# 3
# 5
# 5 6 8 4 3
# 3
# 8 9 7
# 3
# 2 1 3

# Output
# Case #1: OK
# Case #2: 1
#

# implement pseudo code by question
def trouble_sort(list): # L is a 0-indexed list of integers
    done = False
    while not done:
        done = True
        for i in range(len(list)-2):
            if list[i] > list[i+2]:
                done = False
                list[i], list[i+2] = list[i+2], list[i]

t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    a = int(input())
    b = [int(s) for s in input().split(" ")]
    trouble_sort(b)
    result = "OK"
    for j in range(1, len(b)):
        if (b[j-1] > b[j]):
            result = j - 1
            break

    print("Case #{}: {}".format(i, result))

"""

Input
3
4
940
4444
 	
Output 
Case #1: 2 2
Case #2: 852 88
Case #3: 667 3777
"""


def split(x):
    digitCnt = 0
    cur = x
    counterpart = 0
    while cur > 0:
        temp = cur % 10
        if temp == 4:
            counterpart += 10**digitCnt
        cur /= 10
        digitCnt += 1
    return counterpart


# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    a = input()
    b = split(int(a))
    print("Case #{}: {} {}".format(i, a-b, b))

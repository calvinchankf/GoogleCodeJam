import sys

"""
    i really hate interative problem

    small dataset   Pass
    medium dataset  Fail
    large dataset   Fail
"""

T, B = [int(s) for s in raw_input().split(" ")]
for t in range(1, T + 1):
    arr = B * [0]
    for i in range(B):
        print(i+1)
        sys.stdout.flush()
        num = int(raw_input())
        arr[i] = num
        if (i+1)%10 == 0:
            print(''.join([str(x) for x in arr]))
            sys.stdout.flush()
    ok = raw_input()

sys.exit()
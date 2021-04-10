"""
    S WA LTE
"""
def f(nums):
    res = 0
    cMax = nums[0]
    for i in range(1, len(nums)):
        curr = nums[i] 
        if curr > cMax:
            cMax = curr
            # print(cMax)
            continue
        s_cMax = str(cMax)
        s_curr = str(curr)
        if len(s_cMax) == len(s_curr):
            cMax = curr * 10
            res += 1
        else:
            _j = 0
            for j in range(min(len(s_cMax), len(s_curr))):
                if s_cMax[j] != s_curr[j]:
                    break
                _j += 1
            common_prefix = s_curr[:_j]
            remaining_cMax = s_cMax[_j:]
            remaining_curr = s_curr[_j:]
            # print(common_prefix, remaining_cMax, remaining_curr)
            if len(remaining_curr) == 0:
                cand = int(remaining_cMax) + 1
                s_cand = str(cand)
                if len(s_cand) == len(remaining_cMax):
                    cMax = int(common_prefix + s_cand)
                    res += len(s_cand)
                    # print('a')
                else:
                    zeroCount = len(s_cand)
                    cMax = int(common_prefix + zeroCount * '0')
                    res += zeroCount
                    # print('b', zeroCount)
            elif remaining_cMax[0] > remaining_curr[0]:
                zeroCount = len(remaining_cMax) - len(remaining_curr) + 1
                cMax = int(s_curr + zeroCount * '0')
                res += zeroCount
                # print('c')
            else:
                zeroCount = len(remaining_cMax) - len(remaining_curr)
                cMax = int(s_curr + zeroCount * '0')
                res += zeroCount
                # print('d')
        # print(cMax)
    return res

print(f([100, 7, 10]))
print(f([10, 10]))
print(f([4, 19, 1]))
print(f([1, 2, 3]))

print("-----")

print(f([1,1,1,1,1,1,1,1,1,1,1,1]))

print(f([7751,776]))
print(f([7761,776]))
print(f([7771,776]))

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
T = int(raw_input())  # read a line with a single integer
for t in range(1, T + 1):
    N = int(raw_input())
    nums = [int(s) for s in raw_input().split(" ")]
    res = f(nums)
    print("Case #{}: {}".format(t, res))

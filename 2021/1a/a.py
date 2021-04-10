"""
    1st: greedy
    - learned from Gennady.Korotkevich
    
    consider the cases

    case1:
    [100, 1, 1, 1, 1, ....]
    100
    1 -> answer is in the range {100, 199} or x = 101, x = 101
    1 -> answer is in the range {100, 199} or x = 102, x = 102
    1 -> answer is in the range {100, 199} or x = 103, x = 103
    1 -> answer is in the range {100, 199} or x = 104, x = 104
    1 -> answer is in the range {100, 199} or x = 105, x = 105

    case2:
    [100, 7, 10]
    100
    7   -> answer is in the range {700, 799} or x = 101     => x = 700
    10  -> answer is in the range {1000, 1099} or x = 701   => x = 1000
"""
def f(nums):
    res = 0
    for i in range(1, len(nums)):
        L, R = nums[i], nums[i]
        while R <= nums[i - 1]:
            L = L * 10 + 0
            R = R * 10 + 9
            res += 1
        # print(nums[i - 1] + 1, L, R)
        nums[i] = max(nums[i - 1] + 1, L)
    # print(nums)
    return res

print(f([100, 7, 10]))
# print(f([10, 10]))
# print(f([4, 19, 1]))
# print(f([1, 2, 3]))
# print(f([100,1,1,1,1,1,1,1,1,1,1,1]))
# print(f([7751,776]))
# print(f([7761,776]))
# print(f([7771,776]))

# # input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# # This is all you need for most Code Jam problems.
# T = int(raw_input())  # read a line with a single integer
# for t in range(1, T + 1):
#     N = int(raw_input())
#     nums = [int(s) for s in raw_input().split(" ")]
#     res = f(nums)
#     print("Case #{}: {}".format(t, res))

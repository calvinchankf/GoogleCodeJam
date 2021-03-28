"""
    1st approach: brute force

    Time    
    Space   
"""
def f(nums):
    n = len(nums)
    cost = 0
    for i in range(n-1):
        x = i + 1
        if nums[i] == x:
            cost += 1
            continue
        k = -1
        for j in range(i, n):
            if nums[j] == x:
                k = j
                break
        reverseDigits(nums, i, k)
        cost += k - i + 1
        # print(nums)
    return cost

def reverseDigits(nums, i, j):
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1

print(f([4, 2, 1, 3]))
print(f([2, 1]))
print(f([7, 6, 5, 4, 3, 2, 1]))
print("-----")
print(f([1, 3, 4, 2]))
print(f([1, 2, 3, 5, 7, 6, 4]))


# # input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# # This is all you need for most Code Jam problems.
# T = int(raw_input())  # read a line with a single integer
# for t in range(1, T + 1):
#     N = int(raw_input())
#     L = [int(s) for s in raw_input().split(" ")]
#     res = f(L)
#     print("Case #{}: {}".format(t, res))

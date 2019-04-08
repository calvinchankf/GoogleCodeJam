"""
2
103 31
217 1891 4819 2291 2987 3811 1739 2491 4717 445 65 1079 8383 5353 901 187 649 1003 697 3239 7663 291 123 779 1007 3551 1943 2117 1679 989 3053
10000 25
3292937 175597 18779 50429 375469 1651121 2102 3722 2376497 611683 489059 2328901 3150061 829981 421301 76409 38477 291931 730241 959821 1664197 3057407 4267589 4729181 5335543

Output

Case #1: CJQUIZKNOWBEVYOFDPFLUXALGORITHMS
Case #2: SUBDERMATOGLYPHICFJKNQVWXZ
"""


def getPrimes(n):
    if n < 2:
        return []
    res = []
    notPrime = n*[False]
    for i in range(2, n):
        if notPrime[i] == False:
            res.append(i)
            j = 2
            while i*j < n:
                notPrime[i*j] = True
                j += 1
    return res


def bsearch(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left + right)/2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def findGcd(a, b):
    if b == 0:
        return a
    return findGcd(b, a % b)


def cryptopangram(n, nums):
    primes = getPrimes(n+1)
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    candidates = (len(nums)+1)*[0]
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            continue
        candidates[i] = findGcd(nums[i], nums[i-1])
        j = i-1
        while j >= 0 and candidates[j] == 0:
            candidates[j] = nums[j]/candidates[j+1]
            j -= 1
        j = i+1
        while j <= len(nums) and candidates[j] == 0:
            candidates[j] = nums[j-1]/candidates[j-1]
            j += 1

    # print(candidates)

    indeces = []
    for can in candidates:
        pIdx = bsearch(primes, can)
        indeces.append(pIdx)

    # sort the seen prime numbers
    clone = indeces[:]
    sortedIndeces = sorted(list(set(clone)))

    # for each prime, get the index in prime numbers
    res = ""
    for primeIdx in indeces:
        pos = bsearch(sortedIndeces, primeIdx)
        res += alphabets[pos]

    return res


# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    a = [int(s) for s in raw_input().split(" ")]
    b = [int(s) for s in raw_input().split(" ")]
    try:
        c = cryptopangram(a[0], b)
        print("Case #{}: {}".format(i, c))
    except:
        print("Case #{}: {}".format(i, ""))

"""
6 10 15
3,2 2,5 5,3
BACB

6 6 9
3,2 2,3 3,3
BABB

6 6 6 9
2,3 3,2 2,3 3,3
BABB

35 35 49 217
7,5 5,7 7,7 7,31
BABBC
"""

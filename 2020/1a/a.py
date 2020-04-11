"""
    DP like "wildcard matching" but its hard to implement

    testset 1:
"""

class Node(object):
    def __init__(self, is_word):
        self.children = 26*[None]
        self.is_word = is_word

class Trie(object):

    def __init__(self):
        self.root = Node(False)

    def insert(self, word):
        cur = self.root
        for w in word:
            idx = ord(w) - ord('A')
            if cur.children[idx] == None:
                cur.children[idx] = Node(False)
            cur = cur.children[idx]
        cur.is_word = True

    def findLongest(self):
        pass

def f(raw):
    arr = []
    for x in raw:
        s = x[::-1]
        s = s[:-1]
        arr.append(s)
    longest = ''
    for x in arr:
        if len(x) > len(longest):
            longest = x
    for x in arr:
        if x not in longest:
            return '*'
    return longest[::-1]

a = [
    "*CONUTS",
    "*COCONUTS",
    "*OCONUTS",
    "*CONUTS"
]
print(f(a))

a = [
    "*XZ",
    "*XYZ",
]
print(f(a))

a = [
    "*FUL",
    "*TIFUL",
    "*UL",
    "*BEAUTIFUL"
]
print(f(a))

a = [
    "*",
    "*TIFUL",
    "*UL",
    "*BEAUTIFUL"
]
print(f(a))

T = int(raw_input())  # read a line with a single integer
for t in range(1, T + 1):
    N = int(raw_input())
    arr = []
    for _ in range(N):
        arr.append(raw_input())
    res = f(list(set(arr)))
    print("Case #{}: {}".format(t, res))
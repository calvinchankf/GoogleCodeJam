"""
    1st: trie + recursion dfs
    - the basic idea is to count the unpair suffix
    - an intuitive idea is to build a suffix tree, and remove the "matched pairs"(by count)
    - for each legit word, we increase the count by 1(res += 1)
    - since duplicate suffix is not allowed, we return res - 2(if res >= 2) for every node

    Time    O(N)
    Space   O(logN) if tree is balanced
    
    Small Dataset: Pass
    Large Dataset: Pass
"""

"""
    Reuse classes "Node" and "Trie" from leetcode,
    https://github.com/calvinchankf/AlgoDaily/blob/master/leetcode/208-implement-trie-prefix-tree/main.py
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

def find_unpaired(node):
    res = 0
    if node.is_word:
        res += 1
    for child in node.children:
        if child != None:
            res += find_unpaired(child)
    if res >= 2:
        return res - 2
    return res

def f(arr):
    trie = Trie()
    for s in arr:
        trie.insert(s[::-1])
    
    unpair_count = 0
    for i in range(26):
        child = trie.root.children[i]
        if child != None:
            unpair_count += find_unpaired(child)
    return len(arr) - unpair_count

a = [
    'TARPOL',
    'PROL',
]
print(f(a))

a = [
    'TARPOR',
    'PROL',
    'TARPRO',
]
print(f(a))

a = [
    'CODEJAM',
    'JAM',
    'HAM',
    'NALAM',
    'HUM',
    'NOLOM',
]
print(f(a))

a = [
    'PI',
    'HI',
    'WI',
    'FI',
]
print(f(a))

T = int(input())  # read a line with a single integer
for t in range(1, T + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(raw_input())
    res = f(arr)
    print("Case #{}: {}".format(t, res))

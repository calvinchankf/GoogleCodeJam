# Input
#
# 10
# 1 CS
# 2 CS
# 1 SS
# 6 SCCSSC
# 2 CC
# 3 CSCSS
# 1 C
# 1 S
# 0 C
# 0 S

# Output
#
# Case #1: 1
# Case #2: 0
# Case #3: IMPOSSIBLE
# Case #4: 2
# Case #5: 0
# Case #6: 5

def reckon_damage(instructions):
    damage = 0
    power = 1
    for i in range(len(instructions)):
        if instructions[i] == 'C':
            power *= 2
        if instructions[i] == 'S':
            damage += power
    return damage

def char_swap(s, i, j):
    x = list(s);
    x[i], x[j] = x[j], x[i]
    return ''.join(x)

def swap_from_begining(s, resistance, prefix):
    clone = s
    last = s[0]
    cur = ''
    idx = 1
    steps = 0
    while idx < len(s):
        cur = clone[idx]
        if last == 'C' and cur == 'S':
            clone = char_swap(clone, idx-1, idx)
            steps += 1
            damn = reckon_damage(prefix + clone)
            # print("swap_from_begining {}, {}, {}".format(clone, damn, resistance))
            if damn <= resistance:
                return (clone, steps, True)
        last = clone[idx]
        idx += 1
    return (clone, steps, False)

def do(instructions, resistance):
    clone = instructions
    idx = len(clone) - 1
    last = clone[idx]
    cur = ''
    idx -= 1
    steps = 0
    while idx >= 0:
        cur = clone[idx]
        if cur == 'C' and last == 'S':
            x = swap_from_begining(clone[idx:], resistance, clone[:idx])
            clone = clone[:idx] + x[0]
            steps += x[1]
            stop = x[2]
            if stop:
                break
            # print("clone {}".format(clone))
        last = clone[idx]
        idx -= 1

    x = reckon_damage(clone)
    # print("finally {} => {} in steps: {}".format(clone, x, steps))
    if x > resistance:
        raise Exception('IMPOSSIBLE')
    return steps

def check(resistance, instructions):
    # check original damage
    damage = reckon_damage(instructions)
    # print("at first {}".format(damage))
    if damage <= resistance:
        return 0
    else:
        try:
            return do(instructions, resistance)
        except Exception as e:
            return e

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    try:
        a, b = input().split(" ")
        c = check(int(a), b)
        print("Case #{}: {}".format(i, c))
    except:
        print("Case #{}: {}".format(i, 0))

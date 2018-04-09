def isTidy(num):
    last = 0
    for digit in str(num):
        if digit >= last:
            last = digit
        else:
            return False
    return True

def findTidy(num):
    clone = num
    while not isTidy(clone):
        clone -= 1
    return clone

# x = '1'
# x += '2'
# print(x)

t = int(input())
lines = [];
for i in range(t):
    x = int(input())
    y = findTidy(x)
    lines.append('Case #{}: {}'.format(i+1, y))

for i in range(len(lines)):
    print(lines[i])

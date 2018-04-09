# conecpt:
# flip the cake within i+k-1 times, if there is still '-', it means imposible
# the order of flip actaully doesn't matter so just flip from the begin to N+k-1

def go(pancakes, k):
    clone = pancakes[0: len(pancakes)]
    count = 0
    n = len(pancakes)-k+1
    i = 0
    while i < n:
        if clone[i] == '-':
            for j in range(k):
                if clone[i+j] == '+':
                    clone = clone[0:i+j] + '-' + clone[i+j+1:len(clone)]
                else:
                    clone = clone[0:i+j] + '+' + clone[i+j+1:len(clone)]
            count += 1
        i += 1
    for i in range(len(clone)):
        if clone[i] == '-':
            count = -1
    return 'IMPOSSIBLE' if count == -1 else count

fRead = open("A-small-practice.in", "r")
fWrite = open("A-out.txt", "w")
t = fRead.readline()
lineCount = 0
for line in fRead.readlines():
    lineCount += 1
    pancakes, k = line.split(" ")
    flipsCount = go(pancakes, int(k))
    fWrite.write('Case #{}: {}\n'.format(lineCount, flipsCount))
fWrite.close()

# a = '++-'
# clone = a[0:len(a)]
# clone = clone[0:1] + '-' + clone[2:len(clone)]
# print(clone)

def shouldEliminate(grid, x, y):
    up, down, left, right = 0, 0, 0, 0
    
    i, j = x - 1, y
    while i >= 0:
        if grid[i][j] > 0:
            up += grid[i][j]
            break
        i -= 1
    
    i, j = x + 1, y
    while i < len(grid):
        if grid[i][j] > 0:
            down += grid[i][j]
            break
        i += 1
    
    i, j = x, y - 1
    while j >= 0:
        if grid[i][j] > 0:
            left += grid[i][j]
            break
        j -= 1
    
    i, j = x, y + 1
    while j < len(grid[0]):
        if grid[i][j] > 0:
            right += grid[i][j]
            break
        j += 1

    total = up + down + left + right
    count = (up > 0) + (down > 0) + (left > 0) + (right > 0)
    if count == 0:
        return False
    avg = total / (count * 1.0)
    return grid[x][y] < avg

def f(grid):
    total_interest = 0
    
    prev = 0
    while True:

        interest = 0
        clone = []
        for i in range(len(grid)):
            temp = []
            for j in range(len(grid[i])):
                temp.append(grid[i][j])
                interest += grid[i][j]
            clone.append(temp)
        
        if interest == prev:
            break
        prev = interest
        total_interest += interest
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if shouldEliminate(grid, i, j):
                    clone[i][j] = 0
        grid = clone
    
    return total_interest

T = int(raw_input())  # read a line with a single integer
for t in range(1, T + 1):
    R, C = [int(s) for s in raw_input().split(" ")]
    grid = []
    for i in range(R):
        row = [int(s) for s in raw_input().split(" ")]
        grid.append(row)
    print("Case #{}: {}".format(t, f(grid)))

print("-----")

a = [[15]]
print(f(a))

a = [
    [1, 1, 1],
    [1, 2, 1],
    [1, 1, 1]
]
print(f(a))

a = [[3,1,2]]
print(f(a))

a = [[1,2,3]]
print(f(a))

from random import randint

print(100)
for i in range(0, 100):
    x = randint(1, 100)
    y = [randint(0, 1000000000) for j in range(0, x)]
    print("{}".format(x))
    print("{}".format(' '.join(str(item) for item in y)))
print(" ")

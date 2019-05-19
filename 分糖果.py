import sys

def count(candy, basket):
    if candy < 0:
        return 0
    if candy == 1 or basket == 1:
        return 1
    return count(candy-basket,basket) + count(candy,basket-1)

for line in sys.stdin:
    line = eval(line)
    print(count(line[0],line[1]))

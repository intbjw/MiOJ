import sys

for line in sys.stdin:
    line = line.strip()
    list = eval(line)
    for i in range(1,len(list)+2):
        if i not in list:
            print(i)
            break

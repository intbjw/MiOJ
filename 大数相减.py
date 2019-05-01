import sys

for line in sys.stdin:
    a, b = line.rstrip().split('-')
    i = len(a) - 1
    j = len(b) - 1
    r = 0
    ans = ""
    while (i >= 0 and j >= 0):
        val = int(a[i]) - int(b[j]) - r
        if val >= 0:
            ans += str(val)
            r = 0
        else:
            ans += str(val + 10)
            r = 1
        i -= 1
        j -= 1

    while (i >= 0):
        val = int(a[i]) - r
        if val >= 0:
            ans += str(val)
            r = 0
        else:
            ans += str(val + 10)
            r = 1
        i -= 1
    print(ans[::-1].lstrip("0"))

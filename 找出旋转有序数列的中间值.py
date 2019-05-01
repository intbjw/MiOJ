import sys

for line in sys.stdin:
    nums=[]
    line = line.strip()
    line = line.split(',')
    for i in line:
        nums.append(int(i))
    nums = sorted(nums)
    n = len(nums)
    ans = int((n - 1) / 2)
    print(nums[ans])

import sys
for line in sys.stdin:
    line = line.strip()
    line = line.split()
    nums = [int(i) for i in line[0].split(",")]
    target = int(line[1])
    if not nums:
            print('-1')
            continue
    low, high = 0, len(nums) - 1
    flag = 0
    while low <= high:
        mid = (low + high) // 2
        if target == nums[mid]:
            print(mid)
            flag = 1
            break

        if nums[low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    if flag != 1:
        print(-1)

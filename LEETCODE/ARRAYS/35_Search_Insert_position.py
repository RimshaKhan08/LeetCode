def binSearch(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = nums[mid]

        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1   # not found

nums = [1, 3, 5, 7, 9]
target = 9
print(binSearch(nums, target))
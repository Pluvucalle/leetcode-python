def search_insert(nums, target):
    left = 0
    right = len(nums) - 1
    # We start searching for the target from the middle,
    # which is why we need both the left and right sides of the sorted array.
    # If the array wasn't sorted, we need to use more complex result.

    while left <= right:  # the loop stops when left passes right (search exhausted)
        mid = (left + right) // 2  # calculate the middle index
        if nums[mid] == target:  # if target is found, return its index
            return mid
        if nums[mid] > target:  # move search to the left half
            right = mid - 1
        elif nums[mid] < target:  # move search to the right half
            left = mid + 1

    return (
        left  # if the target is not found, return the index where it should be inserted
    )


print(my_func([1, 3, 5, 6], 7))

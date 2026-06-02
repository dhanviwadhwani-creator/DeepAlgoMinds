def findKthLargest(nums, k):
    for i in range(k-1):
        largest = max(nums)
        nums.remove(largest)

    return largest
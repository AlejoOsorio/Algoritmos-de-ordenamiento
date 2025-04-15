from utils.utils import measure_time


@measure_time
def radix_sort(nums):
    # Determine the maximum number of digits
    max_digit = len(str(max(nums)))

    # Pad the elements with zeroes if necessary
    nums = [str(num).zfill(max_digit) for num in nums]

    # Sort the list by each digit
    for i in range(max_digit - 1, -1, -1):
        buckets = [[] for _ in range(10)]

        for num in nums:
            buckets[int(num[i])].append(num)

        nums = [num for bucket in buckets for num in bucket]

    # Convert the elements back to integers
    nums = [int(num) for num in nums]
    return nums

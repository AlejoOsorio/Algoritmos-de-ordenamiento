from utils.utils import measure_time


@measure_time
def ternarySearch(A, x):
 
    (left, right) = (0, len(A) - 1)
 
    while left <= right:
 
        leftMid = left + (right - left) // 3
        rightMid = right - (right - left) // 3
 
        # leftMid = (2*left + right) // 3
        # rightMid = (left + 2*right) // 3
 
        if A[leftMid] == x:
            return leftMid
        elif A[rightMid] == x:
            return rightMid
        elif A[leftMid] > x:
            right = leftMid - 1
        elif A[rightMid] < x:
            left = rightMid + 1
        else:
            left = leftMid + 1
            right = rightMid - 1
 
    return -1
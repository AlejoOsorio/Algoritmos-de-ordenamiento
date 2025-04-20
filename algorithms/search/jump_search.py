# Este algoritmo fue extraido de https://stackabuse.com/jump-search-in-python/
import math

from algorithms.search.linear_search import __linear_search
from utils.utils import measure_time


@measure_time
def jump_search(A, item):
    # print("Entering Jump Search")
    n = len(A)                          # Length of the array
    m = int(math.sqrt(n))               # Step length
    i = 0                               # Starting interval

    while i != len(A)-1 and A[i] < item:
        # print("Processing Block - {}".format(A[i: i+m]))
        if A[i+m-1] == item:            # Found the search key
            return i+m-1
        elif A[i+m-1] > item:           # Linear search for key in block
            B = A[i: i+m-1]
            return __linear_search(B, item, i)
        i += m

    B = A[i:i+m]                        # Step 5
    # print("Processing Block - {}".format(B))
    return __linear_search(B, item, i)
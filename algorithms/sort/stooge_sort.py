# Este algoritmo fue extraido de https://rosettacode.org/wiki/Sorting_algorithms/Stooge_sort#Python
from utils.utils import measure_time


@measure_time
def stoogesort(L, i=0, j=None):
    if j is None:
        j = len(L) - 1
    if L[j] < L[i]:
        L[i], L[j] = L[j], L[i]
    if j - i > 1:
        t = (j - i + 1) // 3
        stoogesort(L, i, j - t)
        stoogesort(L, i + t, j)
        stoogesort(L, i, j - t)
    return L

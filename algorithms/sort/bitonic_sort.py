from utils.utils import measure_time


def c_swap(a, b, c, d):
    if (d == 1 and a[b] > a[c]) or (d == 0 and a[b] < a[c]):
        a[b], a[c] = a[c], a[b]


def merge(a, b, cnt, d):
    if cnt > 1:
        k = int(cnt / 2)
        for i in range(b, b + k):
            c_swap(a, i, i + k, d)
        merge(a, b, k, d)
        merge(a, b + k, k, d)


def bitonic_sort(a, b, cnt, d):
    if cnt > 1:
        k = int(cnt / 2)
        bitonic_sort(a, b, k, 1)
        bitonic_sort(a, b + k, k, 0)
        merge(a, b, cnt, d)


@measure_time
def sort(a, B, u):
    bitonic_sort(a, 0, B, u)

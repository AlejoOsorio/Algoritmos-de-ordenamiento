from utils.utils import measure_time


def linear_search(lista, objetivo):
    return __linear_search(lista, objetivo, 0)

@measure_time
def __linear_search(B, item, loc):
    # print("\t Entering Linear Search")
    i = 0

    while i != len(B):
        if B[i] == item:
            return loc+i
        i += 1
    return -1
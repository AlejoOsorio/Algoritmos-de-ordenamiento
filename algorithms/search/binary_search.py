# Este algoritmo fue extraido de https://4geeks.com/es/lesson/algoritmos-de-ordenamiento-y-busqueda-en-python
from utils.utils import measure_time

def binary_search(lista, objetivo):
    return __binary_search(lista, objetivo, 0, len(lista) - 1)

@measure_time
def __binary_search(lista, objetivo, inicio, fin ):
    if inicio > fin:
        return -1

    centro = (inicio + fin) // 2
    if lista[centro] == objetivo:
        return centro
    elif lista[centro] < objetivo:
        return __binary_search(lista, objetivo, centro + 1, fin)
    else:
        return __binary_search(lista, objetivo, inicio, centro - 1)
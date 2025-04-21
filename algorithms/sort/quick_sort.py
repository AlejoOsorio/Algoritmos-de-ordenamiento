from utils.utils import measure_time

#Esta función divide el arreglo en dos partes alrededor de un pivote (último elemento). 
#Todo lo menor o igual al pivote queda a la izquierda, y lo mayor a la derecha.
#Devuelve la posición final del pivote.

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


#Este es el algoritmo Quick Sort. Recursivamente ordena el arreglo dividiéndolo por la posición del pivote.
# El decorador @measure_time indica que se mide el tiempo de ejecución.

@measure_time
def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index - 1)
        quicksort(array, pivot_index + 1, high)



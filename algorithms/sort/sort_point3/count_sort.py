# Python3 implementation to sort an array of size n using base-n Radix Sort

# A function to do counting sort of arr[] according to the digit represented by exp. 
def countSort(arr, n, exp): 
    output = [0] * n  # O(n) -> Inicialización del arreglo de salida
    count = [0] * n   # O(n) -> Inicialización del conteo para cada posible dígito en base-n

    for i in range(n):
        count[i] = 0  # O(n) -> Inicialización explícita (ya está hecho arriba, pero se repite)

    # Contar ocurrencias del dígito actual (según exp)
    for i in range(n):  
        count[(arr[i] // exp) % n] += 1  # O(n) -> Recorrido de todos los elementos

    # Transformar count[i] para que contenga la posición final de cada dígito en output
    for i in range(1, n):  
        count[i] += count[i - 1]  # O(n)

    # Construir el arreglo de salida (ordenado por el dígito actual)
    for i in range(n - 1, -1, -1):  # O(n)
        output[count[(arr[i] // exp) % n] - 1] = arr[i]
        count[(arr[i] // exp) % n] -= 1

    # Copiar el arreglo ordenado de salida a arr[]
    for i in range(n):  
        arr[i] = output[i]  # O(n)

# Función principal para ordenar usando Radix Sort
def sort(arr, n):
    
    # Aplicar counting sort para la posición de dígito menos significativa (exp = 1)
    countSort(arr, n, 1)  # O(n)

    # Aplicar counting sort para la siguiente posición de dígito (exp = n)
    countSort(arr, n, n)  # O(n)

# Código de prueba
if __name__ == "__main__": 
    arr = [40, 12, 45, 32, 33, 1, 22]  # Arreglo de ejemplo
    n = len(arr)  # Longitud del arreglo
    print("Given array is")
    print(*arr)

    sort(arr, n)  # O(n) + O(n) = O(n) ya que Radix Sort corre d veces y d es constante (2 en este caso)

    print("Sorted array is")
    print(*arr)

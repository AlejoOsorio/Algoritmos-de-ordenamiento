from collections import Counter  # O(1): Importación de librería estándar

def relative_sort(arr1, arr2):
    # O(n): contar frecuencias de los elementos en arr1 (n = len(arr1))
    freq = Counter(arr1)
    
    index = 0  # O(1): inicialización del índice

    # O(m): recorrer los elementos de arr2 (m = len(arr2))
    for element in arr2:
        # O(freq[element]) para cada elemento. En total este while tiene O(n)
        while freq[element]:
            arr1[index] = element  # O(1): asignación en arr1
            index += 1             # O(1): incremento del índice
            freq[element] -= 1     # O(1): decremento de la frecuencia

    # O(k log k): ordenar los elementos restantes (k = elementos restantes no presentes en arr2)
    remaining = sorted(freq.elements())

    # O(k): copiar los elementos ordenados restantes en arr1 desde index hasta el final
    arr1[index:] = remaining

    return arr1  # O(1): retorno del resultado

# --- Ejecución de prueba ---

# arr1 tiene tamaño n = 11
arr1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
# arr2 tiene tamaño m = 4
arr2 = [2, 1, 8, 3]

print("Given array is")  # O(1)
print(arr1)              # O(n)

# O(n + k log k): llamada a la función principal
sorted_arr1 = relative_sort(arr1, arr2)

print("Sorted array is")  # O(1)
print(sorted_arr1)        # O(n)

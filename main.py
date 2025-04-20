import matplotlib.pyplot as plt
from algorithms.search.binary_search import binary_search
from algorithms.search.jump_search import jump_search
from algorithms.search.linear_search import linear_search
from algorithms.search.ternary_search import ternarySearch
from algorithms.sort.bitonic_sort import sort
from algorithms.sort.bubble_sort import bubble_sort
from algorithms.sort.merge_sort import mergeSort
from algorithms.sort.quick_sort import quicksort
from algorithms.sort.radix_sort import radix_sort
from utils.generate_list import file_to_list, generate_list, list_to_file
from utils.utils import print_time, write_to_json


file_list_ten = "lists/list_ten_thousand.txt"
fiel_list_hundred = "lists/list_one_hundred_thousand.txt"
file_list_million = "lists/list_one_million.txt"

lists = [file_list_ten, fiel_list_hundred, file_list_million]
keys = ["ten thousand", "one hundred thousand", "one million"]
sizes = ["\033[94mDiez mil elementos\033[0m", "\033[94mCien mil elementos\033[0m", "\033[94mUn millon de elementos\033[0m"]


# Función para probar un algoritmo de ordenamiento con los tres conjuntos de datos
def test_sort_algorithm(name, algorithm, list_times=None):
    if list_times is None:
        list_times = keys
    times = {}
    for list, size, key in zip(lists, sizes, list_times):
        print(size)
        x = file_to_list(list)
        time = algorithm(x)
        times[key] = time
        print("--> ", end="")
        print_time(name, time)
    return times


# Función para probar un algoritmo de busqeuda con los tres conjuntos de datos
def test_search_algorithm(name, algorithm, element_to_seach, list_times=None):
    if list_times is None:
        list_times = keys
    times = {}
    for list, size, key in zip(lists, sizes, list_times):
        print(size)
        x = file_to_list(list)
        time = algorithm(x, element_to_seach)
        times[key] = time
        print("--> ", end="")
        print_time(name, time)
    return times

# Permite usar la función sort en la función 'test_algoritms'
def bitonic_sort(list):
    return sort(list, len(list), 1)

# Ordena los algoritmos de mayor a menor dependiendo del tiempo de ejecución
def sort_algorithms_time(times: dict[str, dict[str, float]]):
    list_ten = {alg: t[keys[0]] for alg, t in times.items()}
    list_hundred = {alg: t[keys[1]] for alg, t in times.items()}
    list_million = {alg: t[keys[2]] for alg, t in times.items() if "one million" in t}

    times_sort = {}

    times_sort[keys[0]] = dict(sorted(
        list_ten.items(),
        key=lambda item: item[1],
        reverse=True
    ))

    times_sort[keys[1]] = dict(sorted(
        list_hundred.items(),
        key=lambda item: item[1],
        reverse=True
    ))

    times_sort[keys[2]] = dict(sorted(
        list_million.items(),
        key=lambda item: item[1],
        reverse=True
    ))

    return times_sort

# Geneara los graficos de barras segun el diccionario de tiempos
def generate_bar_charts(sorted_dict_by_size: dict[str, dict[str, float]], name = ""):
    for size, algos in sorted_dict_by_size.items():
        algorithms = list(algos.keys())
        times = [algos[alg] for alg in algorithms]

        plt.figure(figsize=(10, 6))
        plt.bar(algorithms, times, color='skyblue')
        plt.title(f"Execution Time by Algorithm ({size})")
        plt.xlabel("Algorithm")
        plt.ylabel("Time (s)")
        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.savefig(f"{name}-{size}.png")
        plt.close()


# Genera los arreglos de las tres dimensiones y los guarda en archivos txt
def generate_arrays():
    list = generate_list(10000)
    list_to_file(list, "lists/list_ten_thousand.txt")

    list2 = generate_list(100000)
    list_to_file(list2, "lists/list_one_hundred_thousand.txt")

    list3 = generate_list(1000000)
    list_to_file(list3, "lists/list_one_million.txt")


# Invoca los algoritmos de ordenamiento y retorna el tiempo que le toma a todos en ordenar los arreglos
def sort_algorithms():
    times = {}

    times["Quick Sort"] = test_sort_algorithm("Quick Sort", quicksort)
    write_to_json("times.json", times)
    print()

    times["Radix Sort"] = test_sort_algorithm("Radix Sort", radix_sort)
    write_to_json("times.json", times)
    print()

    times["Merge Sort"] = test_sort_algorithm("Merge Sort", mergeSort)
    write_to_json("times.json", times)
    print()

    times["Bitonic Sort"] = test_sort_algorithm("Bitonic Sort", bitonic_sort)
    write_to_json("times.json", times)
    print()

    times["Bubble Sort"] = test_sort_algorithm("Bubble Sort", bubble_sort, list_times=keys[:2])
    write_to_json("times.json", times)

    return times

def search_algorithms(element):
    times = {}

    times["Binary Search"] = test_search_algorithm("Binary Search", binary_search, element)
    write_to_json("times_serch.json", times)
    print()
    
    times["Jump Search"] = test_search_algorithm("Jump Search", jump_search, element)
    write_to_json("times_serch.json", times)
    print()
    
    times["Linear Search"] = test_search_algorithm("Linear Search", linear_search, element)
    write_to_json("times_serch.json", times)
    print()

    times["Ternary Search"] = test_search_algorithm("Ternary Search", ternarySearch, element)
    write_to_json("times_serch.json", times)
    
    return times


def main():
    # Se generan los arreglos y se guardan en archivos
    # generate_arrays()

    # Se ejecutan los algoritmos de ordenamiento y se almacena el tiempo de ejecución de todos
    times = sort_algorithms()

    # Se ordena el tiemo de los algoritmos de mayor a menor, separado por el arreglo ordenado
    sorted_times = sort_algorithms_time(times)

    # Se generan los graficos de barras con los tiempos ya ordenados
    generate_bar_charts(sorted_times, "sort_algorithms")

    # Busca el numero especifico con distintos algoritmos en las tres listas
    search_times = search_algorithms(69787673)
    sorted_search_times = sort_algorithms_time(search_times)
    generate_bar_charts(sorted_search_times, "search_algorithms")


if __name__ == '__main__':
    main()

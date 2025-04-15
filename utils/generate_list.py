import os
import random


def generate_list(length):
    """Genera un arreglo del tamaño de `length` con numeros aleatorios de 8 digitos"""
    list = []
    for _ in range(length):
        rand = random.randint(10000000, 99999999)
        list.append(rand)
    return list


def list_to_file(list, path_file):
    """Pasa una lista a un archivo"""

    dir_name = os.path.dirname(path_file)

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        print(f'La ruta {dir_name} ha sido creada.')

    with open(path_file, "w") as file:
        for elem in list:
            file.write(str(elem) + "\n")


def file_to_list(path_file):
    """Pasa de un archivo a una lista"""
    with open(path_file, 'r') as file:
        list = []
        elements = file.read().splitlines()
        for elem in elements[:-1]:
            list.append(int(elem))

    return list

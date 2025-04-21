import json
import time


def measure_time(function):
    "Mide y retorna el tiempo de ejecución de una función"
    def function_measured(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        duration = end - start
        return result, duration
    return function_measured


def print_time(agorith_name, time):
    if time < 1:
        # Menos de 1 segundo → milisegundos
        formated_time = f"{time * 1000:.2f} ms"
    elif time < 60:
        # Menos de 1 minuto → segundos
        formated_time = f"{time:.2f} s"
    else:
        # 1 minuto o más → minutos y segundos
        minutes = int(time // 60)
        seconds = time % 60
        formated_time = f"{minutes} min {seconds:.2f} s"

    print(f"{agorith_name}: {formated_time}")


def write_to_json(file_name, data):
    with open(file_name, "w") as archivo:
        json.dump(data, archivo, indent=4)


def read_from_json(file_name) -> dict:
    with open(file_name, "r") as archivo:
        data = json.load(archivo)
    return data

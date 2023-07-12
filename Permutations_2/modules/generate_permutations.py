# El código proporcionado parece ser un generador de permutaciones con repetición y tiene la capacidad de realizar el procesamiento en paralelo utilizando múltiples núcleos de la CPU. La generación de permutaciones se realiza en función de los valores de entrada proporcionados en chars_value, min_value y max_value.

import sys
import os
# Agregar el directorio padre al path
# La función os.path.abspath(__file__) obtiene la ruta absoluta del import sys
import os
# Agregar el directorio padre al path
# La función os.path.abspath(__file__) obtiene la ruta absoluta del archivo actual. Luego, os.path.dirname obtiene el directorio padre de esa ruta, y nuevamente os.path.dirname obtiene el directorio padre del directorio anterior. Finalmente, sys.path.append agrega ese directorio al sys.path, permitiendo que Python encuentre el módulo correctamente al importarlo.
sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


# import time
# import os
# import timeit
# from multiprocessing import Lock, Process, cpu_count
# from itertools import product
# from data.permutations_params import chars_value, min_value, max_value


# class PermutationGenerator:
#     def __init__(self, chars_value, min_value, max_value):
#         self.chars_value = chars_value
#         self.min_value = min_value
#         self.max_value = max_value

#     def generate_permutations(self):
#         start_time = time.time()
#         path = "dataCreated/permutations.txt"

#         # Crea el directorio si no existe
#         os.makedirs(os.path.dirname(path), exist_ok=True)

#         num_cores = cpu_count()

#         processes = []

#         for _ in range(num_cores):
#             p = Process(target=self._worker, args=(path,))
#             p.start()
#             processes.append(p)

#         for p in processes:
#             p.join()

#         end_time = time.time()  # Tiempo de final de la ejecución
#         duration = end_time - start_time  # Duración total de la ejecución

#         self._remove_duplicates(path)

#         print("\tPermutations generated successfully.")
#         print(f"\tDuration: {duration:.2f} sec.")

#     def _worker(self, path):
#         # Genera las permutaciones con repetición y las escribe en el archivo
#         lock = Lock()

#         with open(path, "a") as file:
#             for r in range(self.min_value, self.max_value + 1):
#                 self._generate_permutation(r, file, lock)

#     def _generate_permutation(self, r, file, lock):
#         for permutation in product(self.chars_value, repeat=r):
#             permutation_str = "".join(permutation)
#             with lock:
#                 file.write(permutation_str + "\n")

#     def _remove_duplicates(self, path):
#         lines_seen = set()
#         temp_file = path + ".temp"

#         with open(path, "r") as input_file, open(temp_file, "w") as output_file:
#             for line in input_file:
#                 if line not in lines_seen:
#                     output_file.write(line)
#                     lines_seen.add(line)

#         os.replace(temp_file, path)



# if __name__ == "__main__":
#     permutation_generator = PermutationGenerator(chars_value, min_value, max_value)
#     permutation_generator.generate_permutations()
    



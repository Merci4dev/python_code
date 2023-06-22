
# Calcular el número máximo de permutaciones posibles permitiendo caracteres repetidos
import time
from itertools import product
from data.params_data import char_value, max_value, min_value
# from  data.params_data import char_value, max_value, min_value

class CalculateCombinations:
    def calculate_permutations_count(self, n, r):
        start_time = time.time()

        permutations = n ** r

        return permutations


num_unique_chars = len(set(char_value))
calculateCombinations = CalculateCombinations()

total_permutations = 0
for r in range(min_value, max_value + 1):
    num_permutations = calculateCombinations.calculate_permutations_count(num_unique_chars, r)
    total_permutations += num_permutations

# Imprimir el resultado
# print("Número de permutaciones posibles (permitiendo repetición) entre", min_value, "y", max_value, "caracteres:")
# print(total_permutations)


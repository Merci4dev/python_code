
import time
from itertools import product
from data.params_data import get_string, get_min_value, get_max_value

from modules.calculate_combinations import CalculateCombinations


def generate_permutations():
    char_value = get_string()
    max_value = get_max_value()
    min_value = get_min_value()

    class GenerateCombinations:
        def generate_combinations(self, n, r):
            permutations = CalculateCombinations().calculate_permutations_count(n, r)
            return permutations

    num_unique_chars = len(set(char_value))
    generateCombinations = GenerateCombinations()

    start_time = time.time()
    print(f"Started at: {start_time}")

    total_permutations = 0

    with open("permutations.txt", "w") as file:
        for r in range(min_value, max_value + 1):
            num_permutations = generateCombinations.generate_combinations(num_unique_chars, r)
            total_permutations += num_permutations
            
            file.write(f"Permutations for r = {r}:\n")
            
            for permutation in product(char_value, repeat=r):
                permutation_str = "".join(permutation)
                file.write(permutation_str + "\n")
    
    end_time = time.time()
    # print(f"Ended at: {end_time}")
    print(f"Elapsed time: {end_time - start_time} seconds")

    return total_permutations



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
 


from data.permutations_params import chars_value, min_value, max_value
from data.permutations_params import DataPermutationValues

# TODO
# Extract the data to ensure we are using the validation
permutation_data = DataPermutationValues(chars_value, min_value, max_value)
chars_value = permutation_data.get_chars_value()
min_value = permutation_data.min_value
max_value = permutation_data.max_value

# Calculate the maximum number of possible permutations allowing repeated characters
class CalculatePermutations:
    def calculate_combinations(self, n, r):
        # Uncomment this code if you want to calculate combinations instead of permutations
        # combinations = math.comb(n, r)
        # return combinations
        
        # Or with casting
        n = int(n)
        r = int(r)
        permutations = n ** r
        return permutations

    def calculate_total_permutations(self, n, min_value, max_value):
        total_permutations = 0
        
        for r in range(min_value, max_value + 1):
            num_permutations = self.calculate_combinations(n, r)
            total_permutations += num_permutations
        return total_permutations

num_unique_chars = len(set(chars_value))
calculate_permutations = CalculatePermutations()

total_permutations = calculate_permutations.calculate_total_permutations(num_unique_chars, min_value, max_value)

#======================================================
# print("\n\t ***********************")
# print(f"\t Permutations between: {min_value} & {max_value} are: \n\t {total_permutations}")
# print("\n\t ***********************")







# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from data.permutations_params import chars_value, min_value, max_value
from data.permutations_params import DataPermutationValues
from modules.graphic_symbol import SymbolSequence
from modules.characters_counter import CharactersCounter
from modules.calculate_combinations import  CalculatePermutations
from modules.system_info import SystemInfo
from modules.permutations_time_creation import PermutationTimeCreation
from modules.generate_permutations import PermutationGenerator


if __name__ == "__main__":
 
    #=====================================
    # # Imprime una secuencia de simbolo 
    symbol_generator = SymbolSequence()
    symbol_generator.generate_sequence()

    # Render the permutation data
    #=====================================
    permutation_data_counter = DataPermutationValues(chars_value)
    chars_values = permutation_data_counter.get_chars_value()
    print(f"\t Chars Values: {chars_values}")

    # # Render the permutation character number
    # #=====================================
    chars_counter = CharactersCounter()
    chars_number = chars_counter.characters_counter(chars_value)
    print(f"\t Chars Numbers: {chars_number}")

    # Render the total permutation nuber to create
    #=====================================
    calculate_permutations = CalculatePermutations()
    num_unique_chars = len(set(chars_value))

    total_permutations = calculate_permutations.calculate_total_permutations (num_unique_chars, min_value, max_value)

    print(f"\t Permutations between: {min_value} & {max_value} are: \n\t {total_permutations}")

    #=====================================
    system_info = SystemInfo()
    permutation_time_creation = PermutationTimeCreation(system_info, calculate_permutations)
    permutation_time = permutation_time_creation.calculate_permutation_time(num_unique_chars, min_value, max_value)

    permutation_time_creation = permutation_time_creation.print_formatted_time(permutation_time)

    #=====================================
    # system_info = SystemInfo()
    # speed = system_info.get_task_creation_speed()
    # print(f"\t {speed:.2f}")

    #=====================================
    permutation_generator = PermutationGenerator(chars_value, min_value, max_value)
    permutation_generator.generate_permutations()
    # print(permutation_generator)

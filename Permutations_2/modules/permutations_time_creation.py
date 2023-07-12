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


# from publiC.Python.Permutations_2.modules.system_info import SystemInfo
from data.permutations_params import chars_value, min_value, max_value
# from calculate_combinations import CalculatePermutations
from modules.calculate_combinations import CalculatePermutations
from modules.system_info import SystemInfo

system_info = SystemInfo()
calculate_combinations = CalculatePermutations()


class PermutationTimeCreation:
    def __init__(self, system_info, calculate_combinations):
        self.system_info = system_info
        self.calculate_combinations = calculate_combinations

    def calculate_permutation_time(self, n, min_value, max_value):
        total_permutations = self.calculate_combinations.calculate_total_permutations(n, min_value, max_value)
        task_creation_speed = self.system_info.get_task_creation_speed()

        if task_creation_speed == 0:
            return 0

        permutation_time = total_permutations / task_creation_speed
        return permutation_time

    def print_formatted_time(self, time_in_seconds):
        if time_in_seconds < 60:
            print(f"\t Permutation Stimated Time: {time_in_seconds:.2f} seconds")
        elif time_in_seconds < 3600:
            time_in_minutes = time_in_seconds / 60
            print(f"\t Permutation Stimted Time: {time_in_minutes:.2f} minutes")
        elif time_in_seconds < 86400:
            time_in_hours = time_in_seconds / 3600
            print(f"\t Permutation Stimated Time: {time_in_hours:.2f} hours")
        else:
            time_in_days = time_in_seconds / 86400
            print(f"\t Permutation Stimated Time: {time_in_days:.0f} days")


# =============================================
# permutation_time_creation = PermutationTimeCreation(system_info, calculate_combinations)

# num_unique_chars = len(set(chars_value))
# permutation_time = permutation_time_creation.calculate_permutation_time(num_unique_chars, min_value, max_value)

# permutation_time_creation.print_formatted_time(permutation_time)
# print(f"\t Permutation Stimated Time: {permutation_time:.2f}")


import sys
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


# # Obtén la ruta del directorio principal
# current_dir = os.path.dirname(os.path.abspath(__file__))
# parent_dir = os.path.dirname(current_dir)

# # Agrega el directorio principal a la ruta de importación
# sys.path.insert(0, parent_dir)
 

# from data.permutations_params import *
from data.permutations_params import DataPermutationValues
from data.permutations_params import chars_value

# Extract the chars_value
permutation_data = DataPermutationValues(chars_value)
chars_value = permutation_data.get_chars_value()

# Class to to count the character lenght
class CharactersCounter:
    def characters_counter(self, chars_value):

        counter = 0
        for char in chars_value:
            counter += 1
        return counter
    
# =============================================
# char_counter = CharactersCounter()
# chars_number = char_counter.characters_counter(chars_value)
# print("\t  Chars:",chars_number)
# print("\t **********************")

from modules.characters_counter import CharactersCounter
from modules.calculate_combinations import CalculateCombinations
from modules.generate_combinations import generate_permutations
from data.params_data import get_string, min_value, max_value

# En resumen, if __name__ == "__main__": proporciona una forma de ejecutar cierto código solo cuando el archivo actual se ejecuta directamente, y no cuando se importa como un módulo. Esto es útil cuando tienes código que solo deseas ejecutar cuando el archivo se ejecuta directamente, pero no cuando se importa desde otro archivo.

if __name__ == "__main__":
    
    # Obtener el número de caracteres
    counter = CharactersCounter()
    char_value = get_string()
    chars_number = counter.character_counter(char_value)
    print(f"Character Numbers {chars_number}")


    # Calcular el número total de permutaciones
    calculateCombinations = CalculateCombinations()
    num_unique_chars = len(set(char_value))
    total_permutations_len = 0
    for r in range(min_value, max_value + 1):
        num_permutations = calculateCombinations.calculate_permutations_count(num_unique_chars, r)
        total_permutations_len += num_permutations

    print(f"Permutation number between {min_value} y {max_value} characters: {total_permutations_len}")


    # Generar el archivo con las permutaciones
    total_permutations_created = generate_permutations()
    
    print(f"Permutation created: {total_permutations_created}")
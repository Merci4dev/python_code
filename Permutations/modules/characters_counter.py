# clase que cuenta el número de caracteres en un string
# Usar def contar_caracteres(self, cadena) permite tener métodos más específicos y modularizados en la clase, lo que puede facilitar el mantenimiento y la reutilización del código en escenarios más complejos.
from data.params_data import get_string

# Esta clase no exporta de manera implicita el metodo get_string(). Es decir hay que llamarlo en el main fime 
class CharactersCounter:
    def character_counter(self, input_str):
        counter = 0
        for char in input_str:
            counter += 1
        return counter




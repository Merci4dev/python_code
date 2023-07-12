
import time

# Imprime una secuencia de simbolo 
class SymbolSequence:
    def generate_sequence(self, wati_time = 0.05):
        # symbol = "\u2588"
        symbol = "*"

        for _ in range(10):
            # Imprimir el símbolo seguido de un espacio en blanco
            print(symbol , end=" ")  
            # Forzar la impresión inmediata
            time.sleep(wati_time)

            print("\b", end=" ", flush=True)  # Retroceder un carácter

        print()  # Imprimir una nueva línea al final
 


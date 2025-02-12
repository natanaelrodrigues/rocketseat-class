print("Exemplo de importação de módulo padrão:")
#import math
from math import sqrt

#raiz = math.sqrt(25) se importar todo o math
raiz = sqrt(25)
print("Raiz Quadrada de 25:", raiz)

print("\n Exemplo de criação de utilização de um módulo personalizado...")
import meu_modulo
meu_modulo.saudacao("Natanael")
print(f"O resultado do dobro de 5 é {meu_modulo.dobro(5)}")
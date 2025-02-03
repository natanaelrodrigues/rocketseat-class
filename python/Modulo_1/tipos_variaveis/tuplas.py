"""
Uma tupla é imutável. 
"""

# Criando uma Tupla
minha_tupla = (1, 2, 2, 3, 4)
print("Minha Tupla:", minha_tupla)

# Acessando os elementos
print("Minha Tupla na posição 1:", minha_tupla[0])
print("Minha Tupla na posição 3:", minha_tupla[2])
print("Minha Tupla no último elemento:", minha_tupla[-1])

# Método Count
contagem = minha_tupla.count(2)
print("Quantidade e de vezes que o elemento 2 aparece na tupla:", contagem)

# Método index
indice = minha_tupla.index(3)
print("Indice da primeira ocorrencia do elemento 3:", indice)

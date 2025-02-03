minha_lista = [1, 2, 3, 4, 5, "Rocketseat", True, False]

# Exibindo a lista
print("Minha lista de exemplo", minha_lista)

# Exibindo o elemento
print("Elemento da lista",minha_lista[5])

# Exibindo intervalo de elementos / fatiamento
print("Intervalo de elementos da lista",minha_lista[1:6])

# Exibindo intervalo de elementos / fatiamento
print("Intervalo de elementos da lista",minha_lista[:6])

# Exibindo intervalo de elementos / fatiamento
print("Intervalo de elementos da lista",minha_lista[3:])

# Trocando o primeiro elemento.
minha_lista[0] = "Python"
print("Lista alterada", minha_lista)

# Métodos de lista
# Adicionando um elemento ao final da lista.
minha_lista.append("6")
print("Lista alterada", minha_lista)

# Retorna o indice do elemento.
print("Indice do elemento 'Rocketseat'", minha_lista.index("Rocketseat"))

# Adicionando um elemento em um indice específico da lista.
minha_lista.insert(5,"Programação")
minha_lista.insert(2,10)
print("Lista alterada", minha_lista)


# Remove um elemento em um indice específico da lista.
elemento_removido = minha_lista.pop(3)
print("Elemento removido depois do pop", elemento_removido)
print("Lista alterada", minha_lista)

# Remove o primeiro elemento em um valor especificado na lista.
minha_lista.remove(True)
print("Lista alterada", minha_lista)

# Organização de uma lista.
minha_lista = [6,5,4,3,2,8]
minha_lista.sort()
print("Lista alterada (minha_lista = [6,5,4,3,2,8])", minha_lista)


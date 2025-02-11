# for com lista
print("-------- INICIO  LISTA --------")
lista = [1, 2, 3, 4, 5]
for elemento in lista:
  print(elemento)
print("-------- FIM --------")

# for com tupla
print("-------- INICIO TUPLA --------")
tupla = [1, 2, 3, 4, 5]
for elemento in tupla:
  print(elemento)
print("-------- FIM --------")

# for com DICIONÁRIO
print("-------- INICIO DICIONARIO --------")
pessoa = {"nome": "João", "idade":90, "cidade": "São Paulo"}

print("FOR DAS CHAVES")

for chave in pessoa.keys():
  print(chave)

print("\n--------------------------------")
print("FOR DAS VALORES")

for valor in pessoa.values():
  print(valor)  

print("\n--------------------------------")
print("FOR DAS CHAVE E VALORES(Itens) ")

for chave, valor in pessoa.items():
  print(f"{chave}: {valor}" )    
print("-------- FIM --------")

# range(): Intervalo numérico em formato de lista
print("\n--------------------------------")
print("range()")
print(list(range(0,10)))

for numero in range(5):
  print("Numero:", numero)

print("\nUtilizando o Range com len")
lista = [1, 2, 3, 4, 5, 6, 7]
for indice in range(0,len(lista)):
  print("\nIndice:", indice)
  print("Elemento:", lista[indice])

# enumerate();
print("\n-------FUNCAO ENUMERATE-----------------")
lista_enum = ["a","b","c"]

for indice, valor in enumerate(lista_enum):
  print(f"{indice}: {valor}")
print("Exemplo de while")
contador = 0

while contador < 5:
  print("contagem:", contador)
  contador += 1
print("----------------")

print("\nExemplo de while com break")
contador = 0

while contador < 50:
  print("contagem:", contador)
  contador += 1
  if contador == 4:
    break
print("----------------")
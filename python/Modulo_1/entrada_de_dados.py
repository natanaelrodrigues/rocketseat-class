idade = int(input("Informe uma idade:"))

print("Usando o else/elif")
if idade >= 18:
  print("Você é maior de idade")
elif idade >= 12:
  print("Você é um Adolescente")
else:
  print("Você é menor de idade")
idade = 18
print("Exemplo de comando if")

if idade >= 18:
  print("Você é maior de idade")

if idade == 19:
  print("Você tem 19 anos.")

if idade <= 17:
  print("Você é menor de idade.")

if idade != 10:
  print("Você não tem 10 anos.")


print("Usando o else/elif")
if idade >= 18:
  print("Você é maior de idade")
elif idade >= 12:
  print("Você é um Adolescente")
else:
  print("Você é menor de idade")

## Comparador ternario
mensagem = "Pode tirar a carteira de habilitação" if idade >= 18  else "Você não pode tirar a carteira de habilitação"
print("Pode tirar a carteira de habilitação?",mensagem)

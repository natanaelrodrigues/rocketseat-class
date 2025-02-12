print("Exemplo de captura de exceções")
try:
  numero = int(input("Digite um número inteiro:"))
  resultado = 10/numero
except ValueError as e:
  print(f"Erro de Value error: {e}")
  raise ValueError("Tipo de variáveis incompatíveis")
except Exception as e:
  print(f"Erro: {e}")
else:
  print(resultado) # o else só executa se deu certo.
finally:
  print("Operaçao finalizada") # independente se deu certo ou errado, vai rodar o finally

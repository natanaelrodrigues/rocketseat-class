# POO

# Classe Exemplo - Pessoa
class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
  
  def saudacao(self):
    return f"Ola, meu nome é {self.nome} e eu tenho {self.idade} anos!"


# Objeto - Instancia de uma classe
pessoa1 = Pessoa("Natanael Roberto", 99)
print("Nome:",pessoa1.nome)
print("Idade:",pessoa1.idade)
mensagem = pessoa1.saudacao()
print(mensagem)

pessoa2 = Pessoa(nome="João Silva", idade=90)
print(pessoa2.saudacao())
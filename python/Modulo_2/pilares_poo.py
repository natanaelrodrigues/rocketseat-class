# Exemplo de Herança
class Animal:
  def __init__(self, nome):
    self.nome = nome
  
  def andar(self):
    print(f"O animal {self.nome} andou.")
    return

  def emitir_som(self):
    pass

# Cachorro e Gato herdando de animal.
class Cachorro(Animal):
  def emitir_som(self):
    return "Au, au..."


class Gato(Animal):
  def emitir_som(self):
    return "Miau..."
  

dog = Cachorro(nome="Rex")
cat = Gato(nome="Felix")

animais = [dog, cat]

for animal in animais:
  print(f"{animal.nome} faz: {animal.emitir_som()}")

# exemplo de emcapsulamento
class ContaBancaria:
  def __init__(self, saldo):
    self.__saldo = saldo # Atributo privado, quando houver dois underlines, diz que o atributo é privado.

  def depositar(self, valor):
    if valor > 0:
      self.__saldo += valor
    

  def sacar(self, valor):
    if valor > 0 and valor <= self.__saldo:
      self.__saldo -= valor

  def consultar_saldo(self):
    return self.__saldo
    

conta = ContaBancaria(1000)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")

conta.depositar(650)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")

conta.sacar(850)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")

# Abstração
from abc import ABC, abstractmethod

class Veiculo(ABC):

  @abstractmethod
  def ligar(self):
    pass

  @abstractmethod
  def desligar(self):
    pass

class Carro(Veiculo):
  def __init__(self):
    pass

  def ligar(self):
    pass

  def desligar(self):
    pass

carro_amarelo = Carro()
# @classnethod
# @staticmthod

class MinhaClasse:
  valor = 10 # Atributo da classe

  def __init__(self, nome):
    self.nome = nome # Atributo da instancia.

  # requer uma instância para ser chamado.
  def metodo_instancia(self):
    return f"Methodo da instância chamado para {self.nome}"
  
  @classmethod
  def metodo_classe(cls):
    print(f"Método da classe chamado para valor={cls.valor}")

  @staticmethod
  def metodo_statico():
    return "Método estático chamado"

obj = MinhaClasse(nome="Classe Exemplo")
print(obj.metodo_instancia())
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_statico())


class Carro:
  def __init__(self, marca, modelo, ano):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano

  @classmethod
  def criar_carro(cls, configuracao):
    marca, modelo, ano = configuracao.split(",")
    return cls(marca, modelo, int(ano))

configuracao1 = "Toyota,Corolla,2022"
carro1 = Carro.criar_carro(configuracao1)
print(f"\n\n\nMarca: {carro1.marca} \nModelo: {carro1.modelo} \nAno: {carro1.ano}")


class Matematica:
    @staticmethod
    def somar(a, b):
      return a + b
    
print(f"Resultado da soma: {Matematica.somar(a=50, b=78)}")
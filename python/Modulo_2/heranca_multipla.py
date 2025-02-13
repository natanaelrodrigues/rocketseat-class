class Animal():
  def __init__(self, nome):
    self.nome = nome
  
  def emitir_som(self):
    print('===========================')


class Mamifero(Animal):
  def amamentar(self):
    return f"{self.nome} está amamentando."
  
class Ave(Animal):
  def voar(self):
    return f"{self.nome} está voando."

# Herança Múltipla
class Morcego(Mamifero, Ave):
  def emitir_som(self):
    super().emitir_som()
    return "Morcegos emitem sons ultrassônicos"


morcedo = Morcego("Cazuza")
print(morcedo.emitir_som())
print(morcedo.voar())
print(morcedo.amamentar())
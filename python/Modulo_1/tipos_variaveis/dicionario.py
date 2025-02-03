# Criando um dicionário
pessoa = {
    "nome":"Natanael Roberto Rodrigues",
    "idade": 99,
    "cidade": "Joinville"
}
print("Primeiro dicionário:",pessoa)

# Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

# Atribuir um valor ao dicionário já existente.
pessoa["sobrenome"] = "Rodrigues"
pessoa["status"] = True
print("Sobrenome:", pessoa["sobrenome"])

print("Dicionário completo:",pessoa)

# Alterando uma propriedade
pessoa["idade"] = 90
print("Idade atualizada:", pessoa["idade"])

# Remover um par chave/valor.
del pessoa["sobrenome"]
print("Dicionário completo após remoção:",pessoa)

# métodos:

# keys()
chaves = list(pessoa.keys());
print("Chaves do dicionário:", chaves)
print("Chave do dicionário:", chaves[1])

# values()
valores = list(pessoa.values());
print("Valores do dicionário:", valores)

# itens() > Retorna uma lsita de tuplas
itens = list(pessoa.items());
print("Pares chave/valor do dicionário:", itens)
print("Primeiro Chave-valor: %s = %s" % (itens[0][0], itens[0][1]))

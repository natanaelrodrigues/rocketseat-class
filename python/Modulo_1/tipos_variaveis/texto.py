# Declaração
nome_completo = "Natanael Roberto Rodrigues"

# aqui permite quebra de linhas
nome_completo_aspas = """Natanael 
                         Roberto Rodrigues  """

# nome completo com quebra com barras
nome_completo_quebra = "Natanael Roberto \
    Rodrigues"

nome = "Natanael Roberto"
sobrenome = "Rodrigues"



# Formatação
print("Nome compeleto (1a Forma):", nome_completo) # a concatenação com virgula, inclui um espaço entre o conteúdo informado
print("Nome compeleto (2a Forma):" + nome_completo)
print("Nome compeleto (3a Forma):" + "Natanael " + "Roberto " + "Rodrigues")
print("Nome compeleto (4a Forma):" , "Natanael" , "Roberto" , "Rodrigues")
print("Nome compeleto (5a Forma):" , nome_completo_aspas)
print("Nome compeleto (6a Forma):" , nome_completo_quebra)
print("Nome compeleto (7a Forma): %s." % nome_completo)
print("Nome compeleto (8a Forma): %s %s." % (nome, sobrenome)) # mais segura
print(f"Nome compeleto (9a Forma format): {nome} {sobrenome}.") # usando o format (f)
print("Nome compeleto (10a Forma format): {} {}.".format(nome, sobrenome)) # usando o format 

# Metodos em string

print("Metodo upper: ", nome.upper())
print("Metodo lower: ", nome.lower())
print("Primeira letra da variável nome: ", nome[0])
print("Metodo count 'a': ", nome.count("a"))
print("Metodo find: ", nome.find("a"))
print("Metodo encode para byte: ", nome.encode())
print("Metodo decode bype > texto: ", nome.encode().decode())
print("Metodo replace: ", nome.replace("a","4"))
print("Metodo join: ", "-".join("Natanael"))
print("Metodo split: ", nome_completo.split())
nome_sujo = "xNatanaelx"
print("Metodo strip: ", nome_sujo.strip("x")) # só retira no início e no fim da variável.
print("Metodo rstrip: ", nome_sujo.rstrip("x")) # só retira no fim.

# Comparadores
print(nome_completo.startswith("Nat"))
print("Roberto" in nome_completo ) # Se existe
print("Roberto" not in nome_completo ) # Se não existe


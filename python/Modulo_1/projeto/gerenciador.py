def adicionar_tarefa(tarefas, nome_tarefa):
  tarefa = {
    "tarefa": nome_tarefa,
    "completada": False
  }
  tarefas.append(tarefa)
  print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!")
  return

def ver_tarefas(tarefas):
  print("\nLista de tarefas:")
  for indice, tarefa in enumerate(tarefas, start=1):
    status = "✓" if tarefa["completada"] else " "
    print(f"{indice}. [{status}] {tarefa["tarefa"]}")
  return

def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
  indice = int(indice_tarefa) -1

  if indice  >= 0 and indice < len(tarefas):
    tarefas[indice]["tarefa"] = novo_nome_tarefa
    print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}")
  else:
    print("Indice de tarefa inválido.")
  return

def completar_tarefa(tarefas, indice_tarefa):
  indice = int(indice_tarefa) -1

  if indice  >= 0 and indice < len(tarefas):
    tarefas[indice]["completada"] = True
    print(f"Tarefa marcada {indice_tarefa} como completada")
  else:
    print("Indice de tarefa inválido.")
  return

tarefas = []

while True:
  print("\nMenu do Gerenciador de lista de Tarefas:")
  print("1. Adicionar uma tarefa")
  print("2. Ver tarefas")
  print("3. Atualizar tarefas")
  print("4. Completar tarefas")
  print("5. Deletar tarefas completadas")
  print("6. Sair")

  escolha = input("Digite a sua escolha:")
  if escolha == "1":
    nome_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")
    adicionar_tarefa(tarefas, nome_tarefa)
  elif escolha == "2":
    ver_tarefas(tarefas)
  elif escolha == "3":
    ver_tarefas(tarefas)
    indice_tarefa = input("Digite o número da tarefa que deseja atualizar:")
    novo_nome = input("Digite o nome nome da tarefa:")
    atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)
  elif escolha == "4":
    ver_tarefas(tarefas)
    indice_tarefa = input("Digite o número da tarefa que deseja completar:")
    completar_tarefa(tarefas, indice_tarefa)    
  elif escolha == "6":
    break

print("Programa finalizado...")
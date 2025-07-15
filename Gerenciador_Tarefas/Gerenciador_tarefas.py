def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {
        "nome": nome_tarefa, "completa": False
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{nome_tarefa}' foi adicionada com sucesso!")
    return

def ver_tarefas(tarefas):
    print("\n--- Tarefas Pendentes ---")
    if not tarefas:
        print("Nenhuma tarefa na lista.")
        return False 
    else:
        for i, tarefa in enumerate(tarefas, start=1):
            status = "✔️" if tarefa["completa"] else "❌"
            print(f"{i}. {tarefa['nome']} - {status}")
        return True 

def atualizar_tarefa(tarefas, indice, nova_tarefa):
    tarefas[indice]["nome"] = nova_tarefa
    print(f"Tarefa {indice + 1} atualizada para '{nova_tarefa}'.")
    return

def completar_tarefa(tarefas, indice):
    tarefas[indice]["completa"] = True
    print(f"Tarefa {indice + 1} marcada como completa.")
    return


def deletar_tarefas_completas(tarefas):
    
    tarefas_incompletas = [t for t in tarefas if not t["completa"]]
    
    if len(tarefas_incompletas) < len(tarefas):
        print("Todas as tarefas completas foram deletadas.")
        return tarefas_incompletas 
    else:
        print("Nenhuma tarefa completa para deletar.")
        return tarefas 

# --- Início do Programa ---
tarefas = [] 

while True:
    print("\nMenu do Gerenciador de Lista de Tarefas:")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar Tarefa")
    print("4. Completar Tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":    
        nome_tarefa = input("Digite a descrição da tarefa: ")
        adicionar_tarefa(tarefas, nome_tarefa)

    elif escolha == "2":
        ver_tarefas(tarefas)

    elif escolha == "3":
        if ver_tarefas(tarefas):
            try:
                num_tarefa = int(input("Digite o NÚMERO da tarefa a atualizar: "))
                indice = num_tarefa - 1
                
                if 0 <= indice < len(tarefas):
                    nova_tarefa = input("Digite a nova descrição da tarefa: ")
                    atualizar_tarefa(tarefas, indice, nova_tarefa)
                else:
                    print("Número de tarefa inválido.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

    elif escolha == "4":
        if ver_tarefas(tarefas):
            try:
                num_tarefa = int(input("Digite o NÚMERO da tarefa a completar: "))
                indice = num_tarefa - 1
                
                if 0 <= indice < len(tarefas):
                    completar_tarefa(tarefas, indice)
                else:
                    print("Número de tarefa inválido.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

    elif escolha == "5":
        tarefas = deletar_tarefas_completas(tarefas)

    elif escolha == "6":
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")

print("\nPrograma finalizado!")
'''
Elaborar um programa que efetue o gerenciamento dos dados de 10 registgros de uma agenda que contenha nomes, endereços e telefones, defina a estrutura de registro apropriada, o diagrama de blocos e a codigicacao de um  programa que, por meio de um menu de opçoes, execute as seguintes etapas:
    
    a) Cadastrar os 10 registros. 
    b) Pesquisar um registro de cada vez pelo campo nome(usar o método sequencial).
    c) Classificar por ondem de nome os registros cadastrados.
    d) Apresentar todos os registros.
    e)Sair do programa de cadastro.

'''
# ==========================================
# Agenda de Contatos
# ==========================================

agenda = []

# ------------------------------------------
# Cadastro dos 10 registros
# ------------------------------------------
def cadastrar():
    agenda.clear()

    print("\n=== CADASTRO DOS 10 REGISTROS ===")

    for i in range(10):
        print(f"\nRegistro {i + 1}")

        nome = input("Nome: ")
        endereco = input("Endereço: ")
        telefone = input("Telefone: ")

        registro = {
            "nome": nome,
            "endereco": endereco,
            "telefone": telefone
        }

        agenda.append(registro)

    print("\nCadastro realizado com sucesso!\n")


# ------------------------------------------
# Pesquisa sequencial pelo nome
# ------------------------------------------
def pesquisar():
    if len(agenda) == 0:
        print("\nNenhum registro cadastrado.\n")
        return

    nome = input("\nDigite o nome para pesquisar: ")

    encontrado = False

    for registro in agenda:   # Busca Sequencial
        if registro["nome"].lower() == nome.lower():
            print("\nRegistro encontrado:")
            print(f"Nome: {registro['nome']}")
            print(f"Endereço: {registro['endereco']}")
            print(f"Telefone: {registro['telefone']}")
            encontrado = True
            break

    if not encontrado:
        print("\nRegistro não encontrado.")


# ------------------------------------------
# Classificação em ordem alfabética
# ------------------------------------------
def classificar():
    if len(agenda) == 0:
        print("\nNenhum registro cadastrado.\n")
        return

    agenda.sort(key=lambda registro: registro["nome"].lower())

    print("\nRegistros classificados com sucesso!\n")


# ------------------------------------------
# Apresentação dos registros
# ------------------------------------------
def apresentar():
    if len(agenda) == 0:
        print("\nNenhum registro cadastrado.\n")
        return

    print("\n========== AGENDA ==========")

    for i, registro in enumerate(agenda, start=1):
        print(f"\nRegistro {i}")
        print(f"Nome      : {registro['nome']}")
        print(f"Endereço  : {registro['endereco']}")
        print(f"Telefone  : {registro['telefone']}")

    print()


# ------------------------------------------
# Programa Principal
# ------------------------------------------
while True:

    print("========== MENU ==========")
    print("1 - Cadastrar os 10 registros")
    print("2 - Pesquisar por nome")
    print("3 - Classificar por nome")
    print("4 - Apresentar todos os registros")
    print("5 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        cadastrar()

    elif opcao == "2":
        pesquisar()

    elif opcao == "3":
        classificar()

    elif opcao == "4":
        apresentar()

    elif opcao == "5":
        print("\nPrograma encerrado.")
        break

    else:
        print("\nOpção inválida!\n") 
        
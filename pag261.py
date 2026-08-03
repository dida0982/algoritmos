'''
Elaborar um programa que efetue o gerenciamento dos dados de 10 registgros de uma agenda que contenha nomes, endereços e telefones, defina a estrutura de registro apropriada, o diagrama de blocos e a codigicacao de um  programa que, por meio de um menu de opçoes, execute as seguintes etapas:
    
    a) Cadastrar os 10 registros. 
    b) Pesquisar um registro de cada vez pelo campo nome(usar o método sequencial).
    c) Classificar por ondem de nome os registros cadastrados.
    d) Apresentar todos os registros.
    e)Sair do programa de cadastro.

'''

import random

# ----------------------------
# Dados para gerar a agenda
# ----------------------------
nomes = [
    "Guilherme", "Maria", "João", "Pedro", "Ana",
    "Carlos", "Fernanda", "Lucas", "Juliana", "Rafael"
]

enderecos = [
    "Brasília", "Goiânia", "Anápolis", "Valparaíso",
    "Luziânia", "Taguatinga", "Ceilândia",
    "Samambaia", "Sobradinho", "Planaltina"
]

telefones = [
    "61999990001", "61999990002", "61999990003",
    "61999990004", "61999990005", "61999990006",
    "61999990007", "61999990008", "61999990009",
    "61999990010"
]

agenda = []

# =====================================
# ALTERNATIVA A
# Cadastrar os 10 registros
# =====================================

for i in range(10):

    registro = {
        "nome": random.choice(nomes),
        "endereco": random.choice(enderecos),
        "telefone": random.choice(telefones)
    }

    agenda.append(registro)
    agenda.sort(key=lambda registro: registro["nome"].lower())

print("Agenda cadastrada!\n")

for registro in agenda:
    print(registro)

# =====================================
# ALTERNATIVA B
# Pesquisa Sequencial por Nome
# =====================================

nome_procurado = input("\nDigite o nome que deseja pesquisar: ")

encontrou = False

for registro in agenda:

    if registro["nome"] == nome_procurado:

        print("\nRegistro encontrado!\n")
        print("Nome:", registro["nome"])
        print("Endereço:", registro["endereco"])
        print("Telefone:", registro["telefone"])

        encontrou = True
        break

if encontrou == False:
    print("\nRegistro não encontrado.")
    
    
    print("\n=== AGENDA ===\n")

for registro in agenda:
    print(f"Nome: {registro['nome']}")
    print(f"Endereço: {registro['endereco']}")
    print(f"Telefone: {registro['telefone']}")
    print("-" * 30)

print("\nPrograma encerrado.")
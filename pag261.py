"""
Elaborar um programa que efetue o gerenciamento dos dados de 10 registros
de uma agenda contendo nomes, endereços e telefones.

a) Cadastrar os 10 registros.
b) Pesquisar um registro pelo nome (busca sequencial).
c) Classificar os registros por ordem alfabética do nome.
d) Apresentar todos os registros.
e) Sair do programa.
"""

import random

# Dados para gerar os registros

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
# Alternativa A - Cadastrar os registros
# =====================================

for i in range(10):

    registro = {
        "nome": random.choice(nomes),
        "endereco": random.choice(enderecos),
        "telefone": random.choice(telefones)
    }

    agenda.append(registro)

print("\nAgenda cadastrada com sucesso!\n")

# =====================================
# Alternativa B - Pesquisa Sequencial
# =====================================

nome_procurado = input("Digite o nome que deseja pesquisar: ").strip()

encontrou = False

for registro in agenda:

    if registro["nome"].lower() == nome_procurado.lower():

        print("\nRegistro encontrado!\n")
        print("Nome:", registro["nome"])
        print("Endereço:", registro["endereco"])
        print("Telefone:", registro["telefone"])

        encontrou = True
        break

if not encontrou:
    print("\nRegistro não encontrado.")

# =====================================
# Alternativa C - Classificar por nome
# =====================================

agenda.sort(key=lambda registro: registro["nome"].lower())

print("\nAgenda classificada com sucesso!")

# =====================================
# Alternativa D - Apresentar registros
# =====================================

print("\n========== AGENDA ==========\n")

for registro in agenda:
    print(f"Nome: {registro['nome']}")
    print(f"Endereço: {registro['endereco']}")
    print(f"Telefone: {registro['telefone']}")
    print("-" * 30)

# =====================================
# Alternativa E - Encerrar programa
# =====================================

print("\nPrograma encerrado.")
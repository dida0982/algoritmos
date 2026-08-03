import random


nomes = [
    "Guilherme", "Maria", "João", "Pedro", "Ana",
    "Carlos", "Fernanda", "Lucas", "Juliana", "Rafael",
    "Bruno", "Camila", "Diego", "Eduarda", "Felipe",
    "Gabriela", "Henrique", "Isabela", "Leonardo", "Natália"
]

notas = [
    0.0, 0.5, 1.0, 1.5, 2.0, 2.5,
    3.0, 3.5, 4.0, 4.5, 5.0, 5.5,
    6.0, 6.5, 7.0, 7.5, 8.0, 8.5,
    9.0, 9.5, 10.0
]

alunos = []


def mostrar_aluno(aluno):
    print(f"Nome: {aluno['nome']}")
    print(f"1º Bimestre: {aluno['1_bimestre']}")
    print(f"2º Bimestre: {aluno['2_bimestre']}")
    print(f"3º Bimestre: {aluno['3_bimestre']}")
    print(f"4º Bimestre: {aluno['4_bimestre']}")
    print("-" * 30)


# Cadastro dos alunos

for i in range(20):

    aluno = {
        "nome": random.choice(nomes),
        "1_bimestre": random.choice(notas),
        "2_bimestre": random.choice(notas),
        "3_bimestre": random.choice(notas),
        "4_bimestre": random.choice(notas)
    }

    alunos.append(aluno)


print("\n=== ALUNOS CADASTRADOS ===\n")

for aluno in alunos:
    mostrar_aluno(aluno)


# Pesquisa

nome_procurado = input("\nDigite o nome que deseja pesquisar: ").strip()

encontrou = False

for aluno in alunos:

    if aluno["nome"].lower() == nome_procurado.lower():

        print("\nAluno encontrado!\n")
        mostrar_aluno(aluno)

        encontrou = True
        break

if not encontrou:
    print("\nAluno não encontrado.")


# Classificação

alunos.sort(key=lambda aluno: aluno["nome"].lower())

print("\n=== ALUNOS ORDENADOS ===\n")

for aluno in alunos:
    mostrar_aluno(aluno)


print("\nPrograma encerrado.")
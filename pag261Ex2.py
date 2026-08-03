import random

# Nomes dos alunos

nomes = [
    "Guilherme", "Maria", "João", "Pedro", "Ana",
    "Carlos", "Fernanda", "Lucas", "Juliana", "Rafael",
    "Bruno", "Camila", "Diego", "Eduarda", "Felipe",
    "Gabriela", "Henrique", "Isabela", "Leonardo", "Natália"
]

# Notas possíveis (0.0 a 10.0)

notas = [
    0.0, 0.5, 1.0, 1.5, 2.0, 2.5,
    3.0, 3.5, 4.0, 4.5, 5.0, 5.5,
    6.0, 6.5, 7.0, 7.5, 8.0, 8.5,
    9.0, 9.5, 10.0
]

alunos = []

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
    print(aluno)
    
nome_procurado = input("Digite o nome que deseja pesquisar: ").strip()

encontrou = False

for aluno in alunos:

    if aluno["nome"].lower() == nome_procurado.lower():

        print("\aluno encontrado!\n")
        print("Nome:", aluno["nome"])
        print("1_bimestre:", aluno["1_bimestre"])
        print("2_bimestre:", aluno["2_bimestre"])
        print("3_bimestre:", aluno["3_bimestre"])
        print("4_bimestre:", aluno["4_bimestre"])

        encontrou = True
        break

if not encontrou:
    print("\nRegistro não encontrado.")
    
alunos.sort(key=lambda registro: registro["nome"].lower())

print("\nAgenda classificada com sucesso!")

print("\n========== AGENDA ==========\n")

for alunos in alunos:
    print("Nome:", aluno["nome"])
    print("1_bimestre:", aluno["1_bimestre"])
    print("2_bimestre:", aluno["2_bimestre"])
    print("3_bimestre:", aluno["3_bimestre"])
    print("4_bimestre:", aluno["4_bimestre"])
    print("-" * 30)
    
print("\nPrograma encerrado.")
    
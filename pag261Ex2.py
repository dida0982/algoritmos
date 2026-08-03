import random

nomes = [
    "Guilherme", "Maria", "João", "Pedro", "Ana",
    "Carlos", "Fernanda", "Lucas", "Juliana", "Rafael",
    "Bruno", "Camila", "Diego", "Eduarda", "Felipe",
    "Gabriela", "Henrique", "Isabela", "Leonardo", "Natália"
]

notas = [i * 0.5 for i in range(21)]  # gera de 0.0 até 10.0

alunos = []

def mostrar_aluno(aluno):
    print(f"Nome: {aluno['nome']}")
    print(f"1º Bimestre: {aluno['1_bimestre']}")
    print(f"2º Bimestre: {aluno['2_bimestre']}")
    print(f"3º Bimestre: {aluno['3_bimestre']}")
    print(f"4º Bimestre: {aluno['4_bimestre']}")
    media = (aluno['1_bimestre'] + aluno['2_bimestre'] + aluno['3_bimestre'] + aluno['4_bimestre']) / 4 
    print(f"Média: {media:.2f}")
    print("Situação:", "APROVADO ✅" if media >= 5 else "REPROVADO ❌")
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

# Ordenação para pesquisa binária
alunos.sort(key=lambda aluno: aluno["nome"].lower())

print("\n=== ALUNOS ORDENADOS ===\n")
for aluno in alunos:
    mostrar_aluno(aluno)

# Pesquisa binária
def pesquisa_binaria(lista, nome):
    inicio, fim = 0, len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio]["nome"].lower() == nome.lower():
            return lista[meio]
        elif lista[meio]["nome"].lower() < nome.lower():
            inicio = meio + 1
        else:
            fim = meio - 1
    return None

nome_procurado = input("\nDigite o nome que deseja pesquisar: ").strip()
aluno_encontrado = pesquisa_binaria(alunos, nome_procurado)

if aluno_encontrado:
    print("\nAluno encontrado!\n")
    mostrar_aluno(aluno_encontrado)
else:
    print("\nAluno não encontrado.")

print("\nPrograma encerrado.")

# PROGRAMA DADOS_HETEROGENEOS_V1

# Declaração das listas (equivalente ao CONJUNTO [1..3])
nomes = []
idades = []
alturas = []

# PRIMEIRO LAÇO: Leitura dos dados (Executa 3 vezes)
print("=== ENTRADA DE DADOS ===")
for i in range(3):
    print(f"\nCadastro {i + 1}:")
    nome = input("Digite o nome: ").strip()
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura (ex: 1.75): "))
    
    # Adiciona os valores nas respectivas listas
    nomes.append(nome)
    idades.append(idade)
    alturas.append(altura)

# SEGUNDO LAÇO: Escrita dos dados (Executa 3 vezes)
print("\n=== SAÍDA DE DADOS ===")
for i in range(3):
    print(f"\nRegistro {i + 1}:")
    print(f"Nome: {nomes[i]}")
    print(f"Idade: {idades[i]}")
    print(f"Altura: {alturas[i]:.2f}m")

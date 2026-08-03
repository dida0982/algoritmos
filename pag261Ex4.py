# 1. Listas de dados (Agora ambas possuem exatamente 20 elementos)
nomes = [
    'Ana', 'Bruno', 'Camila', 'Diego', 'Eduarda',
    'Felipe', 'Gabriela', 'Henrique', 'Isabela', 'João',
    'Juliana', 'Leonardo', 'Lucas', 'Maria', 'Natália',
    'Pedro', 'Rafael', 'Sophia', 'Thiago', 'Vinícius'
]

alturas = [
    1.65, 1.78, 1.82, 1.60, 1.72,
    1.89, 1.55, 1.68, 1.75, 1.80,
    1.63, 1.70, 1.85, 1.58, 1.74,
    1.69, 1.71, 1.92, 1.60, 1.81  # Adicionados 5 valores para igualar os 20 nomes
]

# Ordenação conjunta por ordem alfabética do nome
dados_juntos = zip(nomes, alturas)
dados_ordenados = sorted(dados_juntos)

nomes = [item[0] for item in dados_ordenados]
alturas = [item[1] for item in dados_ordenados]

while True:
    print("\n" + "="*45)
    print("              SISTEMA DE ALTURAS")
    print("="*45)
    print("1. Pessoas com menos de 1.65m")
    print("2. Pessoas com 1.65m até 1.79m")
    print("3. Pessoas com 1.80m ou mais")
    print("4. Apresentar a média de todas as alturas")
    print("0. Sair do programa")
    print("="*45)
    
    opcao = input("Escolha uma opção: ").strip()
    
    if opcao == '1':
        print("\n=== PESSOAS COM MENOS DE 1.65m ===")
        print(f"{'NOME':<25} | {'ALTURA'}")
        print("-" * 45)
        for i, nome in enumerate(nomes):
            if alturas[i] < 1.65:
                print(f"{nome:<25} | {alturas[i]:.2f}m")
                
    elif opcao == '2':
        print("\n=== PESSOAS COM 1.65m ATÉ 1.79m ===")
        print(f"{'NOME':<25} | {'ALTURA'}")
        print("-" * 45)
        for i, nome in enumerate(nomes):
            if 1.65 <= alturas[i] <= 1.79:
                print(f"{nome:<25} | {alturas[i]:.2f}m")
                
    elif opcao == '3':
        print("\n=== PESSOAS COM 1.80m OU MAIS ===")
        print(f"{'NOME':<25} | {'ALTURA'}")
        print("-" * 45)
        for i, nome in enumerate(nomes):
            if alturas[i] >= 1.80:
                print(f"{nome:<25} | {alturas[i]:.2f}m")
                
    elif opcao == '4':
        print("\n=== MÉDIA DAS ALTURAS ===")
        # sum() soma todos os valores da lista e len() conta o total de pessoas
        media = sum(alturas) / len(alturas)
        print(f"A média de altura do grupo é: {media:.2f}m")
        
    elif opcao == '0':
        print("\nEncerrando o programa. Até mais!")
        break
        
    else:
        print("\nOpção inválida! Escolha de 0 a 4.")

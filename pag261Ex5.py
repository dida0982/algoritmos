nomes = [
    'Ana Beatriz', 'Bruno César', 'Camila Rocha', 'Diego Nunes', 'Eduarda Ramos',
    'Felipe Duarte', 'Gabriela Torres', 'Henrique Lopes', 'Isabela Barros', 'João Pereira',
    'Juliana Costa', 'Leonardo Pinto', 'Lucas Almeida', 'Maria Souza', 'Natália Ribeiro',
    'Pedro Santos', 'Rafael Martins', 'Sophia Mendes', 'Thiago Lima', 'Vinícius Oliveira'
]

salarios = [
    3200.50, 4500.00, 2800.00, 6100.80, 3900.00,
    5200.00, 7500.30, 3100.00, 4200.50, 2900.00,
    4800.00, 5900.90, 3600.00, 8200.00, 4100.40,
    3300.00, 5000.00, 6800.20, 3700.00, 5400.60
]

matriculas = [
    '1001', '1002', '1003', '1004', '1005',
    '1006', '1007', '1008', '1009', '1010',
    '1011', '1012', '1013', '1014', '1015',
    '1016', '1017', '1018', '1019', '1020'
]

# Ordenação conjunta por ordem alfabética do nome (essencial para a busca binária por nome)
dados_juntos = zip(nomes, salarios, matriculas)
dados_ordenados = sorted(dados_juntos)

nomes = [item[0] for item in dados_ordenados]
salarios = [item[1] for item in dados_ordenados]
matriculas = [item[2] for item in dados_ordenados]

while True:
    print("\n" + "="*45)
    print("         SISTEMA DE RH E SALÁRIOS")
    print("="*45)
    print("1. Listar todas as matrículas e dados")
    print("2. Pesquisar salário por Nome (Método Binário)")
    print("3. Salários ACIMA de R$ 5.000,00")
    print("4. Salários ABAIXO de R$ 5.000,00")
    print("5. Salários IGUAIS a R$ 5.000,00")
    print("0. Sair do programa")
    print("="*45)
    
    opcao = input("Escolha uma opção: ").strip()
    
    if opcao == '1':
        print("\n=== LISTA GERAL DE FUNCIONÁRIOS ===")
        print(f"{'MATRÍCULA':<10} | {'NOME':<20} | {'SALÁRIO'}")
        print("-" * 50)
        for i in range(len(nomes)):
            print(f"{matriculas[i]:<10} | {nomes[i]:<20} | R$ {salarios[i]:,.2f}")
            
    elif opcao == '2':
        print("\n=== BUSCA BINÁRIA POR NOME ===")
        nome_procurado = input("Digite o nome EXATO do funcionário: ").strip()
        
        esquerda = 0
        direita = len(nomes) - 1
        indice_encontrado = -1
        
        # Algoritmo de Busca Binária baseado no vetor ordenado de nomes
        while esquerda <= direita:
            meio = (esquerda + direita) // 2
            if nomes[meio].lower() == nome_procurado.lower():
                indice_encontrado = meio
                break
            elif nomes[meio].lower() < nome_procurado.lower():
                esquerda = meio + 1
            else:
                direita = meio - 1
                
        if indice_encontrado != -1:
            i = indice_encontrado
            print(f"\nFuncionário encontrado!")
            print(f"Nome: {nomes[i]} | Matrícula: {matriculas[i]}")
            print(f"Salário atual: R$ {salarios[i]:,.2f}")
        else:
            print(f"O funcionário '{nome_procurado}' não foi encontrado.")
            
    elif opcao == '3':
        print("\n=== SALÁRIOS ACIMA DE R$ 5.000,00 ===")
        print(f"{'NOME':<20} | {'SALÁRIO'}")
        print("-" * 35)
        for i in range(len(nomes)):
            if salarios[i] > 5000.00:
                print(f"{nomes[i]:<20} | R$ {salarios[i]:,.2f}")
                
    elif opcao == '4':
        print("\n=== SALÁRIOS ABAIXO DE R$ 5.000,00 ===")
        print(f"{'NOME':<20} | {'SALÁRIO'}")
        print("-" * 35)
        for i in range(len(nomes)):
            if salarios[i] < 5000.00:
                print(f"{nomes[i]:<20} | R$ {salarios[i]:,.2f}")
                
    elif opcao == '5':
        print("\n=== SALÁRIOS IGUAIS A R$ 5.000,00 ===")
        print(f"{'NOME':<20} | {'SALÁRIO'}")
        print("-" * 35)
        encontrou_algum = False
        for i in range(len(nomes)):
            if salarios[i] == 5000.00:
                print(f"{nomes[i]:<20} | R$ {salarios[i]:,.2f}")
                encontrou_algum = True
        if not encontrou_algum:
            print("Nenhum funcionário recebe exatamente R$ 5.000,00.")
            
    elif opcao == '0':
        print("\nEncerrando o sistema de RH. Até logo!")
        break
    else:
        print("\nOpção inválida! Escolha de 0 a 5.")

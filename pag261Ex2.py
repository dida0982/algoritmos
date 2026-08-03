# Listas de dados iniciais
nomes_alunos = [
    'Ana Beatriz', 'Bruno César', 'Camila Rocha', 'Diego Nunes', 'Eduarda Ramos',
    'Felipe Duarte', 'Gabriela Torres', 'Henrique Lopes', 'Isabela Barros', 'João Pereira',
    'Juliana Costa', 'Leonardo Pinto', 'Lucas Almeida', 'Maria Souza', 'Natália Ribeiro',
    'Pedro Santos', 'Rafael Martins', 'Sophia Mendes', 'Thiago Lima', 'Vinícius Oliveira'
]

notas_1_bimestre = [
    8.5, 7.0, 9.2, 6.4, 8.0, 5.5, 9.8, 7.3, 8.8, 6.0,
    7.5, 8.2, 6.9, 9.0, 8.4, 7.8, 5.0, 9.5, 6.2, 7.7
]

notas_2_bimestre = [
    7.8, 6.5, 9.0, 7.2, 8.5, 6.0, 9.5, 8.0, 8.2, 6.8,
    8.0, 7.9, 7.1, 9.3, 8.0, 8.2, 5.8, 9.7, 6.5, 7.0
]

notas_3_bimestre = [
    8.2, 7.2, 9.5, 6.8, 8.8, 6.5, 10.0, 7.8, 8.5, 7.0,
    8.3, 8.5, 7.5, 9.1, 8.7, 8.0, 6.2, 9.6, 7.0, 7.5
]

# Ordenação conjunta inicial (obrigatória para a Busca Binária)
dados_juntos = zip(nomes_alunos, notas_1_bimestre, notas_2_bimestre, notas_3_bimestre)
dados_ordenados = sorted(dados_juntos)

nomes_alunos = [item[0] for item in dados_ordenados]
notas_1_bimestre = [item[1] for item in dados_ordenados]
notas_2_bimestre = [item[2] for item in dados_ordenados]
notas_3_bimestre = [item[3] for item in dados_ordenados]

while True:
    print("\n" + "="*45)
    print("              SISTEMA ESCOLAR v3")
    print("="*45)
    print("1. Listar todos os alunos (Dados básicos)")
    print("2. Pesquisar aluno (Busca Binária)")
    print("3. Ver Médias e Situações (Aprovado/Reprovado)")
    print("0. Sair do programa")
    print("="*45)
    
    opcao = input("Escolha uma opção: ").strip()
    
    if opcao == '1':
        print("\n=== LISTA DE ALUNOS EM ORDEM ALFABÉTICA ===")
        for i, nome in enumerate(nomes_alunos):
            print(f"Nome: {nome}")
            print(f"Notas: 1ºB: {notas_1_bimestre[i]} | 2ºB: {notas_2_bimestre[i]} | 3ºB: {notas_3_bimestre[i]}")
            print("-" * 45)
            
    elif opcao == '2':
        print("\n=== PESQUISAR ALUNO (BUSCA BINÁRIA) ===")
        nome_procurado = input("Digite o nome EXATO do aluno: ").strip()
        
        esquerda = 0
        direita = len(nomes_alunos) - 1
        indice_encontrado = -1
        
        while esquerda <= direita:
            meio = (esquerda + direita) // 2
            
            if nomes_alunos[meio].lower() == nome_procurado.lower():
                indice_encontrado = meio
                break
            elif nomes_alunos[meio].lower() < nome_procurado.lower():
                esquerda = meio + 1
            else:
                direita = meio - 1
                
        if indice_encontrado != -1:
            i = indice_encontrado
            media = (notas_1_bimestre[i] + notas_2_bimestre[i] + notas_3_bimestre[i]) / 3
            situacao = "REPROVADO" if media < 5 else "APROVADO"
                
            print(f"\nSucesso! Aluno encontrado no índice {i}:")
            print(f"Nome: {nomes_alunos[i]}")
            print(f"Notas: 1ºB: {notas_1_bimestre[i]} | 2ºB: {notas_2_bimestre[i]} | 3ºB: {notas_3_bimestre[i]}")
            print(f"Média Parcial: {media:.1f}")
            print(f"Situação: {situacao}")
        else:
            print(f"O aluno '{nome_procurado}' não foi encontrado.")
            
    elif opcao == '3':
        print("\n=== RELATÓRIO DE MÉDIAS E SITUAÇÕES ===")
        print(f"{'ALUNO':<20} | {'MÉDIA':<6} | {'SITUAÇÃO'}")
        print("-" * 45)
        
        for i, nome in enumerate(nomes_alunos):
            # Calcula a média do aluno atual
            media = (notas_1_bimestre[i] + notas_2_bimestre[i] + notas_3_bimestre[i]) / 3
            
            # Define a mensagem com base na nota menor que 5
            situacao = "REPROVADO" if media < 5 else "APROVADO"
            
            # Exibe os dados formatados em colunas alinhadas
            print(f"{nome:<20} | {media:<6.1f} | {situacao}")
            
    elif opcao == '0':
        print("\nEncerrando o sistema. Até logo!")
        break
    else:
        print("\nOpção inválida! Por favor, digite 1, 2, 3 ou 0.")

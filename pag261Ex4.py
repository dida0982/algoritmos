nomes = [
    'Ana Beatriz', 'Bruno César', 'Camila Rocha', 'Diego Nunes', 'Eduarda Ramos',
    'Felipe Duarte', 'Gabriela Torres', 'Henrique Lopes', 'Isabela Barros', 'João Pereira',
    'Juliana Costa', 'Leonardo Pinto', 'Lucas Almeida', 'Maria Souza', 'Natália Ribeiro',
    'Pedro Santos', 'Rafael Martins', 'Sophia Mendes', 'Thiago Lima', 'Vinícius Oliveira'
]

alturas = [
    1.65, 1.78, 1.82, 1.60, 1.72,
    1.89, 1.55, 1.68, 1.75, 1.80,
    1.63, 1.70, 1.85, 1.58, 1.74
]

dados_juntos = zip(nomes, alturas)
dados_ordenados = sorted(dados_juntos)

nomes = [item[0] for item in dados_ordenados]
alturas = [item[1] for item in dados_ordenados]


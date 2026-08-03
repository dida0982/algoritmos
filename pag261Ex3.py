nomes = [
    'Guilherme',  'Maria', 'João', 'Pedro', 'Ana',
    'Carlos', 'Fernanda', 'Lucas', 'Juliana', 'Rafael',
    'Bruno', 'Camila', 'Diego ', 'Eduarda ', 'Felipe ',
    'Gabriela', 'Henrique', 'Isabela' , 'Leonardo', 'Natália'
]

telefones = [
    '(61) 91234-5678', '(11) 99876-5432', '(21) 98765-4321', '(31) 97654-3210', '(41) 96543-2109',
    '(51) 95432-1098', '(81) 94321-0987', '(11) 93210-9876', '(71) 92109-8765', '(85) 91098-7654',
    '(62) 90987-6543', '(92) 89876-5432', '(91) 88765-4321', '(48) 87654-3210', '(27) 86543-2109',
    '(84) 85432-1098', '(67) 84321-0987', '(86) 83210-9876', '(82) 82109-8765', '(61) 81098-7654'
]

enderecos = [
    'Rua das Flores 123 - Brasília/DF', 'Av. Central 456 - São Paulo/SP', 'Rua das Palmeiras 789 - Rio de Janeiro/RJ',
    'Rua do Sol 321 - Belo Horizonte/MG', 'Av. Brasil 654 - Curitiba/PR', 'Rua das Acácias 987 - Porto Alegre/RS',
    'Rua das Hortênsias 147 - Recife/PE', 'Av. Paulista 258 - São Paulo/SP', 'Rua das Orquídeas 369 - Salvador/BA',
    'Rua das Laranjeiras 741 - Fortaleza/CE', 'Av. Independência 852 - Goiânia/GO', 'Rua das Violetas 963 - Manaus/AM',
    'Rua das Mangueiras 159 - Belém/PA', 'Av. Atlântica 753 - Florianópolis/SC', 'Rua das Oliveiras 357 - Vitória/ES',
    'Rua das Amendoeiras 951 - Natal/RN', 'Av. Amazonas 258 - Campo Grande/MS', 'Rua das Bromélias 654 - Teresina/PI',
    'Rua das Jacarandás 852 - Maceió/AL', 'Av. das Nações 147 - Brasília/DF'
]


dados_juntos = zip(nomes, telefones, enderecos)
dados_ordenados = sorted(dados_juntos)

nomes = [item[0].strip() for item in dados_ordenados]
telefones = [item[1] for item in dados_ordenados]
enderecos = [item[2] for item in dados_ordenados]



print(f"\nPesquisar")
nome_procurado = input("Qual nome vc procura?").strip()

encontrado = False 

for indice, nome in enumerate(nomes):
    if nome.lower() == nome_procurado.lower():
        print(f"Sucesso! Nome encontrado!")
        print(f"Nome: {nome}")
        print(f"Telefone: {telefones[indice]}")
        print(f"Endereço: {enderecos[indice]}")
        encontrado = True
        break
    
if not encontrado:
    print(f"O nome '{nome_procurado}' não está na lista.")
    
print(f"Presente todos os registros {}")
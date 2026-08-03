'''
Elaborar um programa que efetue o gerenciamento dos dados de 10 registgros de uma agenda que contenha nomes, endereços e telefones, defina a estrutura de registro apropriada, o diagrama de blocos e a codigicacao de um  programa que, por meio de um menu de opçoes, execute as seguintes etapas:
    
    a) Cadastrar os 10 registros. 
    b) Pesquisar um registro de cada vez pelo campo nome(usar o método sequencial).
    c) Classificar por ondem de nome os registros cadastrados.
    d) Apresentar todos os registros.
    e)Sair do programa de cadastro.

'''

agenda = []

for i in range(10):
    print(f"\nCadastro {i + 1}")

    nome = input("Nome: ")
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")

    registro = {
        "nome": nome,
        "endereco": endereco,
        "telefone": telefone
    }

    agenda.append(registro)

print("\nCadastro concluído!")
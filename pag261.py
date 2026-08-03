'''
Elaborar um programa que efetue o gerenciamento dos dados de 10 registgros de uma agenda que contenha nomes, endereços e telefones, defina a estrutura de registro apropriada, o diagrama de blocos e a codigicacao de um  programa que, por meio de um menu de opçoes, execute as seguintes etapas:
    
    a) Cadastrar os 10 registros. 
    b) Pesquisar um registro de cada vez pelo campo nome(usar o método sequencial).
    c) Classificar por ondem de nome os registros cadastrados.
    d) Apresentar todos os registros.
    e)Sair do programa de cadastro.

'''

#empty list.
agenda = []

for i in range(10):
    print(f"Register {i + 1}")
    
    name = input("Name: ")
    address = input("Address: ")
    phone = input("Phone: ")
    
    register= {
        "name": name,
        "address": address,
        "phone": phone
    }
    
    agenda.append(register)
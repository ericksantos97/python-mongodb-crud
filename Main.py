import pymongo
from bson import ObjectId

from Cliente import Cliente

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["projeto_mongodb_python"]
col_cliente = mydb["cliente"]
col_produto = mydb["fornecedor"]
col_funcionario = mydb["lanchonete"]


def mensagem_erro():
    print('\nOcorreu um problema na aplicação, tente novamente.')


def mensagem_nenhum_registro(param):
    print('\nNenhum', param, 'encontrado.')


# Metodos do Cliente

def inserir_cliente(cliente):
    result = col_cliente.insert_one(cliente.__dict__)
    if result.inserted_id:
        print(f'\nO cliente {cliente.get_nome()} foi inserido com sucesso.')


def preencher_cliente():
    cliente = Cliente()
    cliente.set_nome(input('\nInforme o nome: '))
    cliente.set_telefone(input('\nInforme o telefone: '))
    cliente.set_endereco(input('\nInforme o endereco: '))
    cliente.set_cidade(input('\nInforme a cidade: '))
    cliente.set_estado(input('\nInforme o estado: '))
    cliente.set_data_nascimento(input('\nInforme a data de nascimento: '))
    cliente.set_email(input('\nInforme o email: '))
    return cliente


def excluir_cliente(id_cliente):
    col_cliente.delete_one({"_id": ObjectId(id_cliente)})
    print("Cliente excluído com sucesso!")


def atualizar_cliente(id_cliente, cliente):
    result = col_cliente.update_one({'_id': id_cliente}, {"$set": cliente.__dict__})
    if result.modified_count > 0:
        print(f'\nO cliente {cliente.get_nome()} foi alterado com sucesso.')


def listar_clientes():
    if col_cliente.estimated_document_count() > 0:
        for cliente in col_cliente.find():
            print("\nID: ", cliente["_id"], "\nNome: ", cliente["nome"], "\nTelefone: ", cliente["telefone"],
                  "\nEndereço: ", cliente["endereco"], "\nCidade: ", cliente["cidade"], "\nEstado: ",
                  cliente["estado"],
                  "\nData Nascimento: ", cliente["data_nascimento"], "\nEmail: ", cliente["email"])
    else:
        print("Não existem clientes cadastrados no banco de dados")


# Metodos do Fornecedor

def inserir_fornecedor(fornecedor):
    result = col_fornecedor.insert_one(fornecedor.__dict__)
    if result.inserted_id:
        print(f'\nO funcionario {fornecedor.get_nome()} foi inserido com sucesso.')


# Metodos da Lanchonete

def inserir_lanchonete(lanchonete):
    result = col_lanchonete.insert_one(lanchonete.__dict__)
    if result.inserted_id:
        print(f'\nO produto {lanchonete.get_descricao()} foi inserido com sucesso.')


continuar = True

while continuar:
    print('\n---------- Menu Cliente ---------- ')
    print('\n1 - Inserir cliente')
    print('\n2 - Listar clientes')
    print('\n3 - Excluir cliente')
    print('\n4 - Alterar cliente')
    print('\n---------- Menu Fornecedor ---------- ')
    print('\n1 - Inserir fornecedor')
    print('\n2 - Listar fornecedores')
    print('\n3 - Excluir fornecedor')
    print('\n4 - Alterar fornecedor')
    print('\n---------- Menu Lanchonete ---------- ')
    print('\n1 - Inserir lanchonete')
    print('\n2 - Listar lanchonetes')
    print('\n3 - Excluir lanchonete')
    print('\n4 - Alterar lanchonete')
    print('\n0 - Sair do sistema')

    opcao = input('\nInforme a opção desejada: ')

    if opcao == '1':
        try:
            print("\n====================Adicionar Cliente====================")
            inserir_cliente(preencher_cliente())
        except:
            mensagem_erro()

    elif opcao == '2':
        try:
            print("\n====================Lista de Clientes====================")
            listar_clientes()
        except:
            mensagem_erro()

    elif opcao == '3':
        try:
            print("\n=====================Excluir Cliente=====================")
            id_cliente = str(input("\nInforme o id do Cliente: "))
            excluir_cliente(id_cliente)
        except:
            mensagem_erro()

    elif opcao == '4':
        print("\n=====================Alterar Cliente=====================")
        id_cliente = str(input("\nInforme o id do Cliente: "))
        atualizar_cliente(id_cliente, preencher_cliente())

    elif opcao == '0':
        continuar = False

    else:
        print('\nOpção inválida.')

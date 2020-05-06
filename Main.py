import pymongo
from bson import ObjectId

from Cliente import Cliente
from Fornecedor import Fornecedor
from Lanchonete import Lanchonete

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["projeto_mongodb_python"]
col_cliente = mydb["cliente"]
col_fornecedor = mydb["fornecedor"]
col_lanchonete = mydb["lanchonete"]


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
                  "\nEndereço: ", cliente["endereco"], "\nCidade: ", cliente["cidade"], "\nEstado: ", cliente["estado"],
                  "\nData Nascimento: ", cliente["data_nascimento"], "\nEmail: ", cliente["email"])
    else:
        print("Não existem clientes cadastrados no banco de dados")


# Metodos do Fornecedor

def inserir_fornecedor(fornecedor):
    result = col_fornecedor.insert_one(fornecedor.__dict__)
    if result.inserted_id:
        print(f'\nO funcionario {fornecedor.get_nome()} foi inserido com sucesso.')


def preencher_fornecedor():
    fornecedor = Fornecedor()
    fornecedor.set_nome(input('\nInforme o nome: '))
    fornecedor.set_telefone(input('\nInforme o telefone: '))
    fornecedor.set_nome_produto_venda(input('\nInforme o nome do produto venda: '))
    fornecedor.set_segmento_produto(input('\nInforme o segmento do produto: '))
    fornecedor.set_gasto_mensal(input('\nInforme o gasto mensal: '))
    return fornecedor


def excluir_fornecedor(id_fornecedor):
    col_fornecedor.delete_one({"_id": ObjectId(id_fornecedor)})
    print("Fornecedor excluído com sucesso!")


def atualizar_fornecedor(id_fornecedor, fornecedor):
    result = col_fornecedor.update_one({'_id': id_fornecedor}, {"$set": fornecedor.__dict__})
    if result.modified_count > 0:
        print(f'\nO fornecedor {fornecedor.get_nome()} foi alterado com sucesso.')


def listar_fornecedores():
    if col_fornecedor.estimated_document_count() > 0:
        for fornecedor in col_fornecedor.find():
            print("\nID: ", fornecedor["_id"], "\nNome: ", fornecedor["nome"], "\nTelefone: ", fornecedor["telefone"],
                  "\nNome produto venda: ", fornecedor["nome_produto_venda"], "\nSegmento do produto: ",
                  fornecedor["segmento_produto"],
                  "\nGasto mensal: ", fornecedor["gasto_mensal"])
    else:
        print("Não existem fornecedores cadastrados no banco de dados")


# Metodos da Lanchonete

def inserir_lanchonete(lanchonete):
    result = col_lanchonete.insert_one(lanchonete.__dict__)
    if result.inserted_id:
        print(f'\nO produto {lanchonete.get_descricao()} foi inserido com sucesso.')


def preencher_lanchonete():
    lanchonete = Lanchonete()
    lanchonete.set_descricao(input('\nInforme a descrição: '))
    lanchonete.set_qtd_clientes(input('\nInforme a quantidade de clientes: '))
    lanchonete.set_num_empregados(input('\nInforme o numero de empregados: '))
    lanchonete.set_total_receita(input('\nInforme o total de receita: '))
    lanchonete.set_total_despesa(input('\nInforme o total de despesa: '))
    return lanchonete


def excluir_lanchonete(id_lanchonete):
    col_lanchonete.delete_one({"_id": ObjectId(id_lanchonete)})
    print("Lanchonente excluído com sucesso!")


def atualizar_lanchonete(id_lanchonete, lanchonete):
    result = col_lanchonete.update_one({'_id': id_lanchonete}, {"$set": lanchonete.__dict__})
    if result.modified_count > 0:
        print(f'\nA lanchonete {lanchonete.get_nome()} foi alterado com sucesso.')


def listar_lanchonetes():
    if col_lanchonete.estimated_document_count() > 0:
        for lanchonete in col_lanchonete.find():
            print("\nID: ", lanchonete["_id"], "\nDescrição: ", lanchonete["descricao"], "\nQuantidade de Clientes: ",
                  lanchonete["qtd_clientes"],
                  "\nNumero de empregados: ", lanchonete["num_empregados"], "\nTotal de receita: ",
                  lanchonete["total_receita"],
                  "\nTotal de despesa: ", lanchonete["total_despesa"])
    else:
        print("Não existem lanchonetes cadastradas no banco de dados")


continuar = True

while continuar:
    print('\n---------- Menu Cliente ---------- ')
    print('\n1 - Inserir cliente')
    print('\n2 - Listar clientes')
    print('\n3 - Excluir cliente')
    print('\n4 - Alterar cliente')
    print('\n---------- Menu Fornecedor ---------- ')
    print('\n5 - Inserir fornecedor')
    print('\n6 - Listar fornecedores')
    print('\n7 - Excluir fornecedor')
    print('\n8 - Alterar fornecedor')
    print('\n---------- Menu Lanchonete ---------- ')
    print('\n9 - Inserir lanchonete')
    print('\n10 - Listar lanchonetes')
    print('\n11 - Excluir lanchonete')
    print('\n12 - Alterar lanchonete')
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
        try:
            print("\n=====================Alterar Cliente=====================")
            id_cliente = str(input("\nInforme o id do Cliente: "))
            atualizar_cliente(id_cliente, preencher_cliente())
        except:
            mensagem_erro()

    elif opcao == '5':
        try:
            print("\n====================Inserir Fornecedor====================")
            inserir_fornecedor(preencher_fornecedor())
        except:
            mensagem_erro()

    elif opcao == '6':
        try:
            print("\n=====================Lista de Fornecedores=====================")
            listar_fornecedores()
        except:
            mensagem_erro()

    elif opcao == '7':
        try:
            print("\n=====================Excluir Fornecedor=====================")
            id_fornecedor = str(input("\nInforme o id do Fornecedor: "))
            excluir_fornecedor(id_fornecedor)
        except:
            mensagem_erro()

    elif opcao == '8':
        try:
            print("\n====================Alterar Fornecedor====================")
            id_fornecedor = str(input("\nInforme o id do Fornecedor: "))
            atualizar_fornecedor(id_fornecedor, preencher_fornecedor())
        except:
            mensagem_erro()

    elif opcao == '9':
        try:
            print("\n=====================Inserir Lanchonete=====================")
            inserir_lanchonete(preencher_lanchonete())
        except:
            mensagem_erro()

    elif opcao == '10':
        try:
            print("\n=====================Lista de Lanchonetes=====================")
            listar_lanchonetes()
        except:
            mensagem_erro()

    elif opcao == '11':
        try:
            print("\n=====================Excluir Lanchonete=====================")
            id_lanchonente = str(input("\nInforme o id da Lanchonete: "))
            excluir_lanchonete(id_lanchonente)
        except:
            mensagem_erro()

    elif opcao == '12':
        try:
            print("\n=====================Alterar Lanchonete=====================")
            id_lanchonente = str(input("\nInforme o id da Lanchonente: "))
            atualizar_lanchonete(id_lanchonente, preencher_lanchonete())
        except:
            mensagem_erro()

    elif opcao == '0':
        continuar = False

    else:
        print('\nOpção inválida.')

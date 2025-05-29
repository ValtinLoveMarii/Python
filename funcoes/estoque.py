# import os

# produtos_dicionario = {}


# def limpar_tela():
#     os.system('cls' if os.name == 'nt' else 'clear')


# def cabecalho(msg):
#     print("\n" + "=" * 40)
#     print(f"{msg.center(40)}")
#     print("=" * 40)


# def adicionar_produtos(produtos_dicionario):
#     limpar_tela()
#     cabecalho("Adicionar Produto")
#     nome_prod = str(input('Digite o nome do produto: ')).lower()
#     quantidade = int(input('Digite a quantidade de unidades: '))
#     preco = float(input('Digite o preço da unidade: '))
#     produtos_dicionario[nome_prod] = [quantidade, preco]
#     print("\nProduto adicionado com sucesso!")
#     input("\nPressione Enter para continuar...")


# def remover_produto(produtos_dicionario):
#     limpar_tela()
#     cabecalho("Remover Produto")
#     remove_prod = str(input('Qual produto deseja remover: ')).lower()
#     if remove_prod in produtos_dicionario:
#         produtos_dicionario.pop(remove_prod)
#         print(f"\nProduto '{remove_prod}' removido com sucesso!")
#     else:
#         print('\nEsse produto não existe!')
#     input("\nPressione Enter para continuar...")


# def atualizar_produtos(produtos_dicionario):
#     limpar_tela()
#     cabecalho("Atualizar Produto")
#     resp_atualizar = str(input('Qual produto deseja atualizar: ')).lower()
#     if resp_atualizar not in produtos_dicionario:
#         print('Esse produto não existe!')
#     else:
#         new_quantidade = int(input(f'Qual a nova quantidade do produto {resp_atualizar}: '))
#         new_preco = float(input(f'Qual o novo preço do produto {resp_atualizar}: '))
#         produtos_dicionario[resp_atualizar] = [new_quantidade, new_preco]
#         print(f"\nProduto '{resp_atualizar}' atualizado com sucesso!")
#     input("\nPressione Enter para continuar...")


# def listar_produto(produtos_dicionario):
#     limpar_tela()
#     cabecalho("Lista de Produtos")
#     if not produtos_dicionario:
#         print("\nNenhum produto cadastrado no estoque.")
#     else:
#         for i, z in produtos_dicionario.items():
#             print(f"{i.title()} - Quantidade: {z[0]} - Preço: R${z[1]:.2f}")
#     input("\nPressione Enter para continuar...")


# # SISTEMA FINAL
# while True:
#     limpar_tela()
#     cabecalho("Sistema de Estoque")
#     print("""
#     [1] - Adicionar Produto
#     [2] - Remover Produto
#     [3] - Atualizar Produto
#     [4] - Listar Produtos
#     [5] - Sair
#     """)

#     resp = input('Escolha uma opção: ')
#     if resp == '1':
#         adicionar_produtos(produtos_dicionario)
#     elif resp == '2':
#         remover_produto(produtos_dicionario)
#     elif resp == '3':
#         atualizar_produtos(produtos_dicionario)
#     elif resp == '4':
#         listar_produto(produtos_dicionario)
#     elif resp == '5':
#         limpar_tela()
#         print('FIM DO ESTOQUE'.center(40, "="))
#         break
#     else:
#         limpar_tela()
#         print("Opção inválida! Tente novamente.".center(40, "="))
#         input("\nPressione Enter para continuar...")







#TESTE DE SISTEMA
import os
dados_produtos = {}
tamanho_linha = 100
print(f'DADOS PRODUTOS {dados_produtos}')

def adiconar_produtos(dados_produtos):
    nome_prod = input('Digite o nome do produto: ').lower()
    quantidade = int(input('Digite a quantidade do produto em estoque: '))
    preco = float(input('Digite o preço por unidade: '))
    
    dados_produtos.update({f'{nome_prod}': [quantidade, preco]})
    if os.path.exists('dados_estoque.txt') == True:
        with open('dados_estoque.txt', 'a', encoding='UTF-8') as a:
            a.write(f'Nome produto: {nome_prod} - Quantidade: {quantidade} - Preço: {preco}\n')
    else:
        with open('dados_estoque.txt', 'w', encoding='UTF-8') as w:
            w.write(f'Nome produto: {nome_prod} - Quantidade: {quantidade} - Preço: {preco}\n')
adiconar_produtos(dados_produtos=dados_produtos)

def remover_produtos(dados_produtos):
    remover = str(input('Qual produto deseja remover do estoque: ')).lower()
    if remover not in dados_produtos:
        print('Valor Inválido, o item náo existe no estoque!')
    elif len(dados_produtos) == 0:
        print('Estoque ainda não possuí produtos, por favor adicione!')
    else:
        dados_produtos.pop(remover)
        with open('dados_estoque.txt', 'r') as r:
            lista = r.readlines()
            for i, valor in enumerate(lista):
                if remover in valor:
                    del lista[i]
                    with open('dados_estoque.txt', 'w', encoding='UTF-8') as w:
                        w.writelines(lista)

remover_produtos(dados_produtos=dados_produtos)

def atualizar_produtos(dados_produtos):
    produto_atualizar = str(input('Qual produto deseja atualizar: '))
    
    if produto_atualizar not in dados_produtos:
        print('Produto Inválido ou inexistente!')
    elif len(dados_produtos) == 0:
        print('Estoque ainda não possuí produtos, por favor adicione!')
    else:
        nova_quantidade = int(input(f'Digite a nova quantidade disponível do produto {produto_atualizar}: '))
        novo_preco = int(input(f'Digite o novo valor de cada produto: '))
        dados_produtos.update({f'{produto_atualizar}':[nova_quantidade, novo_preco]})
        with open('dados_estoque.txt', 'r') as r:
            lista = r.readlines()
            for i, valor in enumerate(lista):
                if produto_atualizar in valor:
                    lista[i] = f'Nome produto: {produto_atualizar} - Quantidade: {nova_quantidade} - Preço: {novo_preco}\n'
                    with open('dados_estoque.txt', 'w', encoding='UTF-8') as w:
                        w.writelines(lista) 
atualizar_produtos(dados_produtos=dados_produtos)

def mostrar_tela(tamanho_linha):
    with open('dados_estoque.txt', 'r', encoding='UTF-8') as r:
        print('=' * tamanho_linha)
        print('PRODUTOS CADASTRADOS NO ESTOQUE'.center(tamanho_linha))
        print('=' * tamanho_linha)
        print(r.read())
mostrar_tela(tamanho_linha=tamanho_linha)
print(dados_produtos)

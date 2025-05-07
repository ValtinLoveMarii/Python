import os
items_produtos = {}
numero_prod = 0
for i in range(1):
    nome_prod = str(input('Qual produto a ser cadastrado? '))
    quantidade = int(input('Qual a quantidade do produto? '))
    preco = float(input('Qual o valor por unidade? '))
    numero_prod = str(numero_prod)
    items_produtos['Produto_'+numero_prod] = {'nome':nome_prod, 'quantidade':quantidade, 'preco':preco}
    numero_prod = int(numero_prod)
    numero_prod += numero_prod
    os.system('cls')


#ADICONAR PRODUTO
def adiconar_produtos(items_produtos):
    numero_prod = 1
    nome_prod = str(input('Qual produto a ser cadastrado? '))
    quantidade = int(input('Qual a quantidade do produto? '))
    preco = float(input('Qual o valor por unidade? '))
    numero_prod = str(numero_prod)
    items_produtos.update({'Produto_'+numero_prod:{'nome':nome_prod,'quantidade':quantidade, 'preco':preco}})
    numero_prod = int(numero_prod)
    numero_prod += numero_prod
    os.system('cls')
adiconar_produtos(items_produtos)

#REMOVER PRODUTO
def remover_produto(items_produtos):
    remover = str(input('Qual produto deseja remover? ')).lower()
    if remover == 'n' or remover == 'nao':
        pass
    else:
        items_produtos.pop('Produto_'+remover)
    os.system('cls')
remover_produto(items_produtos)


#ATUALIZAR QUANTIDADE
def atualizar_quantidade(items_produtos):
    prod_atualizar = str(input('Qual produto atualizar? '))
    prod_atualizar = 'Produto_'+prod_atualizar
    if prod_atualizar in items_produtos:
        atu = int(input(f'Qual a nova quantidade do {prod_atualizar}? '))
        var = items_produtos[prod_atualizar]
        var['quantidade'] = atu
    else:
        print('Produto já removido!')
atualizar_quantidade(items_produtos)


#MOSTRAR O ESTOQUE
def listar_estoque(items_produtos):
    for i,z in items_produtos.items():
        print(i, z)
listar_estoque(items_produtos)

#SISTEMA INTEGRADO COMPLETO
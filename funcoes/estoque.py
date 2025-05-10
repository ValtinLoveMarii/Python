import os

produtos_dicionario = {}
for i in range(1):
    nome_prod = str(input('Digite o produto: ')).lower()
    quantidade = int(input('Digite a quantidade de unidades: '))
    preco = float(input('Digite o preço da unidade: '))
    produtos_dicionario[nome_prod] = [quantidade, preco]
    os.system('cls')
#--------------------------------------------------------------------
def adicionar_produtos(produtos_dicionario):
    nome_prod = str(input('Digite o novo valor: ')).lower()
    quantidade = int(input('Digite a quantidade de unidades: '))
    preco = float(input('Digite o preço da unidade: '))
    produtos_dicionario[nome_prod] = [quantidade, preco]
    os.system('cls')
# adicionar_produtos(produtos_dicionario)
#--------------------------------------------------------------------
def remover_produto(produtos_dicionario):
    remove_prod = str(input('Qual produto deseja retirar: '))
    if remove_prod in produtos_dicionario:
        produtos_dicionario.pop(remove_prod)
    else:
        print('Esse produto não existe!')
# remover_produto(produtos_dicionario)

#--------------------------------------------------------------------
def atualizar_produtos(produtos_dicionario):
    resp_atualizar = str(input('Qual produto deseja atualizar: ')).lower()
    if resp_atualizar not in produtos_dicionario:
        print('Esse produto não existe!')
        os.system('cls')
    else:    
        new_quantidade = int(input(f'Qual a nova quantidade do produto {resp_atualizar}: '))
        new_preco = float(input(f'Qual o novo preço do produto {resp_atualizar}: '))
        produtos_dicionario[resp_atualizar] = [new_quantidade, new_preco]
#--------------------------------------------------------------------
def listar_produto(produtos_dicionario):
    for i,z in produtos_dicionario.items():
        print(f'{i} : {z}')



#--------------------------------------------------------------------
# SISTEMA FINAL
while True:
    print('SISTEMA DE ESTOQUE')
    resp = input(('ADICIONAR PRODUTO[1]\nREMOVER PRODUTO[2]\nATUALIZAR PRODUTO[3]\nLISTAR PRODUTO[4]\nSAIR[5]\n\nDesejo: '))
    if resp == '1':
        os.system('cls')
        adicionar_produtos(produtos_dicionario)
    elif resp == '2':
        os.system('cls')
        remover_produto(produtos_dicionario)
    elif resp == '3':
        os.system('cls')
        atualizar_produtos(produtos_dicionario)
    elif resp == '4':
        os.system('cls')
        listar_produto(produtos_dicionario)
    elif resp == '5':
        break
    else:
        os.system('cls')
        print('Dado Inválido!')
        print('Tente Novamente!')
os.system('cls')
print('FIM DO ESTOQUE')


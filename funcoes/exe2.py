#EX1 - Crie uma função com nomes de alunos e suas notas. Depois, calcule e imprima a média das notas.
# def function(**kwags):
#     return kwags
# alunos = {}
# while True:
#     nome = str(input('Nome: '))
#     nota = float(input('Nota: '))    
#     aluno = function(**{nome:nota})
    
#     alunos.update(aluno)
    
#     cont = str(input('CONTINAR? (S)'))
#     if cont == 's':
#         continue
#     else:
#         break

# EX2 - PROJETO ANALISE DE DADOS BASICO Consiste em uma analise sobre uma loja

# #BASE DE DADOS de vendas da LOJA
vendas = [
    {'dia': 'segunda', 'produto': 'camiseta', 'quantidade': 72, 'preco_unitario': 50},
    {'dia': 'segunda', 'produto': 'calça', 'quantidade': 1, 'preco_unitario': 120},
    {'dia': 'terça', 'produto': 'camiseta', 'quantidade': 5, 'preco_unitario': 50},
    {'dia': 'quarta', 'produto': 'tênis', 'quantidade': 12, 'preco_unitario': 200},
    {'dia': 'quarta', 'produto': 'calça', 'quantidade': 9, 'preco_unitario': 120},
    {'dia': 'quinta', 'produto': 'camiseta', 'quantidade': 11, 'preco_unitario': 250},
    {'dia': 'sexta', 'produto': 'tênis', 'quantidade': 71, 'preco_unitario': 200},
]

#DADOS A SEREM EXTRAIDOS
def prods_sales(vendas):
    tot_prods_sales = {}
    for v in vendas:
        prod = v['produto']
        qtd = v['quantidade']
        if prod in tot_prods_sales:
            tot_prods_sales[prod] += qtd
        else:
            tot_prods_sales[prod] = qtd
    return tot_prods_sales
result_total_prods = prods_sales(vendas)

#PRODUTO COM A MAIOR QUANTIDADE DE VENDAS
def more_sales(result_total_prods):
    maior = 0
    name_prod = None
    for i,z in result_total_prods.items():
        if z > maior:
            maior = z
            name_prod = i
    return name_prod
res_more_sales = more_sales(result_total_prods)



#DIA COM MAIOR FATURAMENTO
def day_more_sales_list(vendas):
    day_sales = {}
    for d in vendas:
        day = d['dia']
        price = d['preco_unitario']
        if day in day_sales:
            day_sales[day] += price
        else:
            day_sales[day] = price
    maior = 0
    name_day = None
    for i,z in day_sales.items():
        if z > maior:
            maior = z
            name_day = i
    return day_sales, name_day
day_sales,name_day = day_more_sales_list(vendas)
print('Relatório de Vendas')
print('--'*20)
print('Quantidade de Vendas por produto')
for i,z in result_total_prods.items():
    print(f'{i}: {z}')
print('--'*20)
print('Faturamento diário')
for x,m in day_sales.items():
    print(f'{x}: {m}')
print('--'*20)
print(f'Dia com o maior faturamento: {name_day}')
print(f'Produto com maior número de vendas: {res_more_sales}')
print('--'*20)
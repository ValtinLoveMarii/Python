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

#BASE DE DADOS de vendas da LOJA
vendas = [
    {'dia': 'segunda', 'produto': 'camiseta', 'quantidade': 3, 'preco_unitario': 50},
    {'dia': 'segunda', 'produto': 'calça', 'quantidade': 1, 'preco_unitario': 120},
    {'dia': 'terça', 'produto': 'camiseta', 'quantidade': 2, 'preco_unitario': 50},
    {'dia': 'quarta', 'produto': 'tênis', 'quantidade': 1, 'preco_unitario': 200},
    {'dia': 'quarta', 'produto': 'calça', 'quantidade': 2, 'preco_unitario': 120},
    {'dia': 'quinta', 'produto': 'camiseta', 'quantidade': 1, 'preco_unitario': 50},
    {'dia': 'sexta', 'produto': 'tênis', 'quantidade': 1, 'preco_unitario': 200},
]

#DADOS A SEREM EXTRAIDOS


#Total de vendas por produtos



#CRIA A LISTA COM TODOS OS PRODUTOS
prods_values_list = []
def get_prods(prods_values):
    for i in vendas:
        values = i["produto"]
        prods_values_list.append(values)
    return prods_values_list

prods_values = get_prods(prods_values_list)


#CRIA O DICIONARIO COM OS TOTAL DE VENDAS POR PRODUTO

def tot_sales(prods_values):
    dic_res = {}
    x_index = 0
    for i in vendas:
        while x_index < len(prods_values):
            x = prods_values[x_index]
            if x not in dic_res:
                qtd = i['quantidade']
                dic_res.update({x:qtd})
                x_index += 1  
                break
            else:
                qtd =i['quantidade']
                dic_res[x] += qtd
                x_index += 1  
    return dic_res
result_total_sales = tot_sales(prods_values)
print(f'Total de Vendas da Loja!')
for x,z in result_total_sales.items():
    print(x,z)
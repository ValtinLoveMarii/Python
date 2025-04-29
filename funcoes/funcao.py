#AULA 30 - Funções
def myfunction():
    a = 5
    b = 3
    print(a+b)
    if (a > b):
        print('A > B')
    else:
        print('B > A')

def mysecondfunction():
    l = [1,3,4,5,6]
    maior = 0
    menor = 99999999999
    for i in l:
        if i > maior:
            maior = i
        if i < menor:
            menor = i
    return maior, menor
maior, menor = mysecondfunction()
print(maior, menor)   

lista = [1,2,3,4,1]
def functionPOP():
    lista.pop()
    return lista
res = functionPOP()
print(res) 


def creat_data():
    l = {"Produto":'Mouse00991', 'Preco':90}
    return l
def update_values(data):
    name_update = data['Produto']
    name_update = name_update[0:5]
    data['Produto'] = name_update
    return data
datas_ini = creat_data()
res_final = update_values(datas_ini)
print(f'Planilha formatada! {res_final}')

def function(nome, idade):
    print(nome)
    print(idade)
function(idade=19, nome='pedro')    

def function(x=None, z = None):
    if x != None:
        print(x, z)
    else:
        print('Valores não passados passa ai')
function(z='narutinjo', x='elliee')

def function(nome, *args):
    print(nome)
    print(args)
function('naruto',[1,2,'balde'])
def function(**kwags):
    print(kwags)
function(nome='aluno1', nota=7)
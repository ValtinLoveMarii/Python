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

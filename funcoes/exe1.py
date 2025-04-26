#Exercícios de Função
#EX1 - Crie uma função que receba dois números e retorne a soma deles.
def function():
    a = 10
    b = 1290
    soma = a + b
    return soma
res = function()
# print(res)

#EX2 - Crie uma função que receba uma string e imprima "Olá, [nome]!".
def function():
    nome = str(input('Nome: '))
    print(f'Olá {nome}')
# function()

#EX3 - Crie uma função que retorne o maior de uma lista.
def function():
    l = []
    maior = 0
    for i in range(3):
        n = int(input('Numero: '))
        l.append(n)
    for x in l:
        if x > maior:
            maior = x
    return maior
# maior = function()
# print(f'Maior número é {maior}')

#EX4 - Crie uma função que receba um número e retorne True se for par e False se for ímpar.
def function():
    n = int(input('Numero: '))
    if n%2 == 0:
        return True
    else:
        return False
# res = function()
# print(res)

#EX5 - Crie uma função que calcule o fatorial de um número (sem usar bibliotecas).
def function():
    n = int(input('Numero: '))
    valor = 1
    for i in range(1, n+1):
        valor = valor * i
    return valor
# res = function()
# print(res)

#EX6 - Crie uma função que receba uma lista de números e retorne a média deles.
def function():
    l = [1,3,6,1,3,2324,244,542,233,56,8,91,2,4566,12]
    soma = sum(l)
    media = soma/(len(l))
    return media
# res = function()
# print(round(res, 2))

#EX7 - Crie uma função que conte o número de vogais em uma string.
def function():
    c = 0
    vogais = 'aeiou'
    palavra = str(input('Digite uma palavra: ')).lower()
    for i in palavra:
        if i in vogais:
            c = c + 1
    return c
# res = function()
# print(f'O numero de vogais é de {res}')

#EX8 - Crie uma função que receba uma lista e retorne outra lista com apenas os números pares.
def function():
    l = [1,3,6,21312,67676,13,99012]
    l_par = []
    for i in l:
        if i%2 == 0:
            l_par.append(i)
        else:
            continue
    return l_par
# res = function()
# print(res)

#EX9 - Crie uma função que, dado um número, retorne uma lista de todos os seus divisores.
def function():
    n = int(input('Numero: '))
    l_divs = []
    for i in range(1, n+1):
        if n%i == 0:
            l_divs.append(i)
        else:
            continue
    return n, l_divs
# n, divs = function()
# print(f'Os divisores de {n} são {divs}')

#EX10 - Criar variáveis a partir de items de uma lista
l = ['var1', 'var2', 'var3']
def functionCreateVar():
    for i in l:
        globals()[f'{i}'] = None
    print(globals())
def functionUpdateVar():
    while True:
        for i in range(1, len(l)+1):
            globals ()[f'var{i}'] = 1
        break
    a = globals()
    return a
# res = functionUpdateVar()
# print(res)
            

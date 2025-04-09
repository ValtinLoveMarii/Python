#EX1 - Dada a tupla acima, use .index() para descobrir a posição da primeira ocorrência do número 3.
# l = []
# for i in range(1, 4):
#     n = int(input('Number: '))
#     l.append(n)
# l = tuple(l)
# print(f'The occurrence it happened in index {l.index(3)}')

#EX2 - Dada a tupla valores = (10, 20, 30, 40, 50, 60, 70, 80), obtenha: Os três primeiros elementos, Os três últimos elementos, Os elementos do meio (excluindo os primeiros e últimos dois).
# tuple_values = (10, 20, 30, 40, 50, 60, 70, 80)
# print(f'The first to third {tuple_values[1:4]}')
# print(f'The last three numbers {tuple_values[5:8]}')

#EX3 - Crie um programa que receba uma tupla de números e retorne uma nova tupla ordenada do menor para o maior.
# tupla = (1,4,6,2,9,7,10,12)
# tupla = list(tupla)
# tupla.sort()
# tupla = tuple(tupla)
# print(tupla)

#EX4 - Dada a tupla numeros = (10, 15, 8, 25, 30, 3, 5, 18), crie um código que retorne somente os números pares dentro de uma nova tupla.
# numbers = (10, 15, 8, 25, 30, 3, 5, 18)
# tupla = []
# for i in numbers:
#     if i%2 == 0:
#         tupla.append(i)
# tupla = tuple(tupla)
# print(tupla)

#EX5 -Crie uma função operacoes(a, b) que receba dois números e retorne uma tupla com a soma, subtração, multiplicação e divisão deles.
# a = int(input('Number: '))
# b = int(input('Number: '))
# t = []
# for i in range(1, 5):
#     if (i == 1):
#         soma = a+b
#         t.append(soma)
#     elif (i==2):
#         sub = a-b
#         t.append(sub)
#     elif (i==3):
#         mult = a*b
#         t.append(mult)
#     elif (i == 4):
#         div = a/b
#         t.append(div)
# t = tuple(t)
# print(t)

#EX6 - Crie uma nova tupla que contenha os elementos de ambas as tuplas, mas sem repetir valores.
# t = (1, 2, 3, 4, 5)
# t2 = (3, 4, 5, 6, 7)
# t = t+t2
# t = list(t)
# new_list = []
# for i in t:
#     if i not in new_list:
#         new_list.append(i)
#     else:
#         continue
# print(tuple(new_list))

#EX7 - Atualizando exe5
# import os
# while True:
#     try:
#         x = int(input('Number: '))
#         y = int(input('Number: '))
#         t = []
#         for i in range(1, 5):
#             if (i == 1):
#                 soma = x + y
#                 t.append(soma)
#             elif(i == 2):
#                 sub = x -y
#                 t.append(sub)
#             elif(i == 3):
#                 mult = x * y
#                 t.append(mult)
#             elif(i == 4):
#                 div = x / 2
#                 t.append(div)
#         prox = str(input('Do you want to continue? (s/n) '))
#         if (prox == 's' or prox == 'S'):
#             os.system('cls')
#             continue
#         elif (prox == 'n' or prox == 'N'):
#             break
#         break
#     except ValueError as error:
#         os.system('cls')
#         print('The data entered is not valid')
#         print('Try Again!')
# print(t)

#EX8 - REFAZER o EX6 do arquivo ex1 de TUPLA
# tupla = ('Valtin', 23, 'Pleno')
# list_names_variable = ['name','age','position']
# for i in list_names_variable:
#     globals()[f'{i}'] = None

# for x in range(len(tupla)):
#     globals()[list_names_variable[x]] = tupla[x]
#     print(globals()[list_names_variable[x]])
# print(globals())


# #EX9 - Você deve criar uma tupla contendo objetos mutáveis, como listas ou dicionários. Implemente uma função que altere o conteúdo do objeto mutável na tupla e explique por que é possível.
# tupla = []
# c = 0
# for i in range(2):
#     tupla.append(list())
# for x in tupla:
#     # print(x)
#     print(f'Lista {c+1}')
#     for l in range(1, 3):
#         n = int(input('Numero: '))
#         x.append(n)
#     c = c + 1
# tupla = tuple(tupla)
# print(tupla)

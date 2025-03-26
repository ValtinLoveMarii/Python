#EXERCÍCIOS DE LISTA

#EX1 - Crie uma lista com os seguintes números: 1, 2, 3, 4, 5. Imprima a lista.
# l = [1,2,3,4,5]
# print(l)

#EX2 - Dada a lista lista = [10, 20, 30, 40, 50], altere o valor do terceiro elemento para 100. Imprima a lista atualizada.
# l = [10,20,30,40,50]
# l[3] = 100
# print(l)

#EX3 - Crie uma lista vazia e adicione os números de 1 a 5 utilizando o método append(). Imprima a lista após cada adição.
# l = []
# for i in range(1, 6):
#     num = int(input('Digite um numero: '))
#     l.append(num)
# print(l)

# #EX4 - Dada a lista lista = [10, 20, 30, 40, 50], remova o número 30 da lista usando o método remove(). Imprima a lista resultante.

# l = [10, 20, 30, 40, 50]
# l.remove(l[3])
# print(l)


#EX5 - Dada a lista lista = [1, 2, 3, 4, 5], verifique se o número 3 está na lista e imprima "Sim" ou "Não" dependendo do resultado.
# l = [1,2,3,4,5]
# if 3 in l:
#     print('Sim tem 3 em na lista')
# else:
#     print('Não tem 3 na lista')


#EX6 - Crie duas listas, lista1 = [1, 2, 3] e lista2 = [4, 5, 6]. Junte as duas listas em uma só. Imprima o resultado.
# l = [1,2,3]
# l2 = [9,8,7]
# l.extend(l2)
# print(l)

#EX7 - Dada a lista lista = [1, 2, 3, 4, 5, 6], crie uma nova lista contendo os elementos do índice 2 até o índice 4. Imprima a lista resultante.
# l = [1,2,3,4,5,6]
# l2 = []
# for i in l[2:5]:
#     l2.append(i)
# print(l2)


#EX8 - Dada a lista lista = [5, 1, 4, 3, 2], ordene os elementos da lista em ordem crescente e imprima a lista ordenada.
# l = [5, 1, 4, 3, 2]
# l.sort()
# sorted(l)

#EX9 - Dada a lista lista = [10, 20, 5, 8, 15], encontre e imprima o maior e o menor valor.
# lista = [10, 20, 5, 8, 15]
# # maior = 0
# # menor = 999999999
# # for i in lista:
# #     if (i > maior):
# #         maior = i
# #     if (i < menor):
# #         menor = i
# # print(menor, maior)
# # OU
# print(max(lista))
# print(min(lista))

#EX10 - Dada a lista lista = [1, 2, 3, 1, 2, 1], conte quantas vezes o número 1 aparece na lista.

# lista = [1, 2, 3, 1, 2, 1]
# contador = 0
# for i in lista:
#     if (i == 1):
#         contador = contador + 1
#     else:
#         continue
# print(contador)

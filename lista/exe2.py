#EXERCÍCIOS DE LISTA

#EX1 - Dada a lista lista = [10, 20, 30, 40, 50], calcule a soma e a média dos elementos da lista.
# lista = [10, 20, 30, 40, 50]
# # soma = 0
# # for i in lista:
# #     soma = soma + i
# # media = soma / len(lista)
# # print(soma, media)
# # OU
# media = sum(lista) / len(lista)
# print(media)

#EX2 - Dada a lista lista = [1, 2, 3, 1, 2, 4, 5], remova os números duplicados da lista e imprima a lista sem repetições.
# lista = [1, 2, 3, 1, 2, 4, 5]
# lista_nova = []
# for i in lista:
#     if i not in lista_nova:
#         lista_nova.append(i)
# print(lista_nova)

#EX3 - Crie uma lista de listas, onde cada sublista contém três números. Por exemplo: listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]. Acesse o número 5 utilizando índice.
# listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# novo_indice = listas[1]
# print(novo_indice[1])

# #EX4  - Recriar o 3 mas agorando criando a lista
# l = []
# a = 0
# for i in range(1,4):
#     l.append([])
# for x in l:
#     print('Novo lop! ')
#     if(len(x) == 3):
#         print('Acabou!')
#         continue
#     else:
#         for m in range(1, 4):
#             num = int(input('Numero: '))
#             x.append(num)
#             print('Dado inserido com sucesso!')
# print(l)

#EX5  - Escreva uma função que remova elementos duplicados de uma lista sem usar conjuntos (set) ou listas auxiliares. A função deve manter a ordem original dos elementos.
# l = []
# new_lista = []
# for i in range(1, 6):
#     n = int(input('Digite um número: '))
#     l.append(n)
# for d in l:
#     if (d not in new_lista):
#         new_lista.append(d)
#     else:
#         continue
# print(l, new_lista)

#EX6 - Dada uma lista de números inteiros e um número alvo, escreva uma função que encontre todas as sublistas contínuas cuja soma seja igual ao número alvo.
new_list = []
final_list = []
l = [1, 2, 3, 4, 2, 1, 5, 6] 
alvo = 6
for i in l:
    new_list.append(i)
    if (sum(new_list) == 6):
        print('Deu certo')
        # print(new_list)
        final_list.append(new_list[:])
        print(final_list)
        print(new_list)
        print(len(new_list))
        new_list = []
        continue
    else:
        continue

# print(f'Lista new {new_list}')
print(f'Lista final {final_list}')

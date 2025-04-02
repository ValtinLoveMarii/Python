#EXERCÍCIOS DE TUPLA

#EX1 - Crie uma tupla chamada minha_tupla contendo os números 1, 2, 3, 4, 5. Em seguida, imprima o segundo elemento da tupla.
# minha_tupla = (1,2,3,4,5)
# print(f" Minha tupla, com o segundo valor: {minha_tupla[1]}")

#EX2 - exe1 mas criado a tupla
# lista = []
# for i in range(1, 6):
#     n = int(input('Digite um número: '))
#     lista.append(n)
# lista = tuple(lista)
# print(f"""Sua tupla foi criada! O valor do segundo número: {lista[1]} O tipo de dado: {type(lista)}
#     """)

#EX3 - Dada a tupla frutas = ("maçã", "banana", "laranja", "uva"), imprima: O primeiro e o último elemento da tupla. O terceiro elemento usando índice negativo.
# lista = []
# for i in range(1, 7):
#     n = str(input('Digite uma fruta: '))
#     lista.append(n)
# lista = tuple(lista)
# print(lista)
# print(f"Primeiro índice {lista[0]}")
# print(f"Ultimo índice {lista[-1]}")
# print(f"Terceiro ultimo índice {lista[-3]}")

#EX4 - Dada a tupla tupla1 = (1, 2, 3) e a tupla tupla2 = (4, 5, 6), crie uma nova tupla tupla3 que seja a concatenação de tupla1 e tupla2. Imprima tupla3.
# tupla1 = (1,2,3)
# tupla2 = (4,5,6)
# tupla3 = tupla1 + tupla2
# print(f'Nova tupla com a soma das 2 {tupla3}')

#EX5 - Crie uma tupla chamada numeros = (1, 3, 5, 7, 9) e verifique se o número 5 está presente na tupla. Imprima "Sim" se estiver presente, "Não" caso contrário.
# tupla = (1,3,8,7,9, 5)
# exist = False
# for i in tupla:
#     if i == 5:
#         print(f'Sim existe o número {i}')
#         exist = True
#         break
#     else:
#         print('Ainda não presente! ')
#         continue
# if(exist == False):
#     print('Dentro da lista não existe o número 5')

#EX6 - Dada a tupla dados = ('João', 25, 'Mestre'), desempacote ela em três variáveis chamadas nome, idade e cargo. Depois, imprima essas variáveis.
# tupla = ('João', 25, 'Mestre')
# l = []
# for i in range(len(tupla)):
#     globals ()[f'variavel{i}'] = None
# print(globals())
# for x in range(len(tupla)):
#     globals()[f'variavel{x}'] = tupla[x]

# for z in range(len(tupla)):
#     l.append(globals()[f'variavel{z}'])
# print(l)

# z = 2
# print(globals()[f'variavel{z}'])

#EX7 - Dada a tupla tupla = (1, 2, 3, 4, 2, 5, 2), conte quantas vezes o número 2 aparece na tupla e imprima o resultado.
# tupla = (1, 2, 3, 4, 2, 5, 2)
# l = []
# print(f'O numero 2 aparece {tupla.count(2)} vezes')
# for i in tupla:
#     if i == 2:
#         l.append(i)
# print(f'O número 2 aparece {len(l)} vezes')




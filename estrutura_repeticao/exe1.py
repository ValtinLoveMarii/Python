#Exercíciso FOR e WHILE
#EX1 -  Crie um programa que use um laço for e while para imprimir os números de 1 a 10.
# for i in range(1,11):
#     print(i)
# i = 0
# while i <= 9:
#     i = i + 1
#     print(i)

#EX2 - Crie um programa que use um laço para somar todos os números de 1 a 50 e mostre o resultado.
# contador = 0
# for i in range(1, 51):
#     contador = i + contador
# print(contador)

#EX3 - Crie um programa que use um laço for para imprimir os números pares entre 0 e 20.
# for i in range(1, 20):
#     if (i % 2 == 0):
#         print(i)
#     else:
#         continue
# print('Fim do loop')

#EX4 - Crie um programa que use um laço for para imprimir os primeiros 5 múltiplos de 3.
# for i in range(1, 16):
#     if (i % 3 == 0):
#         print(i)
#     else:
#         continue
# print('Fim do loop')

# #EX5 - Fatorial de um número
# numero = int(input('Numero: '))
# contador = 1
# for i in range(1, numero+1):
#     contador = contador * i
# print(contador)

#EX6 - Solicite ao usuário um número e determine se ele é primo ou não, utilizando um laço de repetição.
# num = int(input('Numero: '))
# primo = 0
# if(num < 2):
#     print('Não é primo')
# else:
#     for i in range(1, num+1):
#         if (num % i == 0):
#             primo = primo + 1
#     if (primo == 2):
#         print('É primo!')
#         print(primo)
#     else:
#         print('Não é primo')

#EX7 - Solicite ao usuário uma string e conte o número de ocorrências de um caractere específico, utilizando laços de repetição
# letras = str(input('Digite: ')).lower()
# contador = 0
# for i in letras:
#     if (i == 'a'):
#         contador = contador + 1
# print(f'A letra "a" aparece {contador}')

#EX8 - Solicite ao usuário uma palavra e determine se ela é um palíndromo (uma palavra que pode ser lida da mesma forma de trás para frente), utilizando laços de repetição.
# palavra = str(input('Digite: '))
# l = []
# invertido = ''
# certo = ''
# for i in palavra:
#     l.append(i)
# for i in reversed(l):
#     invertido = invertido + i
# for i in l:
#     certo = certo + i
# if (certo == invertido):
#     print('Deu certo')
#     print(invertido)
#     print(certo)
# else:
#     print('Deu errado')
#     print(invertido)
#     print(certo)

#EX9 - Solicite ao usuário um número inteiro e calcule a soma de seus dígitos (por exemplo, 123 → 1 + 2 + 3 = 6)
# num = str(input('Numero: '))
# contador = 0
# for i in num:
#     contador = int(i) + contador
#     print(contador)
# print(f'Resultado final foi de {contador}')

#EX10 - Solicite ao usuário um número inteiro positivo n e calcule a sequência de Collatz até chegar a 1
# n = int(input('Digite um número para fazer uma sequência de Collatz:  '))
# if(n < 0):
#     print('Não é possível fazer com números menores que 0!')
# else:
#     while True:
#         print(f'Volta {n}')
#         if (n == 1):
#             break
#         if (n % 2 == 0):
#             n = n / 2
#             print(f"Resultado par {n}")
#             continue
#         if (n % 2 == 1):
#             n = (n * 3) + 1
#             print(f'Resultado impar {n}')
                
    
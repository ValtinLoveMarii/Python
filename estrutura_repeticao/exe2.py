#Exercíciso FOR e WHILE

#EX1 - Solicite ao usuário um número e determine se ele é um número perfeito 
# num = int(input('Digite um número para descobrir se ele é perfeito: '))
# divisor = 0
# for i in range(1, num):
#     if(num % i == 0):
#         divisor = divisor + i
#     else:
#         continue
# if (divisor == num):
#     print(f'Ele é um número perfeito, pois as somas dos divisores é igual')
# else:
#     print(f'Ele não é um número perfeito')

#EX2 - Crie uma versão simples do jogo da forca onde o usuário deve adivinhar uma palavra, e o programa deve exibir as letras corretamente adivinhadas.
# import os
# palavra_certa = 'naruto'
# letras_certas = ''
# letras_erradas = ''
# while True:
#     for i in palavra_certa:
#         letra = str(input('Digite uma letras para acertar a palavra: '))
#         if (i == letra):
#             letras_certas = letras_certas + i
#             print('Letra Correta')
#             continue
#         else:
#             letras_erradas = letras_erradas +i
#             print('Letra incorreta')
#             continue
#     if (letras_certas == palavra_certa):
#         os.system('cls')
#         print('Você acertou!')
#         print(f'A palavra certa era {palavra_certa}')
#         break
#     else:
#         print('Você errou! ')
#         continue

#EX3 - Gerador de senha
# num = '123456789'
# new_senha = ''
# maiuscola = False
# minuscola = False
# tamanho = False
# numero = False
# while True:
#     senha = str(input('Digite sua senha: '))
#     for l in senha:
#         if (len(senha) >= 8):
#             tamanho = True
#         if (l.isupper()):
#             maiuscola = True
#         if(l.lower()):
#             minuscola = True
#     if (maiuscola == True and minuscola == True and tamanho == True):
#         print('Senh correta')
#         for i in senha:
#             if (i in "Aa"):
#                 new_senha = new_senha + '10'
#             elif(i in 'Bb'):
#                 new_senha = new_senha + '11'
#             elif(i in 'Cc'):
#                 new_senha = new_senha + '12'
#             elif(i in 'Dd'):
#                 new_senha = new_senha + '13'
#             elif(i in 'Ee'):
#                 new_senha = new_senha + '14'
#             elif(i in 'Ff'):
#                 new_senha = new_senha + '_'
#             elif(i in 'Gg'):
#                 new_senha = new_senha + '$'
#             else:
#                 new_senha = new_senha + i
#         print(f'Senha Criptografada {new_senha}')
#         break
#     else:
#         print('Tente Novamente')
#         continue


#EX4 - Verificação de números primos até n
import math
n = int(input('Digite um número: '))

if n < 2:
    print('Não é primo')
else:
    for i in range(2, n+1):
        primo = True
        for c in range(2, int(math.sqrt(i)) + 1):
            if (i % c == 0):
                primo = False
                break
        if (primo):
            print(i)
    
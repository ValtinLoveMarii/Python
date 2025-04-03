#EXERCÍCIOS DE IF E ELSE
#EX1 - Crie uma calculadora simples que permita ao usuário escolher entre somar, subtrair, multiplicar ou dividir dois números. 
# num1 = float(input('Numero: '))
# num2 = float(input('Numero: '))
# escolha = str(input('Qual conta voce deseja fazer: S/D/M: '))
# if (escolha == 'S' or escolha == 's'):
#     conta = num1 * num2
#     print(conta)
# elif (escolha == 'D' or escolha == 'd'):
#     conta = num1 / num2
#     print(conta)
# elif (escolha == 'M' or escolha == 'm'):
#     conta = num1 * num2
#     print(conta)

# import random
# #EX2 - Jogo de adivinhação
# while True:
#     num = random.randint(1,100)
#     num_user = int(input('Digite seu numero: '))
#     if (num == num_user):
#         print('Voce acertou!')
#         break
#     else:
#         print('Voce errou tente novamente')
#         continue


# #EX3 - Menu de opções com aninhamento de condições
# while True:
#     num = float(input('Digite um numero: '))
#     opcao = str(input(
#     """Digite suas opções:
#        1: Adicionar número
#        2: Subtrair número
#        3: Multiplicar número
#        4: Dividir número
#        0: Sair: """))
#     if (opcao == '1'):
#         num = num + 1
#         print(num)
#         continue
#     elif (opcao == '2'):
#         num = num - 1
#         print(num)
#         continue
#     elif(opcao == '3'):
#         num = num * 1
#         print(num)
#         continue
#     elif (opcao == '4'):
#         num = num / 2
#         print(num)
#         continue
#     elif (opcao == '0'):
#         print('Saiu do progama!')
#         break

#EX4 - Calculando o fatorial 
# num = int(input('Numero: '))
# conta = 1
# for c in range (1, num + 1):
#     conta = conta * c
#     print(conta)

#EX5 - Triângulo com base em ângulos Escreva um programa que receba três ângulos e determine se eles formam um triângulo.
# ang1 = float(input('Digite o angulo 1: '))
# ang2 = float(input('Digite o angulo 2: '))
# ang3 = float(input('Digite o angulo 3: '))
# if ((ang1 + ang2 + ang3 == 180) and (ang1 > 0 and ang2 > 0 and ang1 > 0) ):
#     print('É um triangulo!')
# else:
#     print('Não é um triângulo')


# import math
# #EX6 - Verificador de números primos
# num = int(input('Digite um numero: '))
# if (num <= 1):
#     print('Não é primo')
# else:
#     raiz_num = int(math.sqrt(num))
#     primo = True

#     for i in range(2,raiz_num+1):
#         conta = num % i
#         if (conta == 0):
#             primo = False
    
#     if (primo == True):
#         print('Primo')
#     else:
#         print('Não é primo!')

#EX7 - Desafio de segurança de senha Implemente um sistema de segurança para login, no máximo 3 tentativas.
# senha_correta = '12345'
# user_correto = 'valtinlovesmari'
# for i in range (3):
#     senha = str(input('Digite sua senha: '))
#     user = str(input('Digite seu user: '))
#     if (senha == senha_correta and user == user_correto):
#         print('Login Valido!')
#         break
#     else:
#         print('Deu erro, continue!')
#         continue
# print(f'Login acessado Bem vindo {user}!')

#EX8 - Verificador de números perfeitos Escreva um programa que verifique se um número é perfeito.
# num = int(input('Digite um numero: '))
# lista = []
# #for para pegar os divisores
# for i in range(1, num + 1):
#     if (num % i == 0):
#         lista.append(i)
#     else:
#         continue
# lista.pop()
# if (sum(lista) == num):
#     print('Ele é um numero perfeito!')
# else:
#     print('Ele não é um numero perfeito!')
# print(lista)


# #EX9 - # #EX10 - Verificar senha com regras REFAÇÃO DOS EXERCÍCIOS!
# num = '123456789'
# maiuscula = False
# minuscula = False
# numero = False
# tamanho = False
# while True:
#     senha = str(input('Digite sua senha: '))
#     for c in senha:
#         if (c.isupper()):
#             maiuscula = True
#         if(c.islower()):
#             minuscula = True
#         if (c in num):
#             numero = True
#         if (len(senha) >= 8):
#             tamanho = True
#     if(maiuscula  == True and minuscula == True and numero == True and tamanho == True):
#             print('Senha valida!')
#             print('Login acessado')
#             break
#     else:
#         print('Tente novamente!')
#         maiuscula = minuscula = tamanho = numero = False
#         continue


#EX10 -  verificar se um numero é primo REFAÇÃO DOS EXERCÍCIOS
# num = int(input('Numero: '))
# conta = 0
# if (num < 1):
#     print('Não é primo!')
# else:
#     for i in range(1, num+1):
#         if(num % i == 0):
#             conta = conta + 1
#     if (conta == 2 or num == 2):
#         print('Primo')
#         print(conta)
#     else:
#         print('Não é primo!')
#         print(conta)



# #EX11 - Sistema de hotel numa colônia de férias
# import os
# pessoas = int(input('Quantas pessoas ficaram hospedadas? '))
# tipo_apartamento = int(input('Qual o tipo do partamento (1/2)? '))
# qtd_dias = int(input('Quantos dia vocês vão ficar? '))
# if (pessoas > 6):
#     print('Não é possível essa quantidade de pessoa! ')
# else:
#     if (tipo_apartamento == 1):
#         if (pessoas == 1):
#             diaria = qtd_dias * 20
#         elif (pessoas == 2):
#             diaria = qtd_dias * 28
#         elif (pessoas == 3):
#             diaria = qtd_dias * 35
#         elif (pessoas == 4):
#             diaria = qtd_dias * 42
#         elif (pessoas == 5):
#             diaria = qtd_dias * 48
#         elif (pessoas == 6):
#             diaria = qtd_dias * 53
#     elif(tipo_apartamento == 2):
#         if (pessoas == 1):
#             diaria = qtd_dias * 25
#         elif (pessoas == 2):
#             diaria = qtd_dias * 34
#         elif (pessoas == 3):
#             diaria = qtd_dias * 42
#         elif (pessoas == 4):
#             diaria = qtd_dias * 50
#         elif (pessoas == 5):
#             diaria = qtd_dias * 57
#         elif (pessoas == 6):
#             diaria = qtd_dias * 63
#     else:
#         print('Esse tipo de apartamento não existe no nosso catálogo! ')
# print(f'O valor final a pagar pelas {qtd_dias} noites será de: {diaria}')



# #EX12 - SISTEMA DE HOTEL ATUALIZADO, MAIS COMPLEXO E COMPLETO
# from rich.console import Console
# from rich.table import Table
# import os
# while True:
#     try:
#         pessoas = int(input('Quantas pessoas ficaram hospedadas? '))
#         tipo_apartamento = int(input('Qual o tipo do partamento (1/2)? '))
#         qtd_dias = int(input('Quantos dia vocês vão ficar? '))
#         verificacao = False
#         if (pessoas > 6):
#             os.system('cls')
#             print('Não é possível essa quantidade de pessoa! ')
#             continue
#         else:
#             if (tipo_apartamento == 1):
#                 if (pessoas == 1):
#                     diaria = qtd_dias * 20
#                 elif (pessoas == 2):
#                     diaria = qtd_dias * 28
#                 elif (pessoas == 3):
#                     diaria = qtd_dias * 35
#                 elif (pessoas == 4):
#                     diaria = qtd_dias * 42
#                 elif (pessoas == 5):
#                     diaria = qtd_dias * 48
#                 elif (pessoas == 6):
#                     diaria = qtd_dias * 53
#                 verificacao = True
#             elif(tipo_apartamento == 2):
#                 if (pessoas == 1):
#                     diaria = qtd_dias * 25
#                 elif (pessoas == 2):
#                     diaria = qtd_dias * 34
#                 elif (pessoas == 3):
#                     diaria = qtd_dias * 42
#                 elif (pessoas == 4):
#                     diaria = qtd_dias * 50
#                 elif (pessoas == 5):
#                     diaria = qtd_dias * 57
#                 elif (pessoas == 6):
#                     diaria = qtd_dias * 63
#                 verificacao = True
#             else:
#                 os.system('cls')
#                 print('Esse tipo de apartamento não existe no nosso catálogo! ')
#                 continue

#         if (verificacao == True):
#             os.system('cls')
#             # Criando o console
#             console = Console()
#             # Exemplo de texto colorido e estilizado

#             console.print("Detalhes da sua Hospedagem!", style="bold white")

#             # Criando uma tabela
#             table = Table(title="")
#             table.add_column("Tipo Apartamento", justify="center", style="blue")
#             table.add_column("Quantidade de Pessoas", justify="center", style="purple")
#             table.add_column("Quantidade de dias hospedados", justify="center", style="red")
#             table.add_column("Valor final da hospedagem", justify="center", style="cyan")

#             # Adicionando uma linha de dados
#             table.add_row(str(tipo_apartamento),str(pessoas), str(qtd_dias), str(diaria))
#             console.print(table)
            
#         else:
#             continue

#         continuar = str(input('Deseja continuar? (s/n)? ')).upper()
#         if (continuar == 'S'):
#             # os.system('cls')
#             continue
#         elif (continuar == 'N'):
#             break

#     except ValueError as error:
#         os.system('cls')
#         print('Erro no Tipo de dado inserido')
#         print('tente denovo!')
#         print(error)


#Exercícios de IF e ELSE

#EX1 - Implemente um programa que receba a idade de uma pessoa e imprima mensagem de acordo com os critérios:Menor de 16 anos: MENOR Entre 16 e 18 anos: EMANCIPADO Maior de 18 anos: MAIOR
# idade = int(input('Digite sua idade: '))
# if (idade < 16):
#     print('Menor de idade')
# elif (idade > 16 and idade < 18):
#     print('Emancipado')
# else:
#     print('Maior de idade')

#EX2 - mplemente um programa que receba a idade de um nadador e imprima a sua categoria seguindo as regras:

# idade = int(input('Digite sua idade: '))
# if (idade >= 5 and idade <= 7):
#     print('Infatil A')
# elif (idade >= 8 and idade <= 10):
#     print('Infantil B')
# elif (idade >= 11 and idade <= 13):
#     print('Juvenil A')
# elif (idade >= 14 and idade <= 17):
#     print('Juvenul B')
# else: 
#     print('Profissional')


#EX3 - Verificar se um número é positivo ou negativo
# num = int(input('Numero: '))
# if (num > 0):
#     print('Numero positivo!')
# else:
#     print('Numero negativo!')

#EX4 - Verificar se o número é par ou ímpar
# num = int(input('Numero: '))
# if (num % 2 == 0):
#     print('Par')
# else:
#     print('Impar')

#EX5 - Faça o 4 com numeros float
# num = float(input('Numero: '))
# if (int(num) % 2 == 0):
#     print('Par')
# elif (int(num) % 2 == 1):
#     print('Impar')

#EX6 - Autenticação simples de senha e usuário
# user = str(input('Seu user: '))
# password = str(input('Sua senha: '))
# if (user == 'mariaruimnofort@gmail.com' and password == '123455'):
#     print('User e Pass validos!')
# else:
#     print('Password ou User incorretos!')

#EX7 - Leia a nota de um aluno (0-100) e informe a classificação
# nota = float(input('Digite sua nota: '))
# if (nota < 60 ):
#     print('F')
# elif (nota >=60 and nota <=  69):
#     print('D')
# elif (nota >= 70 and nota <= 79):
#     print('C')
# elif (nota >= 80 and nota <= 89):
#     print('B')
# elif (nota >= 90):
#     print('A')

#EX8 - Verificar ano bissexto
# ano = int(input('Informe o ano: '))
# if (ano % 4 == 0 and ano % 100 != 0):
#     print('Bissexto')
# else:
#     print('Não é bissexto')

#EX9 - Escolher opção do menu
# res = int(input('1 para suporte / 2 para sacar / 3 para consultar saldo / 4 para depositar: '))
# if (res == 1):
#     print('Suporte aí')
# elif (res == 2):
#     print('Sacar aí')
# elif (res == 3):
#     print('Saldo aí')
# elif (res == 4):
#     print('Depositar aí')

# #EX10 - Verificar senha com regras
# alpha = 'abcdefghijklmnopqrstuvwxyz'
# num = '123456789'
# while True:
#     senha = str(input('Digite sua senha: '))
    
#     if len(senha) >= 8:
#         print('Maior que 8')
#     else:
#         print('Senha muito curta.')
#         continue  # Pula o restante e pede para digitar novamente

#     minuscula = False
#     for c in alpha:
#         if c in senha:
#             minuscula = True
#             break
#     if not minuscula:
#         print('Tem que ter minuscula!')
#         continue
#     numero = False
#     for c in num:
#         if c in senha:
#             numero = True
#             break
#     if not numero:
#         print('Tem que ter numero')
#         continue
#     maiuscula = False
#     for c in alpha.upper():
#         if c in senha:
#             maiuscula = True
#             break
#     if not maiuscula:
#         print('Tem que ter maiuscula')
#         continue    
#     print('Senha valida!')
#     break

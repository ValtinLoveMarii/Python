#DUNDER MAIN


#EX1 - Importe o módulo math e use-o para calcular a raiz quadrada de um número.
# import math
# print(math.sqrt(9))

#EX2 - Importe o módulo random e gere um número aleatório entre 1 e 10.
# from random import randint as rdint
# print(rdint(1,10))


#EX3 - Importe datetime e mostre a data e hora atual.
# import datetime
# x = datetime.datetime.now()
# print(x)

#EX4 - Importe apenas a função sqrt do módulo math e calcule a raiz quadrada de 49.
# from math import sqrt
# print(sqrt(49))

#EX5 - Use a função dir() para listar todos os atributos do módulo math
# import math
# print(dir(math))

#EX6  - Crie um arquivo com uma função que retorna o dobro de um número.
# from pacote_modulo import func
# res = func.dobro(9)
# print(res)

#EX7 - Crie um módulo com funções de soma, subtração, multiplicação e divisão.
# from pacote_modulo import func
# res = input(('Somar[1]\nSubtrair[2]\nDividir[3]\nMultiplicar[4]\n'))
# if res == '1':
#     resposta = func.somar(9,34)
#     print(resposta)
# elif res == '2':
#     resposta = func.sub(9,3)
#     print(resposta)
# elif res == '3':
#     resposta = func.div(129,12)
#     print(resposta)
# elif res == '4':
#     resposta = func.multi(12,7)
#     print(resposta)
# else:
#     print('N tem essa ')

#EX8 - Usar módulos dentro de pasta(pacotes)
# from pacote_modulo import func
# res = func.somar(1,9)
# print(res)

#EX9 - Usar módulos dentro de pasta com outra pasta dentro (sub-pacotes)
# from pacote_modulo.mini_pacote import mini_func
# numero = int(input('Numero: '))
# res = mini_func.imprimir(f'Teclado gamer a {numero} reais corre que ainda tem!')
# print(res)

#EX10 - Criar um arquivo calculadora e usar o dunder main
# from calculadora import somar, multi
# somar(10, 6)
# multi(12, 2)

#EX11 - Sistema de login com módulos: Crie um módulo usuarios.py que guarda e valida usuários.Crie um script principal que usa esse módulo para logar ou registrar novos usuários.
from usuario import login, cadastrar
users = {}
while True:
    if len(users) == 0:
        print('Não existe seu user no noso sistema, por favor cadastre-se!')
        cadastrar(users)
    else:
        resp = str(input('Logar ou Cadastrar: ')).lower()
        if resp == 'logar':
            res_name, res_pass = login()
            if res_name in users and res_pass == users[res_name]:
                print('User correto!')
                break
            else:
                print('Tente Novamente user incorreto!')
        elif resp == 'cadastrar':
            cadastrar(users)
            continue
        else:
            break
print(users)
        
# if res_name in users and res_pass in users:
#     print('usuário correto!')
# else:
#     users.update({res_name:res_pass})
# print(users)

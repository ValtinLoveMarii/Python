#AULA 31 - Módulos
# import exe1 as e
# res = e.function(12,12)
# print(res)

# import random as rd #ou from random import randint -- PEGA só a func RANDINT ou from random import * -- IMPORTA TODAS AS func do RANDOM
# print(rd.randint(1, 9))
# print(rd.choice([1,3,4,5,1,12]))
# print(rd.gauss())

# from pacote_modulo import func, func2
# from pacote_modulo.mini_pacote import mini_func
# print(func.somar(8,6))
# print(func2.mult(8,12))
# res  = mini_func.imprimir('naruto muito toppppp')
# print(res)

#DUNDER DOCSTRING
__doc__ = '''Esse módulo serve para a aula de MÓDULOS
retorna os assuntos tratados na aula
            Assuntos:
                Dunder __name__
                Dunder __main__
                Dunder __doc__
            Dia: 
                17/05/2025
''' #-> Descreve a utilidade do módulo
print(__doc__)
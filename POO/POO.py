# AULA 33 - POO
# PARADIGMA IMPERATIVO

# IMPERATIVO PASSO A PASSO, ITERAÇÃO E DECISÃO
# a = 8
# b = 1
# soma = a + b
# if a - b == 7:
#     print('Naruto')
    
# #PROCEDURAL - CRIAÇÃO E REUTILIZAÇÃO DE FUNÇÕES
# def somar(a, b):
#     return a + b
# def mostrar():
#     print(somar(1, 9))
# mostrar()

# #ESTRUTURADO - CRIAÇÃO DE SINTAXE BEM DEFINIDA E BONTIA  
# if a == 1:
#     print('Meu amigo')
    
    
# #IMPERATIVO "COMPLETO"
# def registrar(nome, idade):
#     paciente = {'nome':nome, 'idade': idade}
#     return paciente

# paciente = registrar('Naruto Antonieta',92)
# print(paciente)


#POO - Classes e Objetos
class Carro():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def andar(self):
        print(f'ANDANDO...... {self.marca}') 

carro1 = Carro('Mercedes', 'Benz')
carro1.andar()
carro2 = Carro('Ferrari', 'Veneno')
carro2.andar()
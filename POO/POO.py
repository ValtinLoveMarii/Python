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

class Conta():
    #ATRIBUTO DE CLASSE
    taxa = 0.50
    #METODO DE CLASSE
    @staticmethod
    def retornarCodigoBanco():
        print('Código: 345')
        
    
    """Atributos de Instâncias""" # --> Construtor
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        

    def extrato(self): # --> Método/Função
        self.saldo -= Conta.taxa
        print(f'Saldo: {self.saldo}')
    
    def depositar(self, valor): # --> Método/Função
        self.saldo += valor
        print(f'Novo saldo: {self.saldo}')
    
    def sacar(self, sacar): # --> Método/Função
        if sacar > self.saldo:
            print(f'Saldo Insuficiente para sacar!')
        else:
            self.saldo -= sacar


c1 = Conta(1, 'Finn', 1800)
c2 = Conta(2, 'Jake', 3400)


Conta.retornarCodigo() # --> MÉTODO DA CLASSE

Conta.retornarCodigoBanco() # --> MÉTODO ESTÁTICO


#ATRIBUTO DINAMICO
# c2.signo = 'Peixes' # -> Atributo Dinamico criado somente para o c2
# -> print(c2.__dict__) 


# CLASSE PARA HOSPITAL
from datetime import date
class Paciente():
    @classmethod
    def idadeAnoNascimento(cls, nome,anoNascimento, cpf, email):
        idade = date.today().year - anoNascimento
        return cls(nome, idade, cpf, email)
        
    def __init__(self, nome, idade, cpf, email):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email
        
	
# pac = Paciente('Mona', 89, '000.222.000', 'monaadwadawd')
# print(pac.__dict__)

# print(Paciente.idadeAnoNascimento(2001))

pac = Paciente.idadeAnoNascimento('Mona', 1957, '000.222.000', 'monaadwadawd')
print(pac.__dict__)
print(pac.idade)

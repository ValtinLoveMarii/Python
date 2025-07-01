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


"""
Visibilidade - Modificador de Acesso
privada (private) -> restritiva  -> Os atributos so podem ser mudados dentro da classe
protegida (protected) ->  intermediaria -> Atributos so podem ser manipulados dentro da classe e nas sub-classes ou que herdam os atributos e metododos
pubica (public) -> livre -> Os atributos e metodos podem ser utilizados em qualquer lugar(parte do código)
"""

class Private():
    def __init__(self, saldo, nome, idade):
        self.__saldo = saldo # --> Atributo PRIVADO, SÓ PODE SER USADO NESSA CLASE 'PRIVATE'
        self.nome = nome # --> Atributo PUBLICA, PODE SER ACESSADO POR TODOS
        self._idade = idade # --> Atributo PROTEGIDA, SÓ PODE SER USADO PELA CLASSE E SUB-CLASSES E AS QUE HERDAM ESSA CLASSE
    def show(self):
        print(self.__saldo)
        print(self._idade)



"""
NAME MANGLING
"""
class Quadrado():
    def __init__(self, lado):
        self.__lado = lado
    
    def area(self):
        print(self.__lado * self.__lado)
        
q1 = Quadrado(2)
q1.area()
q1.__lado = 999 # --> ATRIBUTO DINÂMICO
q1.area()
print(q1.__dict__)
q1._Quadrado__lado = 12 # --> NAME MANGLING
q1.area()

"""
ENCAPSULAMENTO
"""
class Conta():
    def __init__(self, titular,numero, saldo):
        self.titular = titular
        self.__numero = numero
        self.__saldo = saldo
        self.__historico = []
    
    def retornar_saldo(self):
        print(f'Saldo: {self.__saldo}')  

    
    def transacao(self,saldo):
        self.__historico.append(saldo)
    
    def extrato(self): # --> Método/Função
        print('---EXTRATO---')
        print(f"Conta: {self.titular}")
        for saldo in self.__historico:
            print(f'Saldo: {saldo}')
    
    def depositar(self, valor): # --> Método/Função
        self.__saldo += valor
        self.transacao(self.__saldo)
    
    def sacar(self, sacar): # --> Método/Função
        if sacar > self.__saldo:
            print(f'Saldo Insuficiente para sacar!')
        else:
            self.__saldo -= sacar
            self.transacao(self.__saldo)
    
    def transferir(self, valor,destino):
        self.sacar(valor)
        destino.depositar(valor)



c1 = Conta('Bolso', 123, 900)
c2 = Conta('lula', 345, 2000)

c1.transferir(300, c2)
c1.transferir(100, c2)
c1.extrato()


# c1.sacar(500)
# c1.depositar(100)
# c1.saldo()


"""
GETTERS E SETTERS, USADO PARA GET(RETORNAR O VALOR DE UM ATRIUBUTO) SET(COLOCAR VALOR EM UM ATRIBUTO)
AJUDA NO REUSO E MANUTENÇÃO E NO ENCAPSULAMENTO DO CÓDIGO
"""

class Conta():
    def __init__(self, titular, numero, saldo):
        self.titular = titular
        self.__numero = numero
        self.__saldo = saldo
        self.__historico = []
        self.__historico_saldoConta = [saldo]
    
    """GET E SET NUMERO"""
    @property # --> GET NUMERO - RETORNAR O NUMERO
    def numero(self):
        return self.__numero
    
    @numero.setter # --> SET NUMERO - ALTERA O NUMERO
    def numero(self, numero):
        self.__numero = numero
    
    """GET E SET SALDO"""
    @property # --> GET SALDO - RETORNAR O SALDO
    def saldo(self):
        return self.__saldo
    
    @saldo.setter # --> SET SALDO - ALTERA O SALDO
    def saldo(self, saldo):
        self.__saldo = saldo
        
    """MÉTODOS APÓS O GET E SET"""
    
    def sacar(self, valor):
        self.saldo -= valor
        self.transacao_conta(valor)
        self.valor_conta_atual(self.saldo)
            
    def depositar(self, valor):
        self.saldo += valor
        self.transacao_conta(valor)
        self.valor_conta_atual(self.saldo)
    
        
    def retornar_saldo(self):
        print(f'Saldo Atual: {self.saldo}') 
        
    def trasnferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
    
    def transacao_conta(self, saldo):
        self.__historico.append(saldo)
        
    def valor_conta_atual(self,valor):
        self.__historico_saldoConta.append(valor)
    
    def historico_transferencia(self):
        for x in self.__historico:
            print(f'Transição feita R${x}')
        
    def historico_saldo(self):
        for x in self.__historico_saldoConta:
            print(f'Saldo na Conta: {x} {self.titular}')


# c1 = Conta('Valtin', 1, 3200)
# c2 = Conta('MariBB', 2, 4000)
# c1.trasnferir(200, c2)
# c1.historico_transferencia()
# c1.historico_saldo()
# c2.historico_transferencia()
# c2.historico_saldo()

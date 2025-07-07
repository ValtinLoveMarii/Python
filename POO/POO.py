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
privada (private) -> restritiva  -> Os atributos so podem ser mudados dentro da classe e subclasses
protegida (protected) ->  intermediaria -> Atributos so podem ser manipulados dentro da classe e nas sub-classes, mas por fora pode mas é errado
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


"""HERANÇA"""

"""SUPERCLASSSE - CLASSE MÃE"""
class Base(): # --> CLASSE BASE QUE TEM ATRIBUTOS COMUNS EM OUTRAS CLASSES
    def __init__(self, nome, idade, rg, cpf, sexo):
        self._nome = nome
        self._idade = idade
        self._rg = rg
        self._cpf = cpf
        self._sexo = sexo
    
    """GET E SET"""
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self._idade
    
    @property
    def rg(self):
        return self._rg

    @property
    def cpf(self):
        return self._cpf
    
    @property
    def sexo(self):
        return self._sexo

"""SUBCLASSE - CLASSE FILHA"""
class Aluno(Base): # --> A CLASSE ALUNO HERDOU A CLASSE BASE, OU SEJA TODOS OS ATRIBUTOS E MÉTODOS DE BASE PODEM ESTAR NO ALUNO AGORA
    def __init__(self, rgm, ano, curso, nome, idade, rg, cpf, sexo): # --> AQUI ELE RECEBE OS DADOS DOS ATRIBUTOS E JA PASSA OS CERTO PARA A CLASSE MAE(SUPERCLASSE)
        super().__init__(nome, idade, rg, cpf, sexo) # --> AQUI ELE HERDOU TODOS OS ATRIBUTOS DA SUPERCLASSE
        self.__rgm = rgm
        self.__ano = ano
        self.__curso = curso
    
    """GET E SET de ALUNO(atributos específicos de ALUNO(rgm, ano, curso) )"""
    @property
    def rgm(self):
        return self.__rgm
    
    @property
    def ano(self):
        return self.__ano
    
    @property
    def curso(self):
        return self.__curso
    
    def mostrar(self):
        print(f'Aluno: {self.nome}, idade: {self.idade}')


"""SUBCLASSE - CLASSE FILHA"""
class Professor(Base):
    def __init__(self, materia, salario, nome, idade, rg, cpf, sexo):
        super().__init__(nome, idade, rg, cpf, sexo)
        self._materia = materia
        self._salario = salario
        self._carga = 10
    
    @property
    def materia(self):
        return self._materia
    
    @property
    def salario(self):
        return self._salario
    
    @property
    def carga(self):
        return self._carga
    
    def mostrar(self):
        print(f'Professor: {self.nome}, idade: {self.idade}, carga: {self.carga}, salario: {self.salario}')
# a1 = Aluno(1, 7, 'Ti', 'Valquiria', 23, 238890, 5499, 'F')
# a1.mostrar()
# p1 = Professor('MAT', 10000, 'Oscar', 56, 889900, 29988, 'M')
# p1.mostrar()

"""POLIMORFISMO"""
class Animal():
    def __init__(self):
        pass
    """DEF FALAR PARA O POLIMORFISMO"""
    def falar(self):
        raise NotImplemented('Essa bomba aqui não é pra voce acessar nao o caraio')

class Cachorro(Animal):
    def __init__(self):
        pass
    
    def falar(self):
        print('Barulho do cachorro')

class Gato(Animal):
    def __init__(self):
        pass
    
    def falar(self):
        print('Barulho do gato')

# cachorro = Cachorro()
# gato = Gato()
# cachorro.falar()
# gato.falar()


"""CLASSE ABSTRATA"""
#abstratas - Não são instânciadas, não seram criados objetos da classe
from abc import ABC, abstractmethod
class Pessoa(ABC):
    def __init__(self, nome, sexo):
        self.nome = nome
        self.sexo = sexo
        
    @abstractmethod
    def falar(self):
        pass

class Professor(Pessoa):
    def __init__(self, nome, sexo=''):
        super().__init__(nome, sexo='12')
    
    def ler(self):
        print('LER', self.idade, self.nome)
    def falar(self):
        print('LER',  self.nome, self.sexo)
        
# p1 = Professor('pintomole')
# p1.falar()


class Pagamento(ABC):
    def __init__(self, pagamento):
        self.pagamento = pagamento
        
    @abstractmethod
    def pagar(self):
        pass

class Pix(Pagamento):
    def __init__(self, pagamento):
        super().__init__(pagamento)
    
    def pagar(self):
        print('PAGOU COM O PIX')
# pix1 = Pix('Fazer o pix')
# pix1.pagar()

"""HERANÇA MULTIPLA"""
class Funcionario():
    def falar(self):
        print('Trabalhando')


class Front(Funcionario):
    def __init__(self):
        super().__init__()
    def falar(self):
        print('Trabalhar Front-End')
        
class Back(Funcionario):
    def falar(self):
        print('Trabalhar Back-End')

class Full(Back, Front):
    # def falar(self):
    #     print('FULL')
    pass
      
# f1 = Front()
# b1 = Back()
# f1.falar()
# b1.falar()

# ana = Full()
# ana.falar()

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
class Registrar():
    def __init__(self, nome, idade , cpf, email):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email
    def registrar_paciente(self, dic):
        dic.update({'Nome':self.nome, "Idade":self.idade, 'Cpf':self.cpf, 'E-mail':self.email})
        return dic
    
    def verificar_paciente(self):
        if self.idade >= 60:
            print('Grupo de Risco......')
        elif self.idade < 60 and self.idade >= 30:
            print('Ta de boa demais......')
        elif self.idade < 30 and self.idade > 0:
            print('Neném nem precisa se preocupar....')
    

dic = {}
paciente1 = Registrar('Pedro', 60, '121220-1', 'pepedogremio@gmail.com')
paciente1.registrar_paciente(dic=dic)
paciente1.verificar_paciente()
print(dic)

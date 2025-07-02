#EX1 - Crie uma classe Dado que sorteia um número de 1 a 6. Crie outra classe Jogo que permite jogar o dado 5 vezes e mostrar a soma total.
from random import randint
class Dado():
    def __init__(self):
        self.__lado = randint(1, 6)
    
    @property
    def lado(self):
        return self.__lado

class Jogo():
    def __init__(self):
        self.__dado = Dado()
        self.__soma = []
        self.__ladosTirados = []
    
    """"GET e SET"""
    @property
    def ladosTirados(self):
        return self.__ladosTirados
    
    @property
    def soma(self):
        return self.__soma
    
    @property
    def dado(self):
        return self.__dado
    
    def jogar(self):
        valor = self.dado.lado
        for x in range(5):
            self.soma.append(valor)
            self.ladosTirados.append(valor)
        print(sum(self.soma))
        print(self.ladosTirados)


# d1 = Dado()
# j1 = Jogo()
# j1.jogar()

#EX2 - Crie uma classe Votacao com um dicionário interno para contar votos em opções. Métodos: votar(opcao) resultado()
import random
class Voto():
    def __init__(self):
        self.__voto = ['A', 'B']

    
    @property
    def vot(self):
        return random.choice(self.__voto)
    
class Votacao():
    def __init__(self):
        self.__voto = Voto()
        self.__listaVotos = {'A':0, 'B':0}
    
    """GET"""
    @property
    def voto(self):
        return self.__voto
    
    @property
    def listaVotos(self):
        return self.__listaVotos
    

    def votar(self):
        for x in range(5):
            valor = self.voto.vot
            if valor == 'A':
                self.listaVotos[valor] += 1
            elif valor == 'B':
                self.listaVotos[valor] += 1
    
    def resultado(self):
        pass

#EX3 - Crie uma classe base chamada Veiculo com os atributos: marca modelo ano Adicione também um método mostrar_info que imprima os dados do veículo. Depois, crie uma subclasse chamada Carro que herde de Veiculo e adicione um atributo: numero_de_portas Implemente o método mostrar_info na subclasse para incluir também o número de portas do carro.
class Veiculo():
    def __init__(self, marca, modelo, ano):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
        
    def mostrar_info(self, marca, modelo, ano, portas):
        print(f'Marca:{marca}, Modelo:{modelo}, Ano:{ano}, Portas:{portas}')
        
class Carro(Veiculo):
    def __init__(self, portas,marca, modelo, ano):
        super().__init__(marca, modelo, ano)
        self._portas = portas
        
    def mostrar_info(self):
        super().mostrar_info(self._marca, self._modelo, self._ano, self._portas)
        
# c1 = Carro(4, 'Mercedes', 'Benz', 2025)
# c1.mostrar_info()

#EX4 - Crie uma classe base chamada Funcionario com os seguintes atributos privados nome  salario Crie getters e setters para esses atributos. Em seguida, crie uma subclasse chamada Gerente, que herda de Funcionario e adicione um atributo privado: bonus Adicione um getter e setter para o atributo bonus na subclasse.
class Funcionario():
    def __init__(self, nome, salario):
        self._nome = nome
        self._salario = salario
    
    """GET e SET"""
    @property
    def nome(self):
        return self._nome
    
    @property
    def salario(self):
        return self._salario
    
class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self._bonus = bonus
    
    """GET e SET"""
    @property
    def bonus(self):
        return self._bonus
    
    def salario_gerente(self):
        print(f'Salário gerente: {self.salario + self.bonus}')
        
# g1 = Gerente('Edvander', 12000, 500)
# g1.salario_gerente()

#EX4 - Crie uma classe base chamada Produto com os atributos: nome preco Em seguida, crie uma subclasse chamada ProdutoImportado que herde de Produto e adicione o atributo: taxa_imposto Na subclasse, crie um método preco_final que calcule o preço final do produto considerando o imposto (taxa de imposto sobre o preço).
class Produto():
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @property
    def nome(self):
        return self._nome
    
    @property
    def preco(self):
        return self._preco
class Importado(Produto):
    def __init__(self, nome, preco):
        super().__init__(nome, preco)
        self._taxa = 2
    @property
    def taxa(self):
        return self._taxa
    
    def preco_final(self):
        print(f'Preço final: {self.preco + self.taxa}')

# p = Importado('Leite', 9)
# p.preco_final()

#EX5 - Crie uma classe base chamada Pessoa com os atributos: nome cpf (esse atributo deve ser privado) Na subclasse Aluno, crie um método mostrar_dados para exibir o nome e o CPF do aluno. Contudo, use o getter para acessar o cpf, e o setter para alterá-lo.
class Pessoa():
    def __init__(self, nome, cpf):
        self._nome = nome
        self.__cpf = cpf
    
    """GET e SET"""
    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf

class Aluno(Pessoa):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)
    
    def mostrar_dados(self):
        print(self.cpf)
        
# a1 = Aluno('Alex', 999001)
# a1.mostrar_dados()

#EX6 - BANCO DO MINE
class Base():
    def __init__(self, nome, idade, cpf, sexo):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf
        self.__sexo = sexo
    
    
    """GET"""
    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def sexo(self):
        return self.__sexo
    
class ClientePF(Base):
    def __init__(self, nome, idade, cpf, sexo, profissao):
        super().__init__(nome, idade, cpf, sexo)
        self.__profissao = profissao
    
    """GET"""
    @property
    def profissao(self):
        return self.__profissao

class ClientePJ(Base):
    def __init__(self, nome, idade, cpf, sexo, razao_social):
        super().__init__(nome, idade, cpf, sexo)
        self.__razao_social = razao_social

    """GET"""
    
    @property
    def razao_social(self):
        return self.__razao_social

class OrgaoPublico(Base):
    def __init__(self, nome, idade, cpf, sexo, esfera_governo):
        super().__init__(nome, idade, cpf, sexo)
        self.__esfera_governo = esfera_governo



#EX7 - Exercício 8: Sistema de Transporte Classe base: Transporte capacidade velocidade_maxima Subclasses: Onibus: tem numero_de_passageiros Caminhao: tem carga_maxima Crie o método exibir_dados() na classe base e use nas subclasses.

class Transporte():
    def __init__(self, capacidade, velo_maxima):
        self.__capacidade = capacidade
        self.__velo_maxima = velo_maxima
    

    def exibir_dados(self, capacidade, velo_maxima, *args):
        print(f'{capacidade}, {velo_maxima}, {args[0]}')

    """GET"""
    @property
    def capacidade(self):
        return self.__capacidade
    
    @property
    def velo_maxima(self):
        return self.__velo_maxima

class Onibus(Transporte):
    def __init__(self, capacidade, velo_maxima, passageiros):
        super().__init__(capacidade, velo_maxima)
        self.__passageiros = passageiros
    

    """"GET"""
    @property
    def passageiros(self):
        return self.__passageiros
    
    def mostrar_dados(self):
        self.exibir_dados(self.capacidade, self.velo_maxima, self.passageiros)


# o1 = Onibus(44, 120, 12)
# o1.mostrar_dados()

class Caminhao(Transporte):
    def __init__(self, capacidade, velo_maxima, carga_maxima):
        super().__init__(capacidade, velo_maxima)
        self.__carga_maxima = carga_maxima

    """GET"""
    @property
    def carga_maxima(self):
        return self.__carga_maxima
    
    
    def mostrar_dados(self):
        super().exibir_dados(self.capacidade, self.velo_maxima, self.carga_maxima)

# c1 = Caminhao(12, 100, 2000)
# c1.mostrar_dados()

#EX8 - Classe base: Pessoa nome cpf Subclasses: Aluno: matrícula e curso Funcionario: cargo e salário Crie uma lista com objetos misturados e imprima os dados de todos usando apenas os métodos da classe base.
class Pessoa():
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    """GET"""
    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf
    
    def mostrar(self, *args):
        print(args)
    
class Aluno(Pessoa):
    def __init__(self, nome, cpf, matricula, curso):
        super().__init__(nome, cpf)
        self.matricula = matricula
        self.curso = curso
    
    def mostrar(self):
        super().mostrar(self.nome, self.cpf, self.matricula, self.curso)
# a1 = Aluno('DAN', 99012, 1012, 'TI')
# a1.mostrar()
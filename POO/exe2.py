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
        self.votar()
        print(self.listaVotos)
        if self.listaVotos['A'] > self.listaVotos['B']:
            print('A ganhou')
        else:
            print('B ganhou')
v1 = Voto()
votocao = Votacao()
votocao.resultado()
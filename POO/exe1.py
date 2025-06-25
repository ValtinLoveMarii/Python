#EX1 - Crie uma classe Pessoa que tenha: Atributos: nome, idade Um método apresentar() que imprime: "Olá, meu nome é <nome> e tenho <idade> anos."
class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def apresentar(self):
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos')
    
# pessoa1 = Pessoa('Danilo', 42)
# pessoa1.apresentar()

#EX2 - Classe Produto Crie uma classe Produto com: Atributos: nome, preco Um método exibir_info() que imprime os dados do produto.

class Produto():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def exibir_info(self):
        print(f'Produto: {self.nome} - Preço: {self.preco}')
        
# produto1 = Produto('Mouse', 210)
# produto1.exibir_info()

#EX3 - Crie uma classe Retangulo com: Atributos: largura, altura Métodos: area() → retorna a área perimetro() → retorna o perímetro
class Retangulo():
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        
    def area(self):
        area = self.largura * self.altura
        print(f'ÁREA: {area}')
    
    def perimetro(self):
        altura = self.altura * 2
        largura = self.largura * 2
        print(f'PERÍMETRO: {altura+largura}')
        
# retangulo1 = Retangulo(7, 5)
# retangulo1.area()
# retangulo1.perimetro()

#EX4 - Crie uma classe Aluno com: Atributos: nome, notas (lista de 3 notas) Métodos: media() → retorna a média das notas situacao() → retorna "Aprovado" se média ≥ 6, senão "Reprovado"
class Aluno():
    def __init__(self, nome, notas=[]):
        self.nome = nome
        self.notas = notas
    def media(self):
        media = sum(self.notas) / len(self.notas)
        print(f'MÉDIA {self.nome} - {media:.2f}')
    def situacao(self):
        media = sum(self.notas) / len(self.notas)
        if media >= 6:
            print(f'APROVADO!')
        else:
            print(f'REPROVADO...')
            
# aluno1 = Aluno('Miguel', [10,9,8])
# aluno1.media()
# aluno1.situacao()

#EX5 - Crie uma classe ContaBancaria com: Atributos: titular, saldo Métodos: depositar(valor) sacar(valor) (não permitir sacar mais do que o saldo) extrato() → imprime o titular e saldo atual
class  ContaBancaria():
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        
    def depositar(self, valor):
        self.saldo += valor
        
    def sacar(self, valor):
        if valor >= self.saldo:
            print(f'Valor de saque INSUFICIENTE!')
        else:
            self.saldo -= valor

    def extrato(self):
        print(f'Sr.{self.titular}, Saldo: {self.saldo}')
        
# conta1 = ContaBancaria('Calango', 3400)        
# conta1.depositar(400)
# conta1.sacar(230)
# conta1.extrato()


#EX6 - Criar Produto e Carrinho
class Produto():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
class CarrinhoCompras():
    def __init__(self):
        self.lista = []

    def add_item(self, valor):
        self.lista.append(valor)

    def read_values(self):
        for x in self.lista:
            print(f'{x.nome} - Valor: {x.preco}')

    def sum_values(self):
        total = 0
        for x in self.lista:
            total = x.preco + total
        print(f'total - {total}')

# produto1 = Produto('leite', 2)
# produto2 = Produto('carne', 5)
# produto3 = Produto('manteiga', 3)

# carrinho = CarrinhoCompras()
# carrinho.add_item(produto1)
# carrinho.add_item(produto2)
# carrinho.add_item(produto3)

# carrinho.read_values()
# carrinho.sum_values()

#EX7 - Crie uma classe com métodos para somar, subtrair, multiplicar e dividir dois números. Os valores devem ser passados ao instanciar o objeto, e os métodos devem retornar os resultados.
class Calculadora():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def somar(self):
        print(f'A soma entre {self.num1} e {self.num2} é {self.num1 + self.num2}')

    def subtrair(self):
        print(f'A diferença entre {self.num1} e {self.num2} é {self.num1 - self.num2}')

    def mult(self):
        print(f'O produto entre {self.num1} e {self.num2} é {self.num1 * self.num2}')

    def divi(self):
        print(f'A divisao entre {self.num1} e {self.num2} é {self.num1 / self.num2}')

# item1 = Calculadora(9, 2)
# item1.somar()
# item1.subtrair()
# item1.mult()
# item1.divi()

#EX8 - Crie uma classe CaixaMensagem que guarda uma lista de mensagens: Métodos: enviar_mensagem(texto) listar_mensagens() limpar_caixa()
import os
class Mensagem():
    def __init__(self, msg):
        self.msg = msg
    
    def send(self):
        print(f'Mensagem Enviada')

    def list_msg(self):
        print(self.msg)

    def clear(self):
        input('Enter para limpar...')
        os.system('cls')
        print('Limpado')

# msg1 = Mensagem('Naruto é brabo')
# msg1.send()
# msg1.list_msg()
# msg1.clear()

#EX9 - Crie a classe Musica com titulo, artista, duracao.Crie a classe Playlist que pode: Adicionar músicas. Mostrar todas as músicas. Calcular tempo total da playlist.
class Spotify_Music():
    def __init__(self, title, singer, time):
        self.title = title
        self.singer = singer
        self.time = time

class Playlist():
    def __init__(self):
        self.play = {}

    def add_music(self, valor):
        self.play.update({valor.title: [valor.singer, valor.time]})

    def show_playlist(self):
        for x,z in self.play.items():
            print(f'Artista: {x} - Music {z}')
# music1 = Spotify_Music('Rap Jinx', 'TvJinx', 5)
# music2 = Spotify_Music('Rap Vi', 'TvJinx', 4)

# playlist1 = Playlist()
# playlist1.add_music(music1)
# playlist1.add_music(music2)
# playlist1.show_playlist()

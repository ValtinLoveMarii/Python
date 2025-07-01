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


#EX10 - PROJETO ANALISE DE DADOS BASICO Consiste em uma analise sobre uma loja
vendas = [
    {'dia': 'segunda', 'produto': 'camiseta', 'quantidade': 72, 'preco_unitario': 50},
    {'dia': 'segunda', 'produto': 'calça', 'quantidade': 1, 'preco_unitario': 120},
    {'dia': 'terça', 'produto': 'camiseta', 'quantidade': 5, 'preco_unitario': 50},
    {'dia': 'quarta', 'produto': 'tênis', 'quantidade': 12, 'preco_unitario': 200},
    {'dia': 'quarta', 'produto': 'calça', 'quantidade': 9, 'preco_unitario': 120},
    {'dia': 'quinta', 'produto': 'camiseta', 'quantidade': 11, 'preco_unitario': 250},
    {'dia': 'sexta', 'produto': 'tênis', 'quantidade': 71, 'preco_unitario': 200},
    {'dia': 'sexta', 'produto': 'oculos', 'quantidade': 19, 'preco_unitario': 20},
]


#ANALISE
class AnaliseQtd():
    def __init__(self, vendas):
        self.vendas = vendas
        self.total_prods = {}
        self.final_list = {}
        self.maior_prod = 0
    
    def qtd_vendas(self):
        for x in self.vendas:
            produto = x['produto']
            if produto not in self.total_prods:
                self.total_prods.update({produto:x['quantidade']})
            else:
                valor_inicial = self.total_prods[produto]
                valor_novo = valor_inicial + x['quantidade']
                self.total_prods.update({produto:valor_novo})
                
        # print(self.total_prods)
    
    def listar_produtos(self):
        for prod, valor in self.total_prods.items():
            print(f'Produto: {prod} - Quantidade: {valor}')
    

    def total_preco_produto(self):
        total_preco = {}
        for x in self.vendas:
            produto = x['produto']
            valor = x['preco_unitario']
            if produto not in total_preco:
                total_preco.update({produto:valor})
            else:
                valor_inicial = total_preco[produto]
                valor_final = valor_inicial + valor
                total_preco.update({produto:valor_final})
        
        for i,z in self.total_prods.items():
            preco_prod = total_preco[i]
            qtd_prod = z

            self.final_list.update({i:preco_prod*qtd_prod})

        print(self.final_list)

    def melhor_produto(self):
        maior = 0
        for x,z in self.final_list.items():
            if z > maior:
                maior = z
                maior_produto = x
            else:
                continue
        print(f'Item com o maior valor de venda: {maior_produto}')

            

# v1 = AnaliseQtd(vendas)
# v1.qtd_vendas()
# v1.listar_produtos()
# v1.total_preco_produto()
# v1.melhor_produto()

#EX11- Crie uma classe Livro com atributos titulo, autor, preco, estoque. Crie métodos para adicionar e remover do estoque, e para mostrar as informações do livro.
class Livro():
    def __init__(self, titulo, autor, preco):
        self.titulo = titulo
        self.autor = autor
        self.preco = preco

class Biblioteca():
    def __init__(self):
        self.estoque = {}
    
    def add_book(self, valor):
        self.estoque.update({valor.titulo:[valor.autor, valor.preco]})
        print(self.estoque)
    
    def remove_book(self, valor):
        self.estoque.pop(valor.titulo)
        print(self.estoque)
        
    def read_book(self):
        for x,z in self.estoque.items():
            print(f'Livro - {x} - Autor: {z[0]} - Preço: {z[1]}')

# l1 = Livro('As desumildade mata', 'JovemMilo', 12)
# estoque = Biblioteca()
# estoque.add_book(l1)
# estoque.read_book()
# estoque.remove_book(l1)


#EX12 - Crie uma classe Carro com atributos modelo, consumo_por_km, e combustivel. Crie métodos para abastecer e dirigir (reduz o combustível com base na distância e no consumo).
class Carro():
    def __init__(self, modelo, consumo_km, combustivel):
        self.modelo = modelo
        self.consumo_km = consumo_km
        self.combustivel = combustivel
    
    def abastecer(self, valor):
        valor = valor + self.combustivel
        print(f'Novo valor no tanque: {valor}')
    
    def dirigir(self, valor):
        valor = self.consumo_km * valor
        print(f'Gastou isso de combustível: {valor}')
    
# car1 = Carro('fiat', 2, 20)
# car1.abastecer(23)
# car1.dirigir(200)

#EX13 - Classe Agenda de Contatos Crie uma classe Contato com nome, telefone, email. Crie uma classe Agenda que guarda vários contatos em uma lista e permite: adicionar contato remover contato pelo nome buscar contato pelo nome listar todos os contatos.
class Contato():
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.lista_contato = {}
    
    def add_cont(self, valor):
        self.lista_contato.update({valor.nome:[valor.telefone, valor.email]})
        # print(self.lista_contato)
        
    def list_cont(self):
        for x,z in self.lista_contato.items():
            print(f'Contato: {x} - {z}')
    
# c1 = Contato('Superman', 9991212, 'super@fadwad')
# c1.add_cont(c1)
# c1.list_cont()

#EX14 - Crie uma classe chamada ContaBancaria que simula uma conta bancária. A classe deve ter os seguintes atributos e métodos: saldo (float): o saldo da conta. titular (string): o nome do titular da conta. Métodos: depositar(valor): Método para depositar um valor na conta. O valor deve ser positivo. sacar(valor): Método para sacar um valor da conta. O valor deve ser positivo e o saldo deve ser suficiente para o saque.

class Conta():
    def __init__(self, saldo, titular):
        self.__saldo = saldo
        self.titular = titular
        self.__historico = []
    
    def sacar(self, valor):
        self.__saldo -= valor
        self.atualizar_extrado(self.__saldo) # --> CHAMA a FUNÇÃO atualizar_extrato, e passa o valor do parametro dela, que seria o saldo após a alteração
    
    def depositar(self, valor):
        self.__saldo += valor
        self.atualizar_extrado(self.__saldo) # --> CHAMA a FUNÇÃO atualizar_extrato, e passa o valor do parametro dela, que seria o saldo após a alteração
    
    def tranferir(self, valor, destino):
        if valor > self.__saldo:
            print(f'Saldo Insuficiente para Enviar!')
        else:
            self.sacar(valor)
            destino.depositar(valor)
        
    def saldo_atual(self):
        print(f'Saldo: {self.__saldo}')
    
    def extrado(self):
        for i in self.__historico:
            print(f'---EXTRATO {self.titular}---')
            print(f'Saldo Atual: {i}')
    
    def atualizar_extrado(self,saldo):
        self.__historico.append(saldo)
        
# c1 = Conta(3000,'Gabo')
# c2 = Conta(4000, 'Dedé')
# c1.tranferir(300, c2) # --> GABO TRANSFERIU UM VALOR PARA O DEDÉ
# c2.extrado() # --> DEDÉ VERIFICOU O EXTRATO E O SEU PIX
# c1.extrado() # --> GABO VERIFICOU O EXTRATO APÓS A TRANSFERENCIA


#EX15 - Crie uma classe chamada Produto que representa um produto em um sistema de vendas. A classe deve ter os seguintes atributos e métodos: Atributos: nome (string): nome do produto. preco (float): preço do produto. quantidade (int): quantidade disponível do produto. Métodos: alterar_preco(preco): Permite alterar o preço do produto, mas somente se o novo preço for maior que zero. vender(quantidade): Realiza a venda de uma quantidade do produto. Caso a quantidade seja maior que a disponível, o sistema deve informar que não há estoque suficiente. exibir_informacoes(): Exibe as informações do produto (nome, preço e quantidade).

class Produto():
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.__preco = preco
        self.__quantidade = quantidade
        self.__lucro = 0

    def alterar_preco(self, valor):
        if valor > 0:
            self.__preco = valor
        else:
            print(f'Valor Negativo')
        
    def vender(self, qtd):
        self.__quantidade -= qtd
    
    def lucro_empresa(self):
        self.__lucro = self.__quantidade * self.__preco

    def exibir_produto(self):
        self.lucro_empresa()
        print(f'Lucro: {self.__lucro}')

# p1 = Produto('Leite', 2, 90)
# p1.alterar_preco(4)
# p1.vender(20)
# p1.exibir_produto()

#EX16 - Crie uma classe Estoque que gerencia um estoque de produtos. A classe deve conter os seguintes atributos e métodos:
#nome_produto (string): nome do produto. preco (float): preço unitário do produto. quantidade_em_estoque (int): quantidade disponível do produto no estoque. quantidade_vendida (int): quantidade total já vendida.
#atualizar_estoque(quantidade): Atualiza a quantidade disponível no estoque. vender_produto(quantidade): Vende uma quantidade do produto. O estoque não pode ser negativo, então se a quantidade for maior que a disponível, imprima uma mensagem de erro. calcular_faturamento(): Calcula o faturamento gerado pelas vendas, multiplicando o preço pelo total de unidades vendidas. exibir_resumo(): Exibe o nome do produto, quantidade em estoque, quantidade vendida e o faturamento.

class Estoque():
    def __init__(self ,nome, preco, qtd):
        self.nome = nome
        self.__preco = preco
        self.__qtd = qtd
        self.__vendas = 0
        self.__lucro = 0
    

    def atualizar_estoque(self, valor):
        self.__qtd = valor
    
    
    def vender(self, valor):
        self.__qtd -= valor
        self.__vendas = valor
    
    def faturamento(self):
        self.__lucro = self.__vendas * self.__preco

    def exibir(self):
        self.faturamento()
        print(f'Faturamento: R${self.__lucro:.2f}')
    

# e1 = Estoque('Leite', 3, 30)
# e1.atualizar_estoque(40)
# e1.vender(12)
# e1.exibir()

#EX17 - Crie uma classe Dado que sorteia um número de 1 a 6. Crie outra classe Jogo que permite jogar o dado 5 vezes e mostrar a soma total.
from random import randint
class Dado():
    def __init__(self):
        pass
    
    def rolar(self):
        return randint(1, 6)
    
class Jogo():
    def __init__(self):
        self.dado = Dado()
        self.soma = []
    
    def jogar(self):
        for x in range(5):
            valor = self.dado.rolar()
            self.soma.append(valor)
            print(f'Caiu {valor}')

    def exibir(self):
        self.jogar()
        print(sum(self.soma))

# j1 = Jogo()
# j1.exibir()

#EX18 - Crie uma classe Votacao com um dicionário interno para contar votos em opções. Métodos: votar(opcao) resultado()
import random
class Voto():
    def __init__(self):
        self.lista = ['A', 'B']
    
    def vot(self):
        return random.choice(self.lista)

class Urna():
    def __init__(self):
        self.voto = Voto()
        self.resultado = {'A':0, 'B':0}

    def votacao(self):
        for x in range(5):
            valor = self.voto.vot()
            self.resultado[valor] = self.resultado[valor] + 1
        
    def resultado_final(self):
        self.votacao()
        print(self.resultado)

# u1 = Urna()
# u1.resultado_final()

#EX19 - Classe Sensor de Umidade Crie a classe Sensor com uma lista de valores lidos. Adicione métodos para: Adicionar nova leitura. Mostrar média de umidade. Mostrar maior e menor valor registrado.

class SensorUmidade():
    def __init__(self):
        self.lista = []
    
    def add_item(self, valor):
        for x in range(5):
            valor = valor * randint(1, 7)
            self.lista.append(valor)
    def media(self):
        media = sum(self.lista) / len(self.lista)
        return media
    def show(self, valor):
        self.add_item(valor)
        m = self.media()
        print(self.lista)
        print(m)

# s1 = SensorUmidade()
# s1.show(randint(1, 6))

#EX20 - Crie a classe Musica com titulo, artista, duracao.Crie a classe Playlist que pode: Adicionar músicas. Mostrar todas as músicas. Calcular tempo total da playlist. com GET E SET
class Musica():
    def __init__(self, titulo, artista, duracao):
        self.__titulo = titulo
        self.__artista = artista
        self.duracao = duracao

    """GET E SET"""
    @property # --> GET
    def titulo(self):
        return self.__titulo

    @titulo.setter # --> SET
    def titulo(self, titulo):
        self.__titulo = titulo
    
    """GET E SET"""
    @property # --> GET
    def artista(self):
        return self.__artista

    @artista.setter # --> SET
    def artista(self, artista):
        self.__artista = artista

class Play():
    def __init__(self):
        self.lista = {}
    
    def add_music(self, valor):
        self.lista.update({valor.titulo:[valor.artista, valor.duracao]})
        print(self.lista)
        
# m1 = Musica('Rap Caiox', 'CaioxMC', 4)
# p1 = Play()
# p1.add_music(m1)

#EX21 - #EX13 - Classe Agenda de Contatos Crie uma classe Contato com nome, telefone, email. Crie uma classe Agenda que guarda vários contatos em uma lista e permite: adicionar contato remover contato pelo nome buscar contato pelo nome listar todos os contatos.
class Contato():
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.__telefone = telefone
        self.__email = email
    
    """GET E SETS"""
    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email

class Agenda():
    def __init__(self):
        self.agenda = {}
    
    def add_cont(self, valor):
        self.agenda.update({valor.nome:[valor.telefone, valor.email]})
    
    def show_list(self):
        for x,z in self.agenda.items():
            print(f'Contato: {x}: Telefone - {z[0]} E-mail - {z[1]}')


# c1 = Contato('Livro1', '12-99134124', 'lili@yahoo.com')
# agenda = Agenda()
# agenda.add_cont(c1)
# agenda.show_list()


#EX22 - Crie uma classe ContaBancaria com os atributos privados: titular, saldo.
class Conta():
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo
    
    """GET E SET"""
    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.__saldo
    
    def sacar(self, valor):
        self.__saldo -= valor
    
    def depositar(self, valor):
        self.__saldo += valor
        
    def show(self):
        print(self.__saldo)
        print(self.__titular)
    
# c1 = Conta('Mundial', 900)
# c1.depositar(300)
# c1.show()

#EX23 - ANALISE DE VENDAS COM GET E SET
class Analise():
    def __init__(self, vendas):
        self.__vendas = vendas
        self.__totalProds = {}
        self.__totalPreco = {}
    
    
    """GET E SET"""
    @property
    def vendas(self):
        return self.__vendas
    
    @vendas.setter
    def vendas(self, vendas):
        self.__vendas = vendas
    
    """GET E SET"""    
    @property
    def prods(self):
        return self.__totalProds
    
    @prods.setter
    def prods(self, totalProds):
        self.__totalProds = totalProds
    
    """GET E SET"""
    @property
    def totalPreco(self):
        return self.__totalPreco    
    
    @totalPreco.setter
    def totalPreco(self, totalPreco):
        self.__totalPreco = totalPreco
        
    #QUANTIDADE DE VENDAS PRODUTo
    def qtd_vendas(self):
        for x in self.vendas:
            produto = x['produto']
            if produto not in self.prods:
                self.prods.update({produto:x['quantidade']})
            else:
                valor_inicial = x['quantidade']
                valor_final = valor_inicial + self.prods[produto]
                self.prods.update({produto:valor_final})
        print(self.prods)
    
    def total_preco(self):
        total_preco = {}
        for x in self.vendas:
            produto = x['produto']
            if produto not in total_preco:
                total_preco.update({produto:x['preco_unitario']})
            else:
                valor_inicial = total_preco[produto]
                valor_final = x['preco_unitario'] + valor_inicial
                total_preco.update({produto:valor_final})
        
        for x,z in self.prods.items():
            print(x, z)
            if x in total_preco:
                self.totalPreco.update({x:total_preco[x] * z})

            
        # print(self.totalPreco)
        
    def melhor_prod(self):
        m = max(self.totalPreco)
        print(f'Produto com maior faturamento: {m}')

# venda = Analise(vendas)
# venda.qtd_vendas()
# venda.total_preco()
# venda.melhor_prod()

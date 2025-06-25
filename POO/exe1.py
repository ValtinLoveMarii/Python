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

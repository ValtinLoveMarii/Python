#EX1 - Crie um dicionário que associe números de 1 a 10 com seus respectivos quadrados (ex: {1: 1, 2: 4, ..., 10: 100})
dic = {}
for i in range(2):
    n = int(input('Digite um número: '))
    dic.update({n:n**2})
print(dic)

#EX2 - Crie um sistema de cadastro de alunos com nome, idade e uma lista de matérias cursadas. Permita inserir, buscar e remover alunos.
alunos = {
    "nome":'',
    "idade":'',
    "curso":[]
}
for i in alunos:
    nome_aluno = str(input('Digite o nome do aluno: '))
    idade = int(input('Digite a idade do aluno: '))
    alunos.update({'nome':nome_aluno})
    alunos.update({'idade':idade})
    break
a = 0
for x in alunos.keys():
    if x == 'curso':
        lista =alunos[x]
        while a < 3:
            materia_matriculada = str(input('Digite a matéria matriculada: '))
            lista.append(materia_matriculada)
            a = a+1
        break
    else:
        pass
print(alunos)

#EX3 - Dada uma string, conte quantas vezes cada palavra aparece.
frase = "eu amo minha namorada muito amo ela é demais eu amo muito a minha namorada"
frase.lower()
palavras = frase.split()
dic = {}
for i in palavras:
    a = palavras.count(i)
    dic.update({i:a})
print(dic)

#EX4 - Conte quantas vezes cada letra aparece em uma string (ignore espaços).
frase = 'leon é legal que cara massa muito epico foi mordido mas ta bem igual ao bakugou'
frase.lower()
frase = frase.replace(" ","")
dic = {}
for i in frase:
    z = frase.count(i)
    dic.update({i:z})
print(dic)

#EX5 - Dado um dicionário, crie um novo apenas com os itens cujo valor seja maior que 10.
d = {'a': 5, 'b': 12, 'c': 7, 'd': 20}
d_temp = {}
for z in d:
    if d[z] > 10:
        d_temp.update({z:d[z]})
    else:
        continue
print(d_temp)

#EX6 - Com duas listas, uma de chaves e outra de valores, crie um dicionário.
chaves = ['nome', 'idade', 'cidade']
valores = ['João', 25, 'São Paulo']
dic = {}
cont = 0
for i in chaves:
    dic.update({i:valores[cont]})
    cont = cont + 1
print(dic)

#EX7 - A partir de uma lista de tuplas, agrupe os valores por chave.
dados = [('a', 1), ('b', 2), ('a', 3), ('b', 4), ('c', 5)]
dic = {}
c = 0

for i in dados:
    dados[c] = list(i)
    c += 1
for x in dados:
    dic.update({x[0]:[]})
c_2 = 0 
for z in dados:
    dados2 = dados[c_2]
    if dados2[0] in dic:
        x = dic[dados2[0]]
        x.append(dados2[1])
    else:   
        continue
    c_2 += 1
print(dic)

#EX8 - Dado um dicionário com nomes e idades, e uma lista com pessoas que fizeram aniversário, incremente a idade dessas pessoas em 1.
pessoas = {'Ana': 30, 'João': 25, 'Carlos': 40}
aniversariantes = ['Ana', 'Carlos']
for i in aniversariantes:
    if i in pessoas:
        pessoas[i] = pessoas[i] + 1
    else:
        continue
print(pessoas)

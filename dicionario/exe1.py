#EXERCÍCIOS DE DICIONÁRIO

#EX1 - Verificar se um tem um int no dicionário e remove-ló
# dic = {
#     "TIPO":"NOTE",
#     "MARCA":"DELL",
#     "ANO":2024
# }

# for i in dic:
#     # print(dic[i])
#     if dic[i] == 2024:
#         dic[i] = 2090
#     else:
#         print('Não tem')
#         continue
# print(dic)


#EX2 - Crie um dicionário com as informações de uma pessoa: nome, idade e cidade. Depois, imprima cada valor separadamente.
# pessoa = {
#     "nome":"Naruto",
#     "idade":17,
#     "cidade":"Konoha"
# }
# for x in pessoa:
#     print(f' {x} = {pessoa[x]}')


#EX3 - Adicione uma nova chave ao dicionário acima: "profissao" com algum valor de sua escolha.
# profissao = {
#     "nome":"Analista de dados",
# }
# salario = float(input('Digite o salário: '))
# profissao.update({"salario":salario})
# print(profissao)

#EX4 - Modifique o valor da chave "cidade" no dicionário para outra cidade qualquer.
# dic = {
#     "cidade":"konoha"
# }
# city = str(input('Digite uma cidade: '))
# dic.update({"cidade":city})
# print(dic)

#EX5 - Remova a chave "idade" do dicionário.
# dic = {}
# for i in range(1, 3):
#     chave = str(input('Oq deseja adicionar: '))
#     valor = str(input('Adicione: '))
#     dic.update({chave : valor})
# print(dic)

#EX6 - Crie um dicionário com nomes de alunos e suas notas. Depois, calcule e imprima a média das notas.
# import os
# aluno = {}
# media_aluno = {}
# c = 0
# for i in range(2):
#     nome = str(input('Digite o nome do aluno: '))
#     aluno.update({nome: []})

# for x in aluno.values():
#     for l in range(2):
#         os.system('cls')
#         n = float(input(f'Digite a nota do aluno: '))
#         x.append(n)
#     nota_final = sum(x) / len(x)
#     media_aluno.update({f"media-{c}":nota_final})
#     c = c + 1
# print(aluno)
# print(media_aluno)


#EX7 - Dado um dicionário com pares de chave-valor, crie uma função que inverta as chaves e valores.
# dici = {'a': 1, 'b': 2, 'c': 3}
# dici2 = {}
# l = []
# l2 = []
# for i in dici:
#     # print(i)
#     a = i
#     b = dici[i]
#     l.append(a)
#     l2.append(b)
# for x in l2:
#     # print(x)
#     dici2.update({x:None})
# k = 1
# for m in dici.keys():
#     print(m)
#     print(k)
#     dici2.update({k:m})
#     k = k + 1
# print(dici2)

#EX8 - Escreva uma função que recebe uma lista de palavras e retorna um dicionário com a contagem de cada palavra na lista.
# dic = {}
# lista =[]
# for i in range(7):
#     n = str(input('Digite algo: '))
#     lista.append(n)
# for m in lista:
#     dic.update({m:None})
# # print(dic)
# for z in dic:
#     cont = lista.count(z)
#     print(cont)
#     dic.update({z:cont})
# print(dic)

#EX9 - Escreva uma função que mescla dois dicionários, onde as chaves iguais devem somar os valores.
# dic = {}
# c = 0
# for i in range(2):
#     s = str(input('Digite a chave: '))
#     n = int(input('Digite um valor: '))
#     print("-"*30)
#     dic.update({s:n})
# dic2 = {'a':230, 'b':293, 'c':122}
# cont = dic2.keys()
# cont = list(cont)
# for m in dic.keys():
#     if (m == cont[c]):
#         dic.update({m:dic[m] + dic2[m]})
#         c = c + 1
#         print('Entrou')
#     else:
#         print('Nao entrou')
# print(dic)

#EX10 - CRIAR CONTAGEM DE DICIONARIO
# categorias = {
#     "fruta" : ["maça", "banana"],
#     "legume" : ["alface"]
# }
# dic = {}
# for i in categorias:
#     a = len(categorias[i])
#     dic.update({i:a})
# print(dic)

#EX11 - Dada uma lista de nomes, crie um dicionário em que o nome é a chave e o valor é o índice dele na lista.
# lista = ["Ana", "Bruno", "Carlos", "Diana", "Saiko", "Zumbi"]
# dic = {}
# c = 0
# for x in lista:
#     dic.update({x:c})
#     c = c + 1
# print(dic)

#EX12 - Dado um dicionário de produtos e preços, e um nome de produto digitado pelo usuário, verifique se o produto existe no dicionário.
# produtos = {
#     "arroz":10,
#     "carne":20,
#     "pao":0.50,
#     "leite":2
# }
# while True:
#     per = str(input('Digite o produto: '))
#     if per in produtos:
#         print(f'O preço do {per} é {produtos[per]}')
#         break
#     else:
#         print('Produto não encontrado!')
#         continue

#EX13 - Aumente em 10% o valor de todos os produtos.
# precos = {"arroz": 10, "feijão": 8, "leite": 5}
# for i in precos:
#     a = precos[i]
#     per = (10/100) * a
#     conta = a + per
#     precos[i] = conta
# print(precos)

#EX14 - Dada uma lista de tuplas com (nome, idade), agrupe os nomes por idade em um dicionário.
# dados = [("Ana", 25), ("Bruno", 30), ("Carlos", 25), ("Diana", 30)]
# dic = {}
# for nome, idade in dados:
#     if idade in dic:
#         dic[idade].append(nome)
#     else:
#         dic[idade] = [nome]
# print(dic)





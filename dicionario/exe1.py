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


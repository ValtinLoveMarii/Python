#EX1 - Crie um dicionário que associe números de 1 a 10 com seus respectivos quadrados (ex: {1: 1, 2: 4, ..., 10: 100})
# dic = {}
# for i in range(2):
#     n = int(input('Digite um número: '))
#     dic.update({n:n**2})
# print(dic)

#EX2 - Crie um sistema de cadastro de alunos com nome, idade e uma lista de matérias cursadas. Permita inserir, buscar e remover alunos.
# alunos = {
#     "nome":'',
#     "idade":'',
#     "curso":[]
# }
# for i in alunos:
#     nome_aluno = str(input('Digite o nome do aluno: '))
#     idade = int(input('Digite a idade do aluno: '))
#     alunos.update({'nome':nome_aluno})
#     alunos.update({'idade':idade})
#     break
# a = 0
# for x in alunos.keys():
#     if x == 'curso':
#         lista =alunos[x]
#         while a < 3:
#             materia_matriculada = str(input('Digite a matéria matriculada: '))
#             lista.append(materia_matriculada)
#             a = a+1
#         break
#     else:
#         pass
# print(alunos)

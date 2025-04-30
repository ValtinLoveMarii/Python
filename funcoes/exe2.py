#EX1 - Crie uma função com nomes de alunos e suas notas. Depois, calcule e imprima a média das notas.
def function(**kwags):
    return kwags
alunos = {}
while True:
    nome = str(input('Nome: '))
    nota = float(input('Nota: '))    
    aluno = function(**{nome:nota})
    
    alunos.update(aluno)
    
    cont = str(input('CONTINAR? '))
    if cont == 's':
        continue
    else:
        break
    
print(alunos)

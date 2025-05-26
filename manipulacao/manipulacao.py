#AULA 32 - MANIPULAÇÃO de ARQUIVOS
import os
# print(os.name)

print(os.path.exists('meuspacs.txt'))
print(os.path.exists('if/if_else_elif.py'))
# os.mkdir('pasta')
# os.makedirs('manipulacao', exist_ok=True)
# with open('manipulacao/arquuivo.py', 'w', encoding='utf-8') as f:
#     f.write('Esse é o novo arquivo legal')
# os.remove('manipulacao/arquuivo.py')
# os.removedirs('pasta')

# os.rename('./manipulacao/arquuivo.py', './manipulacao/arquivinho.py')

dic ={}
with open('dados.txt','r') as f:
    arquivo = f.readlines()
for x in arquivo:
    cols = x.strip().split()
    dic.update({cols[0]:cols[1]})
print(dic)

# with open('dados.txt', 'a') as f:
#     f.write('\nRAIT DE RUMBA VAI DE RAIT DE RUMBA')

while True:
    aaa = str(input('Criar arquivo: '))
    with open(f'{aaa}.txt', 'w') as f:
        f.write('Criado com Sucesso')
    resp = str(input('Continuar? '))
    if resp == 's':
        continue
    else:
        break

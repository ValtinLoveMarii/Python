##EXERCÍCIOS DE MANIPULACAO DE ARQUIVOS

#EX1 - Criar e escrever em um arquivo
with open('texto.txt', 'w', encoding='utf-8') as f:
    f.write('Naruto Uzumaki legal')

#EX2 - Ler o conteúdo de um arquivo Leia e imprima o conteúdo do arquivo exemplo.txt.
ler = open('texto.txt', 'r')
# print(ler.read())

#EX3 - Adicionar conteúdo em um arquivo existente
with open('texto.txt','a') as f:
    # f.write('\nSasuke tbm bem legal')

#EX4 - Contar linhas de um arquivo
with open('texto.txt', 'r') as  f:
    linhas = f.readlines()
# print(len(linhas))

#EX5 - Copiar conteúdo de um arquivo para outro Copie o conteúdo de exemplo.txt para um novo arquivo chamado copia.txt
with open('texto.txt', 'r') as f:
    t1 = f.read()
# with open('t.txt', 'w') as f:
#     f.write(t1)

#EX6 - Listar arquivos de um diretório Use a biblioteca os para listar todos os arquivos do diretório atual
from os import listdir
# print(listdir())

#EX7 - Verificar se um arquivo existe Peça o nome de um arquivo ao usuário e verifique se ele existe no diretório.
import os
diretorio = str(input('Digite o diretório: '))
arqui = str(input('Digite o arquivo: '))
# print(os.path.exists('if/exe1.py'))
reso = os.path.exists(f'{diretorio}/{arqui}')
if reso == True:
    print('Sim o diretório e o arquivo existem!')
else:
    print('Não existem!')

#EX8 - Contar palavras em um arquivo Conte quantas palavras existem no arquivo exemplo.txt.\
with open('texto.txt','r') as f:
    palavras = f.readline()
z = palavras.split()
# print(len(z))

#EX9 - Renomear um arquivo usando os Renomeie o arquivo copia.txt para backup.txt.
from os import rename
# rename('texto.txt', 'backup.txt')

#EX10 - Criar e remover diretórios
import os
os.mkdir('pasta')
os.removedirs('pasta')

#EX11 - Organizar arquivos por extensão que Escreva um script que percorra uma pasta e mova os arquivos para subpastas de acordo com sua extensão (.txt, .jpg, .py etc).
python = os.path.exists('pasta/x.py')
javaS = os.path.exists('pasta/m.js')
httt = os.path.exists('pasta/g.html')
if python == True:
    os.mkdir('pasta/python_arquivos')
    os.rename('pasta/x.py', 'pasta/python_arquivos/x.py')
else:
    with open('pasta/x.py', 'w', encoding='utf-8') as f:
        f.write('Esse é o novo arquivo legal')
if javaS == True:
    os.mkdir('pasta/js_arquivos')
    os.rename('pasta/m.js', 'pasta/js_arquivos/m.js')
if httt == True:
    os.mkdir('pasta/ht_arquivos')
    os.rename('pasta/g.html', 'pasta/ht_arquivos/g.html')
#EX12 - Crie um arquivo chamado dados.txt com algumas linhas de texto Use with open para ler e imprimir todo o conteúdo do arquivo
with open('dados.txt', 'r') as f:
        conteudo = f.read()
        print(conteudo)

#EX13 - Peça ao usuário para digitar 3 frases Grave essas frases em um arquivo chamado frases.txt, uma por linha
for x in range(3):
    palavra = str(input('Palavra: '))
    with open('dados.txt', 'a') as f:
        f.write(f'\n{palavra}')
with open('dados.txt', 'r') as f:
    print(f.read())

#EX14 - Crie um programa que conte quantas linhas existem em um arquivo texto
with open('dados.txt', 'r') as f:
   conteudo = f.readlines()
  print(len(conteudo))

#EX15 - Leia um arquivo e grave em outro apenas as linhas que contêm uma palavra específica
with open('dados.txt', 'r') as f:
    print(f.readlines())
    lista = f.readlines()
for i in lista:
    i = i.replace('\n', '')
    if i == 'Narutinho':
        with open('dados2.txt', 'w') as f:
            f.write(i)
    else:
        print('Anaru')

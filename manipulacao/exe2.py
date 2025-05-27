##EXERCÍCIOS DE MANIPULACAO DE ARQUIVOS
import os
#EX1 - Use os.path para verificar se um arquivo ou pasta existe
import os
arq = str(input('Digite o arquivo ou pasta ai: '))
if os.path.exists(arq) == True:
    print(('Existe'))
else:
    print('Não existe!')

# #EX2 - Peça ao usuário um caminho de arquivo e: Extraia apenas o nome do arquivo (sem a extensão) Extraia apenas a extensão Extraia apenas o diretório pai
# import os

caminho = str(input('caminho: '))
nome_arquivo = os.path.basename(caminho)
nome_s_extensao = os.path.splitext(nome_arquivo)[0]
extensao = os.path.splitext(nome_arquivo)[1]
diretorio = os.path.dirname(caminho)
print(f'Diretório: {diretorio}')
print(f'Nome do arquivo sem extensão: {nome_s_extensao}')
print(f'Tipo de arquivo: {extensao}')


#EX3 - Crie um script que copie todos os arquivos .txt de uma pasta para outra chamada backup_txt
# import os
while True:
    arquivo = str(input('Criar arquivo: '))
    with open(f'zeeee/{arquivo}.txt', 'w') as f:
        f.write('Criado com Sucesso!')
    resp = input('Criar novamente? ')
    if resp == 's':
        continue
    else:
        break

arquivos = os.listdir()
for x in arquivos:
    if os.path.exists('bkcup.txt') == True:
        if x.endswith('.txt'):
            if x != 'bkcup.txt':
                with open(x,'r') as f:
                    conteudo = f.read()
                with open('bkcup.txt', 'a') as a:
                    a.write(f'{conteudo}\n')
            else:
                print(f'Esse é o {x}')
                continue
    else:
        with open('bkcup.txt', 'w') as w:
            w.write('')
        continue

#EX4 - Apague arquivos de uma pasta que não foram modificados nos últimos 40 segundos.
# import os
from datetime import datetime
arquivos = os.listdir()
for x in arquivos:
    if x.endswith('.txt'):
        data_inicial = os.path.getmtime(x)
        data_formatada = datetime.fromtimestamp(data_inicial)
        segundos = data_formatada.second
        print(data_formatada, segundos)
        if segundos >= 40:
            os.remove(x)
            print(f'REMOVI O {x}')
        else:
            print('LEGALLL!')
            print(segundos)
            continue

#EX5 - Buscar palavra em múltiplos arquivos Dado um diretório, procure por todos os arquivos .txt e exiba aqueles que contêm a palavra "python".
while True:
    arquivo = str(input('Criar arquivo: '))
    with open(f'{arquivo}.txt', 'w') as f:
        f.write('Criado com Sucesso!')
    resp = input('Criar novamente? ')
    if resp == 's':
        continue
    else:
        break

arquivos = os.listdir()
for x in arquivos:
    if x.endswith('.txt'):
        with open(x, 'r') as r:
            palavras = r.read()
            pal_certo = palavras.find('python')
            if pal_certo != -1:
                print(f'O arquivo {x} tem a palavra python!')
            else:
                print(f'Esse arquivo {x} não possuí a palavra python')

#EX6 - Crie um script que gere um arquivo log.txt com a estrutura de diretórios e arquivos a partir de uma pasta raiz.
for dirpath, dirnames, filenames in os.walk('modulos'):
    with open('log.txt', 'a') as a:
        a.write(f'{dirpath}\n {dirnames}\n {filenames} \n')
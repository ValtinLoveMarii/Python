# # ##EXERCÍCIOS DE MANIPULACAO DE ARQUIVOS
import os
from datetime import date
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

# #EX5 - Buscar palavra em múltiplos arquivos Dado um diretório, procure por todos os arquivos .txt e exiba aqueles que contêm a palavra "python".
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

# #EX6 - Crie um script que gere um arquivo log.txt com a estrutura de diretórios e arquivos a partir de uma pasta raiz.
for dirpath, dirnames, filenames in os.walk('modulos'):
    with open('log.txt', 'a') as a:
        a.write(f'{dirpath}\n {dirnames}\n {filenames} \n')

#EX7 - Crie um script que conte quantas vezes a palavra "Python" aparece em todos os .txt de uma pasta.
arquivos = os.listdir()
contador = 0
for x in arquivos:
    if x.endswith('.txt'):
        with open(x, 'r') as r:
            dados = r.read()
        if 'python' in dados:
            contador = dados.count('python') + contador
        else:
            continue
    else:
        continue

print(f'A palavra PYTHON aparece {contador} vezes')

#EX8 - Crie um script que encontre os 3 arquivos .txt mais pesados em uma pasta e mostre o nome e o tamanho.
arquivos = os.listdir()
maiores = {}
numeros = []
for x in arquivos:
    if x.endswith('.txt'):
        tamanho = os.path.getsize(x)
        maiores.update({x:tamanho})
for name, number in maiores.items():
    numeros.append(number)
mariores = numeros.sort(reverse=True)
novos_maiores = []
novos_maiores.extend(numeros[0:4])
print(novos_maiores)
dic = {}
for i in novos_maiores:
    for n, v in maiores.items():
        if i == v:
            dic.update({n:v})
        else:
            print('Não está certo!')
print(dic)

#EX9 - Escreva um programa que renomeie todos os arquivos .jpg de uma pasta para o formato foto_001.jpg, foto_002.jpg(vou usar txt por praticidade)
arquivos = os.listdir()
c = 1
lista_fotos = []
for x in arquivos:
    if x.endswith('.txt'):
        os.rename(x, f'foto00{c}.txt')
        c = c + 1

#EX10 - Faça um backup completo de uma pasta, incluindo subpastas e arquivos, para uma nova pasta com a data atual no nome.
dia_atual = date.today()
os.mkdir(f'bkcup-dia-{dia_atual}')
arquivos = os.listdir('modulos')
lista_arquivos = []
for x in arquivos:
    if x.endswith('.py'):
        print('ARQUIVO')
        lista_arquivos.append(x)
    else:
        os.mkdir(f'bkcup-dia-2025-05-27/{x}')
for i in lista_arquivos:
     os.rename(f'modulos/{i}', f'bkcup-dia-2025-05-27/{i}')


lista_arquivos = []
new_arquivos = os.listdir('bkcup-dia-2025-05-27')
for i in new_arquivos:
    if i.endswith('.py'):
        pass
    else:
        sub_pasta_pacote_modulo = i
print(sub_pasta_pacote_modulo)
sub_pasta = os.listdir(f'modulos/{sub_pasta_pacote_modulo}')
for p in sub_pasta:
    if p.endswith('.py'):
        os.rename(f'modulos/{sub_pasta_pacote_modulo}/{p}', f'bkcup-dia-2025-05-27/{sub_pasta_pacote_modulo}/{p}')
    else:
        os.mkdir(f'bkcup-dia-2025-05-27/{sub_pasta_pacote_modulo}/{p}')
        ultima_pasta = os.listdir(f'modulos/{sub_pasta_pacote_modulo}/{p}')
        os.rename(f'modulos/{sub_pasta_pacote_modulo}/{p}/{ultima_pasta[0]}', f'bkcup-dia-2025-05-27/{sub_pasta_pacote_modulo}/{p}/{ultima_pasta[0]}')


#EX12 - Criar um módulo em python capaz de registrar dados de pacientes

data_atual = date.today()
ano_atual = data_atual.year

def paciente(ano_atual):
    print('-------------------------------------')
    nome  = input('Digite seu nome completo: ')
    email = input('Digite seu email: ')
    data_nascimento = str(input('Ano em que nasceu: '))
    print('-------------------------------------')
    os.system('cls')
    data_nascimento = int(data_nascimento)
    idade = ano_atual - data_nascimento
    if idade >= 65:
        if os.path.exists('pacientes.txt') == True:
            with open('pacientes.txt','a') as a:
                a.write(f'Paciente: {nome} - E-mail: {email} - Idade: {idade} - GRUPO DE RISCO: SIM\n')
        else:
            with open('pacientes.txt', 'w', encoding='UTF-8') as w:
                w.write(f'Paciente: {nome} - E-mail: {email} - Idad: {idade} - GRUPO DE RISCO: SIM\n')
    else:
        if os.path.exists('pacientes.txt') == True:
            with open('pacientes.txt','a') as a:
                a.write(f'Paciente: {nome} - E-mail: {email} - Idade: {idade} - GRUPO DE RISCO: NAO\n')
        else:
            with open('pacientes.txt', 'w', encoding='UTF-8') as w:
                w.write(f'Paciente: {nome} - E-mail: {email} - Idade: {idade} - GRUPO DE RISCO: NAO\n')
if __name__ == '__main__':
    print('Código RODANDO DIRETO')
    print('FASE TESTE!')
    while True:
        paciente(ano_atual=ano_atual)
        print('CLÍNICA HOSPITALAR RAPHAEL AFONSO NUNES')
        print('Dados coletados com sucesso!')
        with open('pacientes.txt', 'r') as r:
            print(r.read())
        input('Pressione em enter para continuar...')
        os.system('cls')
        continuar = input('Deseja cadastrar um novo paciente? (s/n)').lower()
        try:
            if continuar == 's':
                continue
            elif continuar == 'n':
                os.system('cls')
                print('FIM DO SISTEMA')
                input('PRESSIONE ENTER PARA SAIR...')
                break
        except ValueError:
            print('POR FAVOR DIGITE S OU N')
            input('PRESSIONE ENTER PARA VOLTAR A SUA ESCOLHA...')
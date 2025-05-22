##EXERCÍCIOS DE MANIPULACAO DE ARQUIVOS
#EX1 - Use os.path para verificar se um arquivo ou pasta existe
import os
arq = str(input('Digite o arquivo ou pasta ai: '))
if os.path.exists(arq) == True:
    print(('Existe'))
else:
    rint('Não existe!')

#EX2 - Peça ao usuário um caminho de arquivo e: Extraia apenas o nome do arquivo (sem a extensão) Extraia apenas a extensão Extraia apenas o diretório pai
import os

caminho = str(input('caminho: '))
nome_arquivo = os.path.basename(caminho)
nome_s_extensao = os.path.splitext(nome_arquivo)[0]
extensao = os.path.splitext(nome_arquivo)[1]
diretorio = os.path.dirname(caminho)
print(f'Diretório: {diretorio}')
print(f'Nome do arquivo sem extensão: {nome_s_extensao}')
print(f'Tipo de arquivo: {extensao}')

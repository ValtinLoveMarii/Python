# import os

# produtos_dicionario = {}


# def limpar_tela():
#     os.system('cls' if os.name == 'nt' else 'clear')


# def cabecalho(msg):
#     print("\n" + "=" * 40)
#     print(f"{msg.center(40)}")
#     print("=" * 40)


# def adicionar_produtos(produtos_dicionario):
#     limpar_tela()
#     cabecalho("Adicionar Produto")
#     nome_prod = str(input('Digite o nome do produto: ')).lower()
#     quantidade = int(input('Digite a quantidade de unidades: '))
#     preco = float(input('Digite o preço da unidade: '))
#     produtos_dicionario[nome_prod] = [quantidade, preco]
#     print("\nProduto adicionado com sucesso!")
#     input("\nPressione Enter para continuar...")


# def remover_produto(produtos_dicionario):
#     limpar_tela()
#     cabecalho("Remover Produto")
#     remove_prod = str(input('Qual produto deseja remover: ')).lower()
#     if remove_prod in produtos_dicionario:
#         produtos_dicionario.pop(remove_prod)
#         print(f"\nProduto '{remove_prod}' removido com sucesso!")
#     else:
#         print('\nEsse produto não existe!')
#     input("\nPressione Enter para continuar...")


# def atualizar_produtos(produtos_dicionario):
#     limpar_tela()
#     cabecalho("Atualizar Produto")
#     resp_atualizar = str(input('Qual produto deseja atualizar: ')).lower()
#     if resp_atualizar not in produtos_dicionario:
#         print('Esse produto não existe!')
#     else:
#         new_quantidade = int(input(f'Qual a nova quantidade do produto {resp_atualizar}: '))
#         new_preco = float(input(f'Qual o novo preço do produto {resp_atualizar}: '))
#         produtos_dicionario[resp_atualizar] = [new_quantidade, new_preco]
#         print(f"\nProduto '{resp_atualizar}' atualizado com sucesso!")
#     input("\nPressione Enter para continuar...")


# def listar_produto(produtos_dicionario):
#     limpar_tela()
#     cabecalho("Lista de Produtos")
#     if not produtos_dicionario:
#         print("\nNenhum produto cadastrado no estoque.")
#     else:
#         for i, z in produtos_dicionario.items():
#             print(f"{i.title()} - Quantidade: {z[0]} - Preço: R${z[1]:.2f}")
#     input("\nPressione Enter para continuar...")


# # SISTEMA FINAL
# while True:
#     limpar_tela()
#     cabecalho("Sistema de Estoque")
#     print("""
#     [1] - Adicionar Produto
#     [2] - Remover Produto
#     [3] - Atualizar Produto
#     [4] - Listar Produtos
#     [5] - Sair
#     """)

#     resp = input('Escolha uma opção: ')
#     if resp == '1':
#         adicionar_produtos(produtos_dicionario)
#     elif resp == '2':
#         remover_produto(produtos_dicionario)
#     elif resp == '3':
#         atualizar_produtos(produtos_dicionario)
#     elif resp == '4':
#         listar_produto(produtos_dicionario)
#     elif resp == '5':
#         limpar_tela()
#         print('FIM DO ESTOQUE'.center(40, "="))
#         break
#     else:
#         limpar_tela()
#         print("Opção inválida! Tente novamente.".center(40, "="))
#         input("\nPressione Enter para continuar...")







#TESTE DE SISTEMA
import os
import questionary
dados_produtos = {}
grupo = {
    'perifericos':['mouse', 'teclado', 'fone', 'mouse pad', 'monitor','suporte'],
    'pc_pecas':['notebook', 'hd', 'sdd', 'ram', 'cooler', 'fonte', 'placa-mãe','computador', 'gabinete']
}
tamanho_linha = 60

#FUNÇÃO DE VERIFICAR SE O DIC E O TXT EXISTE A SINCRONIZAR OS DADOS
def carregar_dados_arquivo():
    dados = {}
    if os.path.exists('dados_estoque.txt'):
        with open('dados_estoque.txt', 'r', encoding='utf-8') as f:
            for linha in f:
                linha = linha.strip()
                if linha:
                    try:
                        partes = linha.split(' - ')
                        nome = partes[0].split(':')[1].strip().lower() 
                        qtd = int(partes[1].split(':')[1].strip())      
                        preco = float(partes[2].split(':')[1].strip()) 
                        grupo = partes[3].split(':')[1].strip()
                        dados[nome] = [qtd, preco, grupo]
                        
                    except Exception as e:
                        print(f"Erro ao processar linha: {linha}\nDetalhes: {e}")
    elif os.path.exists('dados_estoque.txt') == False:
        print('Estoque inexistente. Crie o estoque antes de prosseguir.')
        
    return dados


# dados_produtos = carregar_dados_arquivo() -----> PARA TESTE DE DEBUG

#FUNÇÃO DE ADICINAR PRODUTOS
def adiconar_produtos(dados_produtos, grupo):
    try:
        nome_prod = input('Informe o nome do produto: ').strip().lower()
        if not nome_prod:
            print('O nome do produto não pode estar vazio.')
            input('Pressione Enter para voltar ao menu...')
            return
        if nome_prod in dados_produtos:
            print('Item já existente')
            input('Pressione Enter para voltar ao menu...')
            return
        
        quantidade = int(input('Informe a quantidade disponível em estoque: '))
        preco = float(input('Informe o preço unitário do produto: '))
        if quantidade < 0 or preco < 0:
            print('A quantidade e o preço devem ser valores positivos.')
            input('Pressione Enter para voltar ao menu...')
            return
        else:    
            print(f'Produto "{nome_prod}" adicionado/atualizado com sucesso!')
            #VERIFICA SE O ARQUIV JÁ EXISTE
            if os.path.exists('dados_estoque.txt') == True:
                
                # VERIFICAÇÃO DE GRUPO
                if nome_prod in grupo['perifericos']:
                    with open('dados_estoque.txt', 'a', encoding='UTF-8') as a:
                        a.write(f'Nome produto: {nome_prod} - Quantidade: {quantidade} - Preço: {preco} - Grupo: Periféricos\n')
                        dados_produtos.update({f'{nome_prod}': [quantidade, preco, 'Periféricos']})
                else:
                    with open('dados_estoque.txt', 'a', encoding='UTF-8') as a:
                        a.write(f'Nome produto: {nome_prod} - Quantidade: {quantidade} - Preço: {preco} - Grupo: Computadores\n')
                        dados_produtos.update({f'{nome_prod}': [quantidade, preco,'Computadores']})
            
            else:
                #VERIFICAÇÃO DE GRUPO
                if nome_prod in grupo['perifericos']:
                    with open('dados_estoque.txt', 'w', encoding='UTF-8') as w:
                        w.write(f'Nome produto: {nome_prod} - Quantidade: {quantidade} - Preço: {preco} - Grupo: Periféricos\n')
                        dados_produtos.update({f'{nome_prod}': [quantidade, preco, 'Periféricos']})
                else:
                    with open('dados_estoque.txt', 'w', encoding='UTF-8') as w:
                        w.write(f'Nome produto: {nome_prod} - Quantidade: {quantidade} - Preço: {preco} - Grupo: Computadores\n')
                        dados_produtos.update({f'{nome_prod}': [quantidade, preco,'Computadores']})
                        
                        
    except ValueError as error:
        print(f'Entrada inválida: {error}')
        print('Por favor, insira os dados corretamente e tente novamente.')
        input('Pressione Enter para voltar ao menu...')

# adiconar_produtos(dados_produtos=dados_produtos, grupo=grupo)


# #FUNÇÃO DE REMOVER PRODUTOS
def remover_produtos(dados_produtos):
    try:
        remover = str(input('Informe o nome do produto que deseja remover do estoque: ')).strip().lower()
        
        if not remover:
            print('O nome do produto não pode estar vazio.')
            input('Pressione Enter para voltar ao menu...')
            return
            
        elif len(dados_produtos) == 0:
            print('O estoque está vazio. Por favor, adicione produtos antes de tentar remover.')
            input('Pressione Enter para voltar ao menu...')
            return
        
        elif remover not in dados_produtos:
            print('Produto não encontrado. Verifique o nome informado.')
            input('Pressione Enter para voltar ao menu...')
            return
        
        else:
            dados_produtos.pop(remover)
            with open('dados_estoque.txt', 'r') as r:
                lista = r.readlines()
                for i, valor in enumerate(lista):
                    nome_arquivo = valor.split(' - ')[0].split(':')[1].strip().lower()
                    if nome_arquivo == remover:
                        del lista[i]
                        with open('dados_estoque.txt', 'w', encoding='UTF-8') as w:
                            w.writelines(lista)
                        print(f'Produto "{remover}" removido com sucesso.')
    except ValueError as error:
        print(f'Entrada inválida: {error}')
        print('Por favor, insira os dados corretamente e tente novamente.')
        input('Pressione Enter para voltar ao menu...')
        
# remover_produtos(dados_produtos=dados_produtos)

#FUNÇÃO DE ATUALIZAR PRODUTOS
def atualizar_produtos(dados_produtos, grupo):
    
    try:
        produto_atualizar = str(input('Qual produto deseja atualizar: ')).strip().lower()
        if not produto_atualizar.strip():
            print('O nome do produto não pode estar vazio.')
            input('Pressione Enter para voltar ao menu...')

        elif len(dados_produtos) == 0:
            print('Estoque ainda não possuí produtos, por favor adicione!')
            input('Pressione Enter para voltar ao menu...')

        elif produto_atualizar.lower() not in dados_produtos:
            print('Produto inválido ou inexistente!')
            input('Pressione Enter para voltar ao menu...')

        else:
            nova_quantidade = int(input(f'Digite a nova quantidade disponível do produto {produto_atualizar}: '))
            novo_preco = float(input(f'Digite o novo valor de cada produto: '))
            if produto_atualizar in grupo['perifericos']:
                with open('dados_estoque.txt', 'r', encoding='UTF-8') as r:
                    lista = r.readlines()
                    for i, valor in enumerate(lista):
                        nome_arquivo = valor.split(' - ')[0].split(':')[1].strip().lower()
                        if nome_arquivo == produto_atualizar:
                            lista[i] = f'Nome produto: {produto_atualizar} - Quantidade: {nova_quantidade} - Preço: {novo_preco} - Grupo: Periféricos\n'
                            dados_produtos.update({f'{produto_atualizar}':[nova_quantidade, novo_preco, 'Periféricos']})
                            with open('dados_estoque.txt', 'w', encoding='UTF-8') as w:
                                w.writelines(lista)
                            print(f'Produto "{produto_atualizar}" atualizado com sucesso.')
            else:
                with open('dados_estoque.txt', 'r', encoding='UTF-8') as r:
                    lista = r.readlines()
                    for i, valor in enumerate(lista):
                        nome_arquivo = valor.split(' - ')[0].split(':')[1].strip().lower()
                        if nome_arquivo == produto_atualizar:
                            lista[i] = f'Nome produto: {produto_atualizar} - Quantidade: {nova_quantidade} - Preço: {novo_preco} - Grupo: Computadores\n'
                            dados_produtos.update({f'{produto_atualizar}':[nova_quantidade, novo_preco, 'Computadores']})
                            with open('dados_estoque.txt', 'w', encoding='UTF-8') as w:
                                w.writelines(lista)
                            print(f'Produto "{produto_atualizar}" atualizado com sucesso.')

    except ValueError as error:
        print(f'Entrada inválida: {error}')
        print('Por favor, insira os dados corretamente e tente novamente.')
        input('Pressione Enter para voltar ao menu...')
        
# atualizar_produtos(dados_produtos=dados_produtos, grupo=grupo)

#FUNÇÃO DE MOSTRAR NA TELA
def mostrar_tela(tamanho_linha):
    with open('dados_estoque.txt', 'r', encoding='UTF-8') as r:
        print('=' * tamanho_linha)
        print('PRODUTOS CADASTRADOS NO ESTOQUE'.center(tamanho_linha))
        print('=' * tamanho_linha)
        print(r.read())

while True:
    os.system('cls')
    print('=' * tamanho_linha)
    print('SISTEMA DE ESTOQUE DE ITENS'.center(tamanho_linha))
    print('=' * tamanho_linha)
    #VERIFICAR O ARQUIVOS TXT(BASE DE DADOS) E O DIC E SINCRONIZA-LÓ
    dados_produtos = carregar_dados_arquivo()
    # print(dados_produtos)
    try:
        escolha_user = questionary.select(
            'Selecione uma opção:',
            choices=[
                "Adicionar Produto",
                "Remover Produto",
                "Atualizar Produto",
                "Mostrar Produtos",
                "Sair"
            ]
        ).ask()
        #ADICIONAR PRODUTO
        if escolha_user == 'Adicionar Produto':
            os.system('cls')
            adiconar_produtos(dados_produtos=dados_produtos,grupo=grupo)

        #REMOVER PRODUTO
        elif escolha_user == 'Remover Produto':
            os.system('cls')
            remover_produtos(dados_produtos=dados_produtos)

        #ATUALIZAR PRODUTO
        elif escolha_user ==  'Atualizar Produto':
            os.system('cls')
            atualizar_produtos(dados_produtos=dados_produtos,grupo=grupo)
        
        #MOSTRAR PRODUTOS NA TELA
        elif escolha_user == 'Mostrar Produtos':
            os.system('cls')
            mostrar_tela(tamanho_linha=tamanho_linha)
            input('Pressione Enter para voltar ao menu...')

        #SAIR
        elif escolha_user == 'Sair':
            os.system('cls')
            print('SAINDO....')
            break


    except ValueError as error:
        os.system('cls') 
        print('Valor Inválido Tente Novamente!')

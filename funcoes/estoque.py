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
            for i,linha in enumerate(f):
                linha = linha.strip()
                if linha:
                    try:
                        partes = linha.split(' - ')
                        nome = partes[0].split(':')[1].strip().lower() 
                        qtd = int(partes[1].split(':')[1].strip())      
                        preco = float(partes[2].split(':')[1].strip()) 
                        grupo = partes[3].split(':')[1].strip()
                        dados[nome] = [qtd, preco, grupo,i]
                        
                    except Exception as e:
                        print(f"Erro ao processar linha: {linha}\nDetalhes: {e}")
    elif os.path.exists('dados_estoque.txt') == False:
        print('Estoque inexistente. Crie o estoque antes de prosseguir.')
        
    return dados


# dados_produtos = carregar_dados_arquivo() #-----> PARA TESTE DE DEBUG
def gerar_novo_id(dados_produtos):
    if not dados_produtos:
        return 0
    return max(produto[3] for produto in dados_produtos.values()) + 1

#FUNÇÃO DE ADICINAR PRODUTOS
def adiconar_produtos(dados_produtos, grupo):
    id_item = gerar_novo_id(dados_produtos)
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
                    with open('dados_estoque.txt', 'a', encoding='utf-8-sig') as a:
                        a.write(f'Nome produto: {nome_prod} - Quantidade: {quantidade} - Preço: {preco} - Grupo: Periféricos - ID: {id_item}\n')
                        dados_produtos.update({f'{nome_prod}': [quantidade, preco, 'Periféricos', id_item]})
                elif nome_prod in grupo['pc_pecas']:
                    with open('dados_estoque.txt', 'a', encoding='utf-8-sig') as a:
                        a.write(f'Nome produto: {nome_prod} - Quantidade: {quantidade} - Preço: {preco} - Grupo: Computadores - ID: {id_item}\n')
                        dados_produtos.update({f'{nome_prod}': [quantidade, preco,'Computadores', id_item]})
                else:
                    with open('dados_estoque.txt', 'a', encoding='utf-8-sig') as a:
                        a.write(f'Nome produto: {nome_prod} - Quantidade: {quantidade} - Preço: {preco} - Grupo: Outros - ID: {id_item}\n')
                        dados_produtos.update({f'{nome_prod}': [quantidade, preco,'Outros', id_item]})
            
            else:
                #VERIFICAÇÃO DE GRUPO
                if nome_prod in grupo['perifericos']:
                    with open('dados_estoque.txt', 'w', encoding='utf-8-sig') as w:
                        w.write(f'Nome produto: {nome_prod} - Quantidade: {quantidade} - Preço: {preco} - Grupo: Periféricos - ID: {id_item}\n')
                        dados_produtos.update({f'{nome_prod}': [quantidade, preco, 'Periféricos', id_item]})
                elif nome_prod in grupo['pc_pecas']:
                    with open('dados_estoque.txt', 'a', encoding='utf-8-sig') as a:
                        a.write(f'Nome produto: {nome_prod} - Quantidade: {quantidade} - Preço: {preco} - Grupo: Computadores - ID: {id_item}\n')
                        dados_produtos.update({f'{nome_prod}': [quantidade, preco,'Computadores', id_item]})
                else:
                    with open('dados_estoque.txt', 'a', encoding='utf-8-sig') as a:
                        a.write(f'Nome produto: {nome_prod} - Quantidade: {quantidade} - Preço: {preco} - Grupo: Outros - ID: {id_item}\n')
                        dados_produtos.update({f'{nome_prod}': [quantidade, preco,'Outros',id_item]})
                        
                        
    except ValueError as error:
        print(f'Entrada inválida: {error}')
        print('Por favor, insira os dados corretamente e tente novamente.')
        input('Pressione Enter para voltar ao menu...')

# adiconar_produtos(dados_produtos=dados_produtos, grupo=grupo)



# # #FUNÇÃO DE REMOVER PRODUTOS
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
            with open('dados_estoque.txt', 'r',encoding='utf-8-sig') as r:
                lista = r.readlines()
                for i, valor in enumerate(lista):
                    nome_arquivo = valor.split(' - ')[0].split(':')[1].strip().lower()
                    if nome_arquivo == remover:
                        del lista[i]
                        with open('dados_estoque.txt', 'w', encoding='utf-8-sig') as w:
                            w.writelines(lista)
                        print(f'Produto "{remover}" removido com sucesso.')
    except ValueError as error:
        print(f'Entrada inválida: {error}')
        print('Por favor, insira os dados corretamente e tente novamente.')
        input('Pressione Enter para voltar ao menu...')
        
# # remover_produtos(dados_produtos=dados_produtos)

# #FUNÇÃO DE ATUALIZAR PRODUTOS
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
            id_original = dados_produtos[produto_atualizar][3]
            
            # Descobrir o grupo correto (string)
            if produto_atualizar in grupo['perifericos']:
                nome_grupo = 'Periféricos'
            elif produto_atualizar in grupo['pc_pecas']:
                nome_grupo = 'Computadores'
            else:
                nome_grupo = 'Outros'
                
            if produto_atualizar in grupo['perifericos']:
                with open('dados_estoque.txt', 'r', encoding='utf-8-sig') as r:
                    lista = r.readlines()
                    for i, valor in enumerate(lista):
                        nome_arquivo = valor.split(' - ')[0].split(':')[1].strip().lower()
                        if nome_arquivo == produto_atualizar:
                            dados_produtos[produto_atualizar] = [nova_quantidade, novo_preco, nome_grupo, id_original]
                            lista[i] = f'Nome produto: {produto_atualizar} - Quantidade: {nova_quantidade} - Preço: {novo_preco} - Grupo: Periféricos - ID: {id_original}\n'
                            with open('dados_estoque.txt', 'w',encoding='utf-8-sig') as w:
                                w.writelines(lista)
                            print(f'Produto "{produto_atualizar}" atualizado com sucesso.')
            elif produto_atualizar in grupo['pc_pecas']:
                with open('dados_estoque.txt', 'r', encoding='utf-8-sig') as r:
                    lista = r.readlines()
                    for i, valor in enumerate(lista):
                        nome_arquivo = valor.split(' - ')[0].split(':')[1].strip().lower()
                        if nome_arquivo == produto_atualizar:
                            dados_produtos[produto_atualizar] = [nova_quantidade, novo_preco, nome_grupo, id_original]
                            lista[i] = f'Nome produto: {produto_atualizar} - Quantidade: {nova_quantidade} - Preço: {novo_preco} - Grupo: Computadores - ID: {id_original}\n'
                            with open('dados_estoque.txt', 'w', encoding='utf-8-sig') as w:
                                w.writelines(lista)
                            print(f'Produto "{produto_atualizar}" atualizado com sucesso.')
            else:
                with open('dados_estoque.txt', 'r', encoding='utf-8-sig') as r:
                    lista = r.readlines()
                    for i, valor in enumerate(lista):
                        nome_arquivo = valor.split(' - ')[0].split(':')[1].strip().lower()
                        if nome_arquivo == produto_atualizar:
                            dados_produtos[produto_atualizar] = [nova_quantidade, novo_preco, 'outros', id_original]
                            lista[i] = f'Nome produto: {produto_atualizar} - Quantidade: {nova_quantidade} - Preço: {novo_preco} - Grupo: Outros - ID: {id_original}\n'
                            with open('dados_estoque.txt', 'w', encoding='utf-8-sig') as w:
                                w.writelines(lista)
                            print(f'Produto "{produto_atualizar}" atualizado com sucesso.')

    except ValueError as error:
        print(f'Entrada inválida: {error}')
        print('Por favor, insira os dados corretamente e tente novamente.')
        input('Pressione Enter para voltar ao menu...')
        
# # atualizar_produtos(dados_produtos=dados_produtos, grupo=grupo)

# #FUNÇÃO DE MOSTRAR NA TELA
def mostrar_tela(tamanho_linha):
    with open('dados_estoque.txt', 'r', encoding='utf-8-sig') as r:
        print('=' * tamanho_linha)
        print('PRODUTOS CADASTRADOS NO ESTOQUE'.center(tamanho_linha))
        print('=' * tamanho_linha)
        print(r.read())
dados_produtos = carregar_dados_arquivo()
while True:
    os.system('cls')
    print('=' * tamanho_linha)
    print('SISTEMA DE ESTOQUE DE ITENS'.center(tamanho_linha))
    print('=' * tamanho_linha)
    #VERIFICAR O ARQUIVOS TXT(BASE DE DADOS) E O DIC E SINCRONIZA-LÓ    
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
        

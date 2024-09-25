from combate import inventario, itens
from time import sleep as sl
from os import system as sy

sy('cls')

# Função que simulará uma loja para vender e comprar itens
def acessar_loja():
    global inventario, itens

    while True:
        # Escolha do usuário para a sua ação
        try:
            escolha = int(input('''Escolha uma ação para fazer na loja:

Vender itens         -> Digite 1
Comprar itens        -> Digite 2
Ver itens na mochila -> Digite 3
Sair da loja         -> Digite 4
                                
              R: '''))
        
            if escolha == 4:
                break
        
            if escolha < 1 or escolha > 3:
                print('Valor inválido. Digite novamente! ')
                sl(3)
                sy('cls')
            
            else:
                break

        
        except ValueError:
            print('Valor inválido. Digite novamente! ')
            sl(3)
            sy('cls')
            continue

    if escolha == 4:
        return
    
    # Escolha do item vender e a quantidade
    if escolha == 1:
        while True:
            # Detectar se tem items para vender
            num = False
            for nome, valor in inventario[2].items():
                if num % 2 == 0:
                    if valor >= 1:
                        num = True

            if num == False:
                print('Você não tem nenhum item para a venda! Escolha novamente: ')
                acessar_loja()

            # Mostrar os produtos vendiveis e o preço
            print('''\n\nSegue a lista dos itens que você possui para vender e o preço de venda: 
              ''')
        
            condicao = 0
            for nome, valor in inventario[2].items():

                if condicao % 2 == 0:
                    print(f'{nome} = {valor} unidades')
            
                else:
                    print(f'Preço = {valor} moedas\n')
            
                condicao += 1
        
            # Escolher qual item vender
            try:
                # Escolhe item
                vender = input('''Digite o nome do item que quer vender (Digite 1 para voltar):\n ''').strip()
                divisao = vender.split()

                if len(divisao) != 2:
                    print('Valor inválido! Digite novamente: ')
                    sl(3)
                    sy('cls')
                    
                vender = divisao[0].capitalize() + ' ' + divisao[1].capitalize()
                


                if vender == '1':
                    sy('cls')
                    acessar_loja()
                    
                condicao2 = False
                condicao3 = 0
                for nome, valor in inventario[2].items():
                    if condicao3 % 2 == 0:
                        if nome == vender:
                            condicao2 = True
                        if valor == 0:
                            print('Você não tem nada desses itens para vender! ')
                            sl(2)
                            sy('cls')
                            continue
                        condicao3 += 1
                        
                if condicao2 == False:
                    print('Valor inválido! Digite novamente: ')
                    sl(3)
                    sy('cls')
                    continue
            
                # Adição, de fato, da quantidade de moedas ao vender os itens
                else:
                    condicao4 = 1
                    for nome, valor in inventario[2].items():
                        if condicao4 % 2 == 1:
                            if nome == vender:
                                preco = 'Preço' + str(condicao4)
                                inventario[3]['Moedas'] += inventario[2][preco] * valor
                                inventario[2][nome] = 0
                                print(f'''Venda bem sucedida!
Foram adicionados {inventario[2][preco] * valor} moedas ao seu inventário, ficando com {inventario[3]['Moedas']} moedas no total! ''')
                                sl(3)
                                sy('cls')
                                acessar_loja()

        
            except ValueError:
                print('Valor inválido! Digite novamente: ')
                sl(3)
                sy('cls')
                continue
    
    # Comprar itens
    if escolha == 2:
        while True:
            try:
                print(f'\nItens disponíveis para compra (você tem {inventario[3]['Moedas']} moedas): ')
                for nome, valor in itens[3].items():
                    print(f'{nome} - {valor} moedas')
                
                pocao_compra = input('\nDigite a poção que deseja comprar (Digite 1 para voltar): ').strip()

                if pocao_compra == '1':
                    sy('cls')
                    acessar_loja()

                divisao = pocao_compra.split()

                if len(divisao) != 2:
                    print('Valor inválido! Digite novamente: ')
                    sl(3)
                    sy('cls')

                pocao_compra = divisao[0].capitalize() + ' ' + divisao[1].capitalize()

                condicao5 = False
                for nome, valor in itens[3].items():
                    if nome.lower() == pocao_compra.lower():
                        condicao5 = True
                        preco = valor
                        if inventario[3]['Moedas'] < valor:
                            print('Você não tem moedas para comprar isso! ')
                            sl(3)
                            sy('cls')
                            continue
                
                if inventario[3]['Moedas'] < itens[3][pocao_compra]:
                    print('Você não tem moedas nem mesmo para comprar 1 dessa poção! Escolha novamente: ')
                    sl(3)
                    sy('cls')
                
                if condicao5 == False:
                    print('Valor inválido! Digite novamente: ')
                    sl(3)
                    sy('cls')
                    continue
                
                # Pergunta quantas poções comprará
                quantidade = int(input('Digite quantas você quer comprar (Digite 1 para voltar): '))
                
                if quantidade == '1':
                    sy('cls')
                    acessar_loja()
                
                if quantidade < 0:
                    print('Valor inválido! Digite novamente: ')
                    sl(3)
                    sy('cls')
                    continue
                
                if quantidade * preco > inventario[3]['Moedas']:
                    print('Você não tem dinheiro suficiente! Digite novamente: ')
                    sl(3)
                    sy('cls')
                    continue
                
                else:
                    print(f'Você comprou {quantidade} {pocao_compra} por {quantidade * preco}! ')
                    inventario[3]['Moedas'] -= quantidade * preco
                    inventario[1][pocao_compra] += quantidade
                        

            except ValueError:
                print('Valor inválido! Digite novamente: ')
                sl(3)
                sy('cls')
                continue
    
    if escolha == 3:
        while True:
            condicao6 = 0
            for nome, quantidade in inventario[2].items():
                if condicao6 % 2 == 0:
                    print(f'{nome} | {quantidade} unidades por item | ', end='')
                else:
                    print(f'Preço: {quantidade} moedas por item')
                
                condicao6 += 1
            
            print('')
            for nome, quantidade in inventario[1].items():
                print(f'{nome} | {quantidade} unidades')

            sl(3)
            pergunta = input('\nDigite qualquer coisa para voltar: ')

            sy('cls')
            acessar_loja()

acessar_loja()
    

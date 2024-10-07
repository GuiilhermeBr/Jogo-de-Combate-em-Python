import random as ra
from nivel import verificar_nivel, aumentar_dano_usuario, aumentar_defesa_usuario
from os import system as sy
from time import sleep as sl

# Itens que existem no jogo e seus respectivos valores

itens = [{
    # Lista de Armaduras
    # Nome | Defesa
    'Armadura de Couro': 10,
    'Armadura de Malha': 15,
    'Armadura de Aço': 25,
    'Armadura de Placas de Ferro': 40
}, {
    # Lista de Espadas
    # Nome | Dano
    'Espada de Madeira': 15,
    'Espada de Aço': 25,
    'Espada de Ferro': 40,
    'Espada Milenar': 50
}, {
    # Lista de Poções
    # Nome | Cura
    'Poção Pequena': 25,
    'Poção Média': 50,
    'Poção Grande': 100
},{
    # Lista de Poções
    # Nome | preço
    'Poção Pequena': 10,
    'Poção Média': 20,
    'Poção Grande': 30
}]

# Inventário do Usuário
# Tem seus itens guardados e equipamentos equipados

inventario = [{
    # Equipamentos equipados
    'Espada Equipada': 'Espada de Madeira',
    'Dano Espada': 15,
    'Armadura Equipada': 'Armadura de Couro',
    'Defesa Armadura': 10
},{
    # Poções que o usuário possui
    'Poção Pequena': 0,
    'Poção Média': 0,
    'Poção Grande': 0
},{
    # Quantidade de itens para venda
},{
    # Quantidade de Moedas
    'Moedas': 0
},{
    # Nível e Experiência do usuário
    'Nível': 1,
    'Experiência': 0
}]


def combate(nome_inimigo, dano_inimigo, vida_inimigo, vida_usuario, vida_max_usuario, chance_fuga, item_ganho, moedas_ganho, experiencia_monstro):
    global inventario
    sy('cls')

    # Variáveis para aumentar o dano e defesa do usuário com base no nível
    porcentagem_dano_usuario = aumentar_dano_usuario()
    porcentagem_defesa_usuario = aumentar_defesa_usuario()

    # Dando valor às variáveis principais
    dano_usuario = inventario[0]['Dano Espada']
    defesa_usuario = inventario[0]['Defesa Armadura']

    # Escolha do Usuário para a ação
    while True:
        try:
            escolha = int(input(f'''Escolha uma opção para lidar com o {nome_inimigo},
ele está com {vida_inimigo} pontos de vida e você {vida_usuario}: 
                                
Atacar (100% de chance) -> Digite 1
Fugir  ({chance_fuga}% de chance) -> Digite 2
Curar  (100% de chance) -> Digite 3'''))

            if escolha < 1 or escolha > 3:
                print('\nValor inválido! Digite novamente: ')
                sl(2)
                sy('cls')
            else:
                break
        
        except ValueError:
            print('\nValor inválido! Digite novamente: ')
            sl(2)
            sy('cls')
            continue

    # Escolha de Poção
    if escolha == 3:
        # Detecta se está com a vida cheia
        if vida_usuario == vida_max_usuario:
            print('Você está com a vida no máximo! ')
            sl(2)
            sy('cls')
            combate(nome_inimigo, dano_inimigo, vida_inimigo, vida_usuario, vida_max_usuario, chance_fuga, item_ganho, moedas_ganho,  experiencia_monstro)

        # Detecta se não tem poções
        elif inventario[1]['Poção Pequena'] == 0 and inventario[1]['Poção Média'] == 0 and inventario[1]['Poção Grande'] == 0:
            print('Você não tem poções para usar agora! ')
            sl(2)
            sy('cls')
            combate(nome_inimigo, dano_inimigo, vida_inimigo, vida_usuario, vida_max_usuario, chance_fuga, item_ganho, moedas_ganho,  experiencia_monstro)

        # Decisão da poção que será utilizada
        while True:
            try:
                pocao = int(input(('''Qual poção você deseja utilizar? 
Poção Pequena (Recupera 25 pontos)  -> Digite 1
Poção Média   (Recupera 50 pontos)  -> Digite 2
Poção Grande  (Recupera 100 pontos) -> Digite 3
Voltar para a escolha anterior      -> Digite 4''')))

                if pocao == 4:
                    combate(nome_inimigo, dano_inimigo, vida_inimigo, vida_usuario, vida_max_usuario, chance_fuga, item_ganho, moedas_ganho,  experiencia_monstro)
                
                elif pocao < 1 or pocao > 3:
                    print('\nValor inválido! Digite novamente: ')
                    sl(2)
                    sy('cls')
                
                # Verifica novamente se tem a poção em específico
                elif inventario[1]['Poção Pequena'] == 0 and pocao == 1:
                    print('\nVocê não tem poções pequenas para usar! Escolha novamente: ')
                    sl(2)
                    sy('cls')
                
                elif inventario[1]['Poção Média'] == 0 and pocao == 2:
                    print('\nVocê não tem poções médias para usar! Escolha novamente: ')
                    sl(2)
                    sy('cls')
                
                elif inventario[1]['Poção Grande'] == 0 and pocao == 3:
                    print('\nVocê não tem poções grandes para usar! Escolha novamente: ')
                    sl(2)
                    sy('cls')
                
                else:
                    if pocao == 1:
                        vida_usuario += 25

                        if vida_usuario > vida_max_usuario:
                            vida_usuario = vida_max_usuario

                        inventario[1]['Poção Pequena'] -= 1
                        print(f'Você curou 25 pontos de vida! Ficando com {vida_usuario} pontos de vida! ')
                        sl(2)
                        sy('cls')

                    elif pocao == 2:
                        vida_usuario += 50

                        if vida_usuario > vida_max_usuario:
                            vida_usuario = vida_max_usuario

                        inventario[1]['Poção Média'] -= 1
                        print(f'Você curou 50 pontos de vida! Ficando com {vida_usuario} pontos de vida! ')
                        sl(2)
                        sy('cls')

                    else:
                        vida_usuario += 100

                        if vida_usuario > vida_max_usuario:
                            vida_usuario = vida_max_usuario

                        inventario[1]['Poção Grande'] -= 1
                        print(f'Você curou 100 pontos de vida! Ficando com {vida_usuario} pontos de vida! ')
                        sl(2)
                        sy('cls')
                    
                    break
            
            except ValueError:
                print('\nValor inválido! Digite novamente: ')
                sl(2)
                sy('cls')
                continue

    # Decisão se irá fugir ou não
    if escolha == 2:
        numero_aleatorio_chance = ra.randint(1, 100)

        if numero_aleatorio_chance <= chance_fuga:
            print('Você escapou com sucesso. Parabéns!')
            sl(2)
            return

    # Escolha de ataque do usuário
    if escolha == 1:
        while True:
            try:
                ataque_usuario = int(input(f'''Escolha um ataque para usar contra o {nome_inimigo}: 
Ataque Rápido (80% de chance de acerto | {dano_usuario // 2} de dano) -> Digite 1
Ataque Normal (60% de chance de acerto | {dano_usuario} de dano)      -> Digite 2
Ataque Forte  (40% de chance de acerto | {dano_usuario * 2} de dano)  -> Digite 3
Voltar para a escolha anterior                                        -> Digite 4
                                    '''))

                if ataque_usuario < 1 or ataque_usuario > 3:
                    print('\nValor inválido! Digite novamente: ')
                    sl(2)
                    sy('cls')
                else:
                    break
        
            except ValueError:
                print('\nErro! Digite novamente: ')
                sl(2)
                sy('cls')
                continue
        
        # Calcula a probabilidade de acerto do ataque
        numero_aleatorio_chance = ra.randint(1, 100)

        # Ataque rápido
        if ataque_usuario == 1:
            if numero_aleatorio_chance <= 80:
                vida_inimigo -= dano_usuario // 2 * porcentagem_dano_usuario
                if vida_inimigo < 0:
                    vida_inimigo = 0

                print(f'''Você acertou o ataque, causando {dano_usuario // 2} pontos de dano a vida do {nome_inimigo}.
Ele ficou com {vida_inimigo} pontos de vida! ''')
                sl(2)

            else:
                print('Você errou o ataque! ')
                sl(2)

        # Ataque normal
        if ataque_usuario == 2:
            if numero_aleatorio_chance <= 60:
                vida_inimigo -= dano_usuario * porcentagem_dano_usuario
                if vida_inimigo < 0:
                    vida_inimigo = 0

                print(f'''Você acertou o ataque, causando {dano_usuario} pontos de dano a vida do {nome_inimigo}.
Ele ficou com {vida_inimigo} pontos de vida! ''')
                sl(2)

            else:
                print('Você errou o ataque! ')
                sl(2)

        # Ataque forte
        if ataque_usuario == 3:
            if numero_aleatorio_chance <= 40:
                vida_inimigo -= dano_usuario * 2 * porcentagem_dano_usuario
                if vida_inimigo < 0:
                    vida_inimigo = 0

                print(f'''Você acertou o ataque, causando {dano_usuario * 2} pontos de dano a vida do {nome_inimigo}.
Ele ficou com {vida_inimigo} pontos de vida! ''')
                sl(2)

            else:
                print('Você errou o ataque! ')
                sl(2)

    # Ataque do inimigo
    if vida_inimigo != 0:
        numero_aleatorio_chance = ra.randint(1, 100)
        numero_aleatorio_ataque = ra.randint(1, 100)

        # Escolha do ataque Rápido
        if numero_aleatorio_ataque <= 33:
            print(f'O {nome_inimigo} usou um ataque rápido! ')
            sl(2)

            if numero_aleatorio_chance <= 80:
                calculo_de_dano = (dano_inimigo // 2) - defesa_usuario * porcentagem_defesa_usuario

                if calculo_de_dano > 0:
                    vida_usuario -= calculo_de_dano
                else:
                    calculo_de_dano = 0

                if vida_usuario < 0:
                    vida_usuario = 0
                
                print(f'''O {nome_inimigo} acertou o ataque, causando {calculo_de_dano} pontos de dano!
Você ficou com {vida_usuario} pontos de vida restando. ''')
                sl(2)
            
            else:
                print(f'O {nome_inimigo} errou o ataque! ')
                sl(2)

        # Escolha do Ataque Normal
        elif numero_aleatorio_ataque > 33 and numero_aleatorio_ataque <= 66:
            print(f'O {nome_inimigo} usou um ataque normal! ')
            sl(2)

            if numero_aleatorio_chance <= 60:
                calculo_de_dano = dano_inimigo - defesa_usuario * porcentagem_defesa_usuario

                if calculo_de_dano > 0:
                    vida_usuario -= calculo_de_dano
                else:
                    calculo_de_dano = 0

                if vida_usuario < 0:
                    vida_usuario = 0
                
                print(f'''O {nome_inimigo} acertou o ataque, causando {calculo_de_dano} pontos de dano!
Você ficou com {vida_usuario} pontos de vida restando. ''')
                sl(2)
            
            else:
                print(f'O {nome_inimigo} errou o ataque! ')
                sl(2)

        # Escolha do Ataque Forte
        elif numero_aleatorio_ataque > 66 and numero_aleatorio_ataque <= 100:
            print(f'O {nome_inimigo} usou um ataque forte! ')
            sl(2)

            if numero_aleatorio_chance <= 40:
                calculo_de_dano = (dano_inimigo * 2) - defesa_usuario * porcentagem_defesa_usuario

                if calculo_de_dano > 0:
                    vida_usuario -= calculo_de_dano
                else:
                    calculo_de_dano = 0

                if vida_usuario < 0:
                    vida_usuario = 0
                
                print(f'''O {nome_inimigo} acertou o ataque, causando {calculo_de_dano} pontos de dano!
Você ficou com {vida_usuario} pontos de vida restando. ''')
                sl(2)
            
            else:
                print(f'O {nome_inimigo} errou o ataque! ')
                sl(2)

    # Finalização detectando se um dos dois foram derrotados, caso não, repetir a função
    if vida_inimigo == 0:
        quantidade_itens_aleatorio = ra.randint(1, 3)

        print('Você derrotou o inimigo! Parabéns! ')
        print(f'Você ganhou {experiencia_monstro} pontos de experiência! ')
        sl(2)
        inventario[4]['Experiência'] += experiencia_monstro
        verificar_nivel()

        print(f'Você também ganhou {quantidade_itens_aleatorio} {item_ganho} e {moedas_ganho} moedas')
        inventario[3]['Moedas'] += moedas_ganho
        inventario[2][item_ganho] += quantidade_itens_aleatorio
        sl(2)
    
    elif vida_usuario == 0:
        print('\nVocê foi derrotado! ')
        sl(2)
        sy('cls')
    
    else:
        combate(nome_inimigo, dano_inimigo, vida_inimigo, vida_usuario, vida_max_usuario, chance_fuga, item_ganho, moedas_ganho,  experiencia_monstro)

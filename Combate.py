import random as rd
from os import system as sy
from time import sleep as sp

sy('cls')


# Itens que existem no jogo e seus respectivos valores

itens = [{
    # Lista de Armaduras
    # Nome | Defesa
    'Armadura de Couro': 10,
    'Armadura de Malha': 15,
    'Armadura de Aço': 25,
    'Armadura de Placas de Ferro': 40
},{
    # Lista de Espadas
    # Nome | Dano
    'Espada de Madeira': 15,
    'Espada de Aço': 25,
    'Espada de Ferro': 40,
    'Espada Milenar': 50
},{
    # Lista de Poções
    # Nome | Cura
    'Poção Pequena': 25,
    'Poção Média': 50,
    'Poção Grande': 100
}]

# Inventário do Usuário
# Tem seus itens guardados e equipamentos equipados

inventario = [{
    # Equipamentos equipados
    'Espada equipada': 'Espada de Madeira',
    'Armadura equipada': 'Armadura de Couro'
},{
    # Poções que o usuário possui
    'Poção Pequena': 0,
    'Poção Média': 0,
    'Poção Grande': 0
},{
    # Quantidade de Itens para venda
}]

def combate(nome_inimigo, dano_inimigo, vida_inimigo, dano_usuario, vida_usuario, vida_max_usuario, chance_fuga):
    sy('cls')

    # Introdução ao combate
    print(f'''Um {nome_inimigo} apareceu!
Ele parece hostil e não hesita em lhe enfrentar!
Ele possui {vida_inimigo} pontos de vida.''')
    
    while True:
        try:
            escolha = int(input('''Escolha uma opção para lidar com o oponente: 
Atacar (100% de chance) -> Digite 1
Fugir  ({chance_fuga}% de chance) -> Digite 2
Curar  (100% de chance) -> Digite 3'''))
            
            if escolha < 1 or escolha > 3:
                print('\nValor inválido! Digite novamente: ')
                sp(3)
                sy('cls')

            else:
                break
        
        except ValueError:
            print('\nValor inválido! Digite novamente: ')
            sp(3)
            sy('cls')
    
    while True:
        try:
            ataque_usuario = int(input(f'''Escolha um ataque para usar contra seu oponente: 
Ataque Rápido (80% de chance de acerto | {dano_usuario // 2} de dano) -> Digite 2
Ataque Padrão (60% de chance de acerto | {dano_usuario} de dano) -> Digite 1
Ataque Forte  (40% de chance de acerto | {dano_usuario * 2} de dano) -> Digite 3
                                    '''))
            
            if ataque_usuario < 1 or ataque_usuario > 3:
                print('\nValor inválido! Digite novamente: ')
                sp(3)
                sy('cls')
            else:
                break
        
        except ValueError:
            print('\nErro! Digite novamente: ')
            sp(3)
            sy('cls')
            continue
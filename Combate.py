import random
from time import sleep
import os
os.system('cls')
# Combate!
# Variáveis | Usuário
vida_usuario = 100
inventario = [
    ['Poção Pequena', 0, 'Poção Média', 0, 'Poção Grande', 0],
    ['Armadura de Couro', 5, 'Armadura de Malha', 10, 'Armadura de Aço', 15],
    ['Espada de Madeira', 10, 'Espada de Pedra', 20, 'Espada de Ferro', 30]
]
espada_equipada = 'Espada de Madeira'
armadura_equipada = 'Armadura de Couro'
dinheiro_ganhado = 0
vida_máxima = 100
dinheiro_total = 0
escolha2 = 0
# Variáveis | Inimigo
vida_inimigo = 0
inimigos = ['Goblin', 'Esqueleto', 'Orc', 'Lobo', 'Zumbi']
ataques = ['Ataque Rápido', 'Ataque Forte']



def combate():
    global vida_usuario, vida_inimigo
    global inventario
    global dinheiro_ganhado
    global dinheiro_total
    global escolha2

    if inventario[1][0] == armadura_equipada:
        defesa = 5
    elif inventario[1][1] == armadura_equipada:
        defesa = 10
    elif inventario[1][2] == armadura_equipada:
        defesa = 15
    else:
        defesa = 0

    if inventario[2][0] == espada_equipada:
        dano_usuario = 10
    elif inventario[2][2] == espada_equipada:
        dano_usuario = 20
    elif inventario[2][4] == espada_equipada:
        dano_usuario = 30

    while True:
        # Variável que escolhe o inimigo
        x = random.choice(inimigos)

        # Escolha do inimigo
        if x == 'Goblin':
            vida_inimigo = 20
            dano_inimigo = 5
        elif x == 'Esqueleto':
            vida_inimigo = 30
            dano_inimigo = 7
        elif x == 'Orc':
            vida_inimigo = 40
            dano_inimigo = 8
        elif x == 'Lobo':
            vida_inimigo = 25
            dano_inimigo = 6
        elif x == 'Zumbi':
            vida_inimigo = 50
            dano_inimigo = 10

        # Introdução ao contexto
        print(f'''Um {x} selvagem apareceu! Ele tem {vida_inimigo} pontos de vida!
Você deseja utilizar o ataque rápido[{dano_usuario} de dano/80%], ou ataque forte[{dano_usuario * 2} de dano/60%]
ou você deseja utilizar uma poção de cura?''')

        # Escolha de fato do ataque
        while True:
            try:
                escolha = int(input(f''' 
                    Ataque rápido[1] | Ataque forte[2] | Poção de cura[3]
                                         '''))
                os.system('cls')
                if escolha > 3:
                    print('Erro! Tente digitar novamente: ')
                    continue
                if escolha <= 0:
                    print('Erro! Tente digitar novamente: ')
                    continue

                # Escolha utilizar poção(se tiver)
                if escolha == 3:
                    if inventario[0][1] == 0 and inventario[0][3] == 0 and inventario[0][5] == 0:
                        print('Erro! Você não possui poções! Escolha novamente: ')
                        continue
                    if vida_usuario == vida_máxima:
                        print('Você já está com a vida cheia! ')
                        continue
                    if inventario[0][1] > 0 or inventario[0][3] > 0 or inventario[0][5] > 0:
                        while True:
                            try:
                                escolha2 = int(input(f'''Você possui {inventario[0][1]} poções pequenas[+25],
{inventario[0][3]} poções médias[+50] e {inventario[0][5]} poções grandes[+100]!
Qual delas você deseja utilizar?

                    Poção Pequena[1] | Poção Média[2] | Poção Grande[3] | Cancelar[4]
                                                      '''))
                                if escolha2 < 1 or escolha2 > 4:
                                    print('\nErro! Tente novamente: \n')
                                    continue

                                # Poção Pequena
                                if escolha2 == 1 and inventario[0][1] == 0:
                                    print('Você não possui poções pequenas, escolha novamente: ')
                                    continue
                                elif escolha2 == 1 and inventario[0][1] > 0:
                                    vida_usuario += 25
                                    if vida_usuario > vida_máxima:
                                        vida_usuario = vida_máxima
                                    print(
                                        f'Você utilizou uma poção pequena! Agora você está com {vida_usuario} pontos de vida! ')
                                    inventario[0][1] -= 1
                                    break

                                # Poção Média
                                if escolha2 == 2 and inventario[0][3] == 0:
                                    print('Você não possui poções médias, escolha novamente: ')
                                    continue
                                elif escolha2 == 2 and inventario[0][3] > 0:
                                    vida_usuario += 50
                                    if vida_usuario > vida_máxima:
                                        vida_usuario = vida_máxima
                                    print(
                                        f'Você utilizou uma poção média! Agora você está com {vida_usuario} pontos de vida! ')
                                    inventario[0][3] -= 1
                                    break

                                # Poção Grande
                                if escolha2 == 3 and inventario[0][5] == 0:
                                    print('Você não possui poções grandes, escolha novamente: ')
                                    continue
                                elif escolha2 == 3 and inventario[0][5] > 0:
                                    vida_usuario += 100
                                    if vida_usuario > vida_máxima:
                                        vida_usuario = vida_máxima
                                    print(
                                        f'Você utilizou uma poção grande! Agora você está com {vida_usuario} pontos de vida! ')
                                    inventario[0][5] -= 1
                                    break

                                # Cancelar
                                if escolha2 == 4:
                                    print('Escolha cancelada! ')
                                    break

                            except ValueError:
                                print('\nErro! Tente novamente: \n')
                                continue

                if escolha2 == 4:
                    escolha2 = None
                    continue

                # Escolha ataque rápido
                if escolha == 1:
                    randomizado = random.randint(1, 5)
                    if randomizado == 1 or randomizado == 2 or randomizado == 3 or randomizado == 4:
                        vida_inimigo -= dano_usuario
                        print(
                            f'Você acertou o ataque! Dessa forma, você causou {dano_usuario} de dano ao total de vida do oponente!')
                        if vida_inimigo < 0:
                            vida_inimigo = 0
                        print(f'A vida do inimigo ficou em {vida_inimigo} pontos de vida! ')
                    else:
                        print('Você errou o ataque! Dessa forma, você não causou dano ao oponente! ')

                # Escolha ataque forte
                elif escolha == 2:
                    randomizado = random.randint(1, 5)
                    if randomizado == 1 or randomizado == 2 or randomizado == 3:
                        vida_inimigo -= dano_usuario * 2
                        print(
                            f'Você acertou o ataque! Dessa forma, você causou {dano_usuario} de dano ao total de vida do oponente!')
                        if vida_inimigo < 0:
                            vida_inimigo = 0
                        print(f'A vida do inimigo ficou em {vida_inimigo} pontos de vida! ')
                    else:
                        print('Você errou o ataque! Dessa forma, você não causou dano ao oponente! ')

            except ValueError:
                print('Erro! Tente digitar novamente: ')
                continue
            print('')

            # Checa a vida do inimigo e dá a devida resposta e dinheiro como recompensa
            if vida_inimigo <= 0:
                vida_usuario = 0
                sleep(3)
                print(f'Parabéns! Você derrotou o {x} selvagem! ')
                if x == 'Goblin':
                    dinheiro_ganhado += 5
                elif x == 'Esqueleto':
                    dinheiro_ganhado += 10
                elif x == 'Orc':
                    dinheiro_ganhado += 15
                elif x == 'Lobo':
                    dinheiro_ganhado += 12.5
                elif x == 'Zumbi':
                    dinheiro_ganhado += 20
                break

            if vida_usuario <= 0:
                vida_usuario = 0
                print('Sua vida chegou a zero! Ou seja, você morreu e perdeu todo seu progresso! ')
                break

            # Ataque do inimigo | Variáveis
            estilo_ataque = random.choice(ataques)
            randomizado2 = random.randint(1, 10)

            # Ataque do inimigo | De fato
            sleep(3)
            print('Agora é a vez do oponente atacar! ')
            sleep(1)
            print(f'O ataque utilizado foi o {estilo_ataque}! ')

            # Escolha Ataque rápido
            if estilo_ataque == 'Ataque Rápido':
                if randomizado2 == 1 or randomizado2 == 2:
                    if dano_inimigo > defesa:
                        resultado = dano_inimigo - defesa
                    elif dano_inimigo < defesa:
                        resultado = 0
                    else:
                        resultado = 0
                    vida_usuario -= resultado
                    sleep(1)
                    print(f'O {x} acertou o ataque! Causando {dano_inimigo} de dano ao usuário! ')
                    sleep(1)
                    print(f'A sua vida atual é {vida_usuario}! ')
                else:
                    sleep(1)
                    print(f'O {x} errou o ataque! Causando nenhum dano ao usuário! ')

            # Escolha Ataque forte
            if estilo_ataque == 'Ataque Forte':
                if randomizado2 == 1:
                    dano_inimigo = dano_inimigo * 2
                    if dano_inimigo > defesa:
                        resultado = dano_inimigo - defesa
                    elif dano_inimigo < defesa:
                        resultado = 0
                    else:
                        resultado = 0
                    vida_usuario -= resultado
                    sleep(1)
                    print(f'O {x} acertou o ataque! Causando {dano_inimigo * 2} de dano ao usuário! ')
                    sleep(1)
                    print(f'A sua vida atual é {vida_usuario}! ')
                else:
                    sleep(1)
                    print(f'O {x} errou o ataque! Causando nenhum dano ao usuário! ')

            if vida_usuario > 0 and vida_inimigo > 0:
                sleep(3)
                print('''
    Escolha seu próximo ataque: ''')
        dinheiro_total += dinheiro_ganhado
        print(f'Você ganhou {dinheiro_ganhado} moedas, ficando com {dinheiro_total} moedas no total! ')
        dinheiro_ganhado = 0
        break
    print('Fim do programa combate! ')


combate()
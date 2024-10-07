from os import system as sy
from time import sleep as sl
from combate import inventario

# Função para verificar se o usuário poderá evoluir de nível com base em sua experiência(XP) atual
def verificar_nivel():
    if inventario[4]['Nível'] == 100:
        print('Você ja chegou ao nível máximo! ')
        return
    
    global aumento_dano_usuario, aumento_defesa_usuario

    aumento_dano_usuario = 1
    aumento_defesa_usuario = 1

    # Variável que checará se o usuário terá experiência para evoluir de nível
    experiencia_necessaria = 10 # Experiência necessária para ir do 1 ao 2

    # Calcula quanto de experiência é necessária para upar de level com base no nível atual
    for x in range(1, 101):
        if inventario[4]['Nível'] == x:
            experiencia_necessaria *= x # Será 10 pontos a mais a cada nível upado
            break
    
    # Aplica, se tiver experiência suficiente, para upar ou não o level do usuário
    if inventario[4]['Experiência'] >= experiencia_necessaria:
        inventario[4]['Nível'] += 1
        inventario[4]['Experiência'] = 0
        sy('cls')
        sl(2)
        print(f'Você evolui de level com sucesso! Agora você está no level {inventario[4]['Nível']}! ')
        sl(2)
    
    # Verifica o nível do usuário e devolve o aumento do dano e defesa com base nesses dados
    for x in range(1, 101):
        if inventario[4]['Nível'] == x:
            aumento_dano_usuario = x * 0.01 + 1 # Dará o dano em porcentagem, se for nível 10 dará o dano * 1.1
            aumento_defesa_usuario = x * 0.02 + 1 # Dará a defesa em porcentagem, se for nível 10 terá defesa * 1.2

# Função para definir o aumento do dano para o arquivo combate
def aumentar_dano_usuario():
    return aumento_dano_usuario

# Função para definir o aumento da defesa para o arquivo combate
def aumentar_defesa_usuario():
    return aumento_defesa_usuario
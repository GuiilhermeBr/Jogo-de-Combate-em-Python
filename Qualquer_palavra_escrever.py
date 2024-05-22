import os
import time
os.system('cls')

alfa = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz ãÃõÕcÇ.,'
palavra = input('Digite qualquer coisa: ')
pala_feita = ''

for x in palavra:
    for y in alfa:
        time.sleep(0.01)
        if x == y:
            pala_feita += x
            print(pala_feita)
            break
        else:
            print(pala_feita + y)
os.system('cls')
print('Processando...')
time.sleep(2)
os.system('cls')
print('Frase digitada:', pala_feita)
print('')
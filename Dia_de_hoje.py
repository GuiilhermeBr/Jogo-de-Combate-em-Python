import os
import datetime
os.system('cls')

dia = datetime.date.today().day
mes = datetime.date.today().month
ano = datetime.date.today().year

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

for x in range(0, 11):
    if x == mes:
        mes = meses[x - 1]
print(f'Hoje é dia {dia} de {mes} de {ano}! ')

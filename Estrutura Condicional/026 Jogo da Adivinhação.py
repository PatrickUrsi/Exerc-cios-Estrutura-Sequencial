# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# Peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import choice #Retorna um elemento da sequência sorteada
from time import sleep
sort = [0,1,2,3,4,5]
print(f'-='*25,'\nVou pensar em um número de 0 a 5. Tente advinhar...')
print('-='*25)
n = int(input('Em qual número eu pensei ? '))
print('PROCESSANDO...')
sleep(3)
if choice(sort) == n:
    print('PARABÉNS, Você conseguiu me vencer !')
else: print(f'GANHEI, Eu pensei no número {choice(sort)}, e não no {n} !')

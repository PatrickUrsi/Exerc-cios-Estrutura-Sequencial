# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

t = int(input('Digite um número para visualizar a tabuada: '))
cont = 1
while cont <= 10:
    print(f'{t} X {cont} = {t*cont}')
    cont += 1

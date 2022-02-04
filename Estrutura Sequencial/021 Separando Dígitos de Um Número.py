# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

valor = int(input('Digite um número de 0 a 9999: '))
print(f'Unidade: {valor // 1 % 10}\n'
      f'Dezena: {valor // 10 % 10}\n'
      f'Centena: {valor // 100 % 10}\n'
      f'Milhar: {valor // 1000 % 10}')
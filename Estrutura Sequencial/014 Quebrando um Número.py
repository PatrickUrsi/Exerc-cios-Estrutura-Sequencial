# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math
s = float(input('Digite um número flutuante: '))
print(f'Valor digitado foi {s} sua parte inteira é {math.trunc(s)}')

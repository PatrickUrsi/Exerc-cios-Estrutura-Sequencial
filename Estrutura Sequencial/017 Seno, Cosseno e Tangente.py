# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do
# seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians
a = int(input('Digite o valor de um ângulo: '))
f = radians(a)
print(f'O ângulo de {a}° tem o SENO de {sin(f):.2f}\nO ângulo de {a}° tem o COSSENO de {cos(f):.2f}')
print(f'O ângulo de {a}° tem a TANGENTE de {tan(f):.2f}')

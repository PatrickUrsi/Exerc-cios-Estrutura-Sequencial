# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))

if n1 > n2 and n1 > n3:
    print(f'O número {n1} é o maior valor !')
elif n2 > n3:
    print(f'O número {n2} é o maior valor !')
else:
    print(f'O número {n3} é o maior valor !')

if n1 < n2 and n1 < n3:
    print(f'O número {n1} é o menor valor !')
elif n2 < n3:
    print(f'O número {n2} é o menor valor !')
else:
    print(f'O número {n3} é o menor valor !')
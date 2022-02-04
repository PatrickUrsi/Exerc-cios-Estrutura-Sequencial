# Crie um programa que leia o nome completo de uma pessoa e mostre
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo sem considerar espaços.
# Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: '))
print(f'Seu nome em letras maiúsculas: {nome.upper()}')
print(f'Seu nome em letras minúsculas: {nome.lower()}')
print(f'Seu nome contém {len(nome) - nome.count(" ")} caracteres.')
nome = nome.split()
print(f'Seu primeiro nome contém {len(nome[0])} caracteres.')

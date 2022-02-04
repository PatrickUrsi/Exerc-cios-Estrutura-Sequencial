# Faça um programa que leia o nome completo de uma pessoa.
# Mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip().split()
print(f'Prazer em conhece-lo!\nSeu primeiro nome é {nome[0]}\n'
      f'Seu segundo nome é {nome[len(nome)-1]}')
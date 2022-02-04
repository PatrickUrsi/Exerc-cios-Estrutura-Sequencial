# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Digite o seu salário R$: '))
print(f'Você vai receber reajuste de 15% no seu salário de R${s:.2f} para R${s+s*0.15:.2f}')

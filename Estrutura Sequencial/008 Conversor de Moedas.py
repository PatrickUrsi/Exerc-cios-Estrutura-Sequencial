# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira.
# E mostre quantos dólares ela pode comprar.

r = float(input('Quantos R$ você tem na carteira ? '))
d = r / 3.27
print(f'Com R${r:.2f} você pode comprar US${d:.2f}')

# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,com 5% de desconto.

p = float(input('Digite o valor do produto R$: '))
print(f'Produto que custava R${p:.2f} Na promoção com 5% de desconto você paga R${p-p*0.05:.2f} APROVEITE !')

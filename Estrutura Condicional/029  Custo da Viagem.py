# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

d = float(input('Digite a distância da sua viagem em Km: '))
if d <= 200:
    print(f'Valor da sua passagem será de R${d*0.50:.2f}')
else:
    print(f'Valor da sua passagem será de R${d*0.45:.2f}')

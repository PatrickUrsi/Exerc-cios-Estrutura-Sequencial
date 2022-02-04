# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# E a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

car = float(input('Digite a quantidade percorrida em KM: '))
day = int(input('Digite a quantidade de dias que o carro foi alugado: '))
pagar = day*60 + car*0.15
print(f'Custo diário por dia alugado R${day*60:.2f}\nCusto por KM rodado R${car*0.15:.2f}')
print(f'Valor total a ser pago R${pagar:.2f}')

#  Escreva um programa que leia a velocidade de um carro.
#  Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#  A multa vai custar R$7,00 por cada Km acima do limite.

speed = float(input('Qual é a velocidade do carro ? '))
if speed > 80:
    print(f'Você foi MULTADO em R${(speed-80)*7:.2f} por dirigir acima da velocidade permitida.\n'
          f'A multa vai custar R$7.00 por cada Km acima do limite.')
print('Dirija com CUIDADO e SEGURANÇA !')

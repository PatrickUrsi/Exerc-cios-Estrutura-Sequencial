# Faça um programa que leia a largura e a altura de uma parede em metros.
# Calcule a sua área e a quantidade de tinta necessária para pintá-la.
# Sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = altura*largura/2
print(f'Quantidade de tinta necessária para pintar esta área total: {area:.1f}l')

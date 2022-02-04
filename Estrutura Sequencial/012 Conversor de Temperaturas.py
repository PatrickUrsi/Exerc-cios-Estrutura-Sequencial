# Escreva um programa que converta uma temperatura digitando em graus Celsius
# E converta para graus Fahrenheit.

c = float(input('Digite a temperatura atual em Celsius para converter em Fahrenheit: '))
print(f'Temperatura em Celsius {c:.1f}°C\nTemperatura em Fahrenheit {(c*1.8)+32:.1f}°F')

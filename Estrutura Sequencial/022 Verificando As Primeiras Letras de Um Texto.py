# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input(f'Digite o nome de uma cidade: ')).strip()
print('Santo' in cidade.title())

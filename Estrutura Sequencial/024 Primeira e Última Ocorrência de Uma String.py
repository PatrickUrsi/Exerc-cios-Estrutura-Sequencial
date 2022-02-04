#  Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”.
#  Em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip().lower()
print(f'A letra A apareceu na frase {frase.count("a")} vezes.\n'
      f'A primeira letra A apareceu na posição {frase.find("a")+1}.\n'
      f'A última letra A apareceu na posição {frase.rfind("a")+1}')

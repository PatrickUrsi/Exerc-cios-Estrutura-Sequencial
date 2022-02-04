# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
a1 = str(input('Digite o nome do aluno 1/4: '))
a2 = str(input('Digite o nome do aluno 2/4: '))
a3 = str(input('Digite o nome do aluno 3/4: '))
a4 = str(input('Digite o nome do aluno 4/4: '))
lista = [a1, a2, a3, a4]
s = shuffle(lista)
print(f'A ordem de apresentação do trabalho é {lista}')

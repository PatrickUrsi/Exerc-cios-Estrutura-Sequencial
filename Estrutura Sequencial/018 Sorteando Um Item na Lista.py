#  Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#  Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice
a1 = str(input('Digite o nome do aluno 1/4: '))
a2 = str(input('Digite o nome do aluno 2/4: '))
a3 = str(input('Digite o nome do aluno 3/4: '))
a4 = str(input('Digite o nome do aluno 4/4: '))
lista = [a1, a2, a3, a4]
sorteio = choice(lista)
print(sorteio)

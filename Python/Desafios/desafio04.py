#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice

aluno1 = str(input('Diga o nome do Primeiro aluno:'))
aluno2 = str(input('Diga o nome do Segundo aluno:'))
aluno3 = str(input('Diga o nome do Terceiro aluno:'))
aluno4 = str(input('Diga o nome do Quarto aluno:'))

lista = []
escolhido = random.choice(lista)
print('O aluno sorteado foi: {}'.format(escolhido))
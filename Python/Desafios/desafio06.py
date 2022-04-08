#Escreva um programa que faça o computador "pensar" em um número inteiro 
#entre 0 e 5 e peça para o usuário tentar descobrir qual foi o 
#número escolhido pelo computador. 
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
computador = int(random.randint(0,5))
print(str('Estou pensando em numero entre o e 5'))
usuario = int(input('Qual numero pensei?'))
if computador == usuario:
    print('O numero que pensei foi o {} e você acertou, parabéns!!'.format(computador))
else:
    print('O numero que pensei foi o {} e você errou, que pena.'.format(computador))
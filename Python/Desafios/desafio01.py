#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
carteira = float(input('Quantos reais você tem na carteira R$?'))
dola_hoje = 4.70
conversor = carteira/dola_hoje
if carteira == int:
    carteira = float
else:

    print('Com R${:.2f} reais que você tem hoje, você pode comprar ${:.2f} dolares'.format(carteira,conversor)) 
    

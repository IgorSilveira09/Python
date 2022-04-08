
#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
produto =float(input('Quanto custa o produto?R$'))
perc_desc = int(input('Quantos porcento de desconto você gostaria?%'))
desconto = (perc_desc/100)*produto
preco_final = produto - desconto
print('Para um produto que custa R${:.2f} reais, com desconto de {}%,você pagará apenas R${:.2f} reais'.format(produto,perc_desc,preco_final)

)

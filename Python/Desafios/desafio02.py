    
#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

altura = float(input('Quanto de altura tem sua parede? (em metros)'))
largura = float(input('Quanto de largura tem a parede?(em metros)'))
area = float(altura * largura)
lata_pinta = int(2)
if area <= lata_pinta:
   print('Você precisará de apenas 1 lata de tinta')
else:
    lata_pinta = int(area - 2)
    print('Você precisará de {} latas'.format(lata_pinta))


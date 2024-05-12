# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-las, sabendo que cada litro de tinta pinta uma área de 2m².

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura*altura
print ('Sua parede tem dimensão de {} x {} e a sua área é de {}m²'.format(largura,altura,area))
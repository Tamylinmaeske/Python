# Crie um programa que leia o quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.Considere US$1.00 = R$5.16 (09/05/2024)

valor = float (input('Quantos de R$ você possui? R$ '))
quantidade = valor/5.16
print ('Com R${:.2f}, é possível comprar US${:.2f}'.format(valor,quantidade))
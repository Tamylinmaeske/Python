# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida= float(input('Digite uma medida em metros: '))
cc = medida*100
mm = medida*1000
print ('A medida {:.2f} metros, em centímetros equivale a {:.2f}, e em milímetros equivale a {:.2f}'.format(medida,cc,mm))
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int (input('Digite um número: '))
dobro= n*2
triplo= n*3
rq= n**(1/2)
print ('O número escolhido foi {}.\nO dobro desse número é {}.\nO triplo é {}.\nE a raiz quadrada é {:.0f}.'.format(n,dobro,triplo,rq))
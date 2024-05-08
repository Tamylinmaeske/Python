# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e antecessor.

n = int (input('Digite um número inteiro: '))
s = n+1
a = n-1
print ('O valor escolhido foi {}.\nO antecessor desse número é o {}.\nO sucessor é o {}.'.format(n, a, s))
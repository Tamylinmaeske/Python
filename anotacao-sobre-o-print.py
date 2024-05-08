# É possível utilizar o comando {}.format()) de outra forma.

nome = input ('Olá, qual é o seu nome? ')
print ('Muito prazer {}, o meu nome é Tamylin!'.format(nome))

# Alterando a posição em que o nome aparece, nesse exemplo ele escreveu o nome em 20 espaços {:20}
print ('Muito prazer {:20}, o meu nome é Tamylin!'.format(nome))

# Também é possível indicando a posição {:>20} ou {:<20}
print ('Muito prazer {:>20}, o meu nome é Tamylin!'.format(nome))
print ('Muito prazer {:<20}, o meu nome é Tamylin!'.format(nome))

# Centralizar {:^20}
print ('Muito prazer {:^20}, o meu nome é Tamylin!'.format(nome))

# Até adicionar caracteres {:=^20}
print ('Muito prazer {:=^20}, o meu nome é Tamylin!'.format(nome))

# Delimitar a quantidade de casas dos números flutuantes {:.2f}
n = float (input('Digite um número: '))
print ('Número ajustado {:.2f}'.format(n))

# Para não quebrar a linha ,end=' ', também é possível incluir caracteres entre as aspas. ,end='**'
print ('Muito prazer {}, o meu nome é Tamylin!'.format(nome),end='')
print (' O resultado é {}'.format(n))
print ('Muito prazer {}, o meu nome é Tamylin!'.format(nome),end='**')

# Para quebrar a linha \n
print ('Estou feliz em te conhecer \n {}!'.format(nome))
print (' O resultado é {}'.format(n))



a = 10
b = 5
c = a * b
print('O resultado da equação c = a * b é {}'.format(c))

# Tabelas verdades aplicadas ao Python

a = True
b = True
c = (a or b)
print('O resultado de c é {}'.format(c))

nome_aluno = input('Por favor, insira o nome do aluno: ')
nota_1 = input('Por favor, insira a nota da prova 01: ')
nota_1 = float(nota_1)
nota_2 = input('Por favor, insira a nota da prova 02: ')
nota_2 = float(nota_2)
nota_3 = input('Por favor, insira a nota da prova 03: ')
nota_3 = float(nota_3)
media_nota_aluno = (nota_1 + nota_2 + nota_3)/3
print('A média do aluno: {}, foi igual à: {}'.format(nome_aluno, media_nota_aluno))

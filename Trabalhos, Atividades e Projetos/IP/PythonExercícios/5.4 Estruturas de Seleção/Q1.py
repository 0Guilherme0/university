""" Uma cidade classifica um índice de poluição menor que 35 como
agradável; de 35 até 60 desagradável e acima de 60 perigoso. Escreva
um programa em Python que lê um número real representando o índice
de poluição e imprime a classificação adequada para ele. """

ip = int(input('Digite o índice de poluição na cidade: '))
if ip < 35:
    print('A classificação da cidade é: Agradável')
elif ip >= 35 and ip < 60:
    print('A classificação da cidade é: Desagradável')
elif ip > 60:
    print('A classificação da cidade é: Perigoso')
else:
    print('Índice inválido')
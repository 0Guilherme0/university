""" Depois da liberação do governo para as mensalidades dos planos de
saúde, as pessoas começaram a fazer pesquisas para descobrir um
bom plano não muito caro. Um vendedor de um plano de saúde
apresentou a tabela a seguir:
 Até 10 anos – R$ 30,00
 Acima de 10 até 29 anos – R$ 60,00
 Acima de 29 até 45 anos – R$ 120,00
 Acima de 45 até 59 anos – R$ 150,00
 Acima de 59 até 65 anos – R$ 250,00
 Maior que 65 anos – R$ 400,00
Criar um programa em Python que entre com o nome e a idade de uma
pessoa e imprimir o nome e o valor que ela deverá pagar. """

nome, idade = input('Digite o seu nome: \n'), int(input('e sua Idade: '))
valorpag = None

if idade <=10:
    valorpag = 30.00
elif idade > 10 and idade <= 29:
    valorpag = 60.00
elif idade > 29 and idade <= 45:
    valorpag = 120.00
elif idade > 45 and idade <= 59:
    valorpag = 150.00
elif idade > 59 and idade <= 65:
    valorpag = 250.00
elif idade > 65:
    valorpag = 400.00

print('{0} deverá pagar R${1} '.format(nome,valorpag))
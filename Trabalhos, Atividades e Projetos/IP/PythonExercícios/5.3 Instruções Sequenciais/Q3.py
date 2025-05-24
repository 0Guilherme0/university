name = input('Digite o nome do produto: ')
value = float(input('Digite o valor do produto: R$'))
qt = int(input('Digite a quantidade de produtos vendidos: '))
print('Você vendeu {0} unidades de {1} e arrecadou R${2}.'.format(qt, name, (value*qt)))
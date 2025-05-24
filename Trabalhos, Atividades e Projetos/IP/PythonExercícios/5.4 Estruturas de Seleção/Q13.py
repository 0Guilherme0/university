""" Para realizar o cálculo do Imposto de Renda a ser pago, é solicitado a
renda anual e o número de dependentes do contribuinte. A renda líquida
é calculada sobre a renda anual com um desconto de 2% para cada
dependente do contribuinte. O contribuinte com uma renda líquida de até
R$ 20.000,00 não paga imposto. Para aqueles que possuem renda
líquida entre R$ 20.000,00 e R$ 50.000,00 o imposto é de 5% sobre o
valor da renda líquida; e para rendas líquidas de R$ 50.000,00 até R$
100.000,00 é de 10%. Rendas superiores a R$ 100.000,00 pagam 15%
de imposto. """

rendaanual = float(input('Digite a renda anual anual: '))
dependentes = int(input('Digite a quantidade de dependentes: '))
imposto = 0
desc = 0
while dependentes != 0:
    dependentes -= 1
    desc = desc+0.02

rendaliquida = rendaanual+(rendaanual*desc)

if rendaliquida <= 20000:
    imposto = 0
elif rendaliquida > 20000 and rendaliquida < 50000:
    imposto = 0.05
elif rendaliquida >= 50000 and rendaliquida <= 100000:
    imposto = 0.1
elif rendaliquida > 100000:
    imposto = 0.15
else:
    print('Renda líquida inválida ')

rendaliquida = rendaliquida-(rendaliquida*imposto)

print('A renda líquida após todos os descontos é ',rendaliquida)
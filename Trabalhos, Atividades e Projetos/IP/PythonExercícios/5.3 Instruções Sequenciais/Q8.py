vendas = float(input('Digite o valor total das vendas do mês: '))
comissao = vendas*0.25
sal = 800+comissao
print('O salário do funcionário será de {0} com um valor de {1} referente a sua comissão.'.format(sal, comissao))

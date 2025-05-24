""" Uma loja que trabalha com crediário funciona da seguinte maneira: se o
pagamento ocorre até o dia do vencimento, o cliente ganha 10% de
desconto e é avisado que o pagamento está em dia. Se o pagamento é
realizado até cinco dias após o vencimento, o cliente perde o desconto,
e se o pagamento atrasa mais de cinco dias, é cobrada uma multa de
2% por dia de atraso. Faça um programa em Python que lê o dia do
vencimento, o dia do pagamento e o valor da prestação e calcule o valor
a ser pago pelo cliente, exibindo as devidas mensagens. Obs.: suponha
que todo vencimento ocorre até o dia dez de cada mês e os clientes
nunca deixam para pagar no mês seguinte. """
"""  Vencimento no dia 10 de todo mês 
 Clientes não pagam no mês seguinte a fatura de um mês
 Supondo que os dias de multa se acumulam e são adicionados todos ao valor inicial bruto
 diapag = data de pagamento
 valpag = valor do pagamento
 dm = dias de multa """

diapag = int(input('Digite a data da realização do pagamento (dia, apenas)'))
if diapag < 31:

    valpag = float(input('Digite o valor total pago: '))

    if diapag <= 10:
        desc = valpag*0.1
        print('O pagamento está em dia.\n Você ganhou um desconto de {0} R$'.format(desc))
    elif diapag > 10 and diapag <= 15:
        print('Você realizou o pagamento após o vencimento. Perdeu seu desconto ("_")')
    elif diapag > 15 and diapag < 31:
    
        count = diapag -10
        multa = 0
        
        while count != 0:
            count -= 1
            multa = multa + 0.02 
    
        dm = diapag -10
        multa = multa*valpag
        valpag = valpag+multa
        
        print('Você realizou o pagamento com {0} dias atraso, sua multa foi de R${1} \nO valor total do seu pagamento será de R${2} '.format(dm,multa,valpag))
else:
    print('Quantidade de dias ultrapassa limite mensal')

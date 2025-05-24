""" Escreva uma função chamada calcula_hora_extra para calcular e
retornar o valor que deverá ser pago ao empregado no final do mês em
horas extras. Para fazer esse cálculo, basta dividir o salário mensal do
empregado pelo número de horas trabalhadas (horas trabalhadas no
mês). Multiplique esse valor por 1,5 e terá o valor da hora extra. """

def calcula_hora_extra():
    horas = float(input('Digite a carga horária mensal do funionário: '))
    sal = float(input('Digite o salário contratual que o funcionário recebe: '))
    qhe = float(input('Quantas horas extras foram trabalhadas esse mês? '))
    he = (sal/horas)*1.5
    tothe = qhe*he
    return tothe

print(f'O valor que o funcinário receberá por horas extras é {calcula_hora_extra()}')


""" Crie um programa em Python para calcular o reajuste do salário dos
funcionários de uma empresa. Para tal, crie as funções main,
folha_pagamento e reajuste_funcionario. A função main é responsável
por criar uma estrutura de menu para chamar a função folha_pagamento.
Já a função folha_pagamento é responsável por cadastrar as
informações do funcionário da empresa, ou seja, nome, salário e o
número de filhos de um grupo indeterminado de funcionários. Para
calcular o aumento dos funcionários, a função folha_pagamento usa a
função reajuste_funcionario que tem como entrada o salário e o número
de filhos, a função reajuste_funcionario calcula e exibe o novo salário e
a diferença salarial (o salário antigo subtraído do novo salário)

O cálculo do novo salário é feito de acordo com as seguintes regras: a)

acréscimo do salário baseado na tabela abaixo, e b) adicional do salário-
família, no qual o funcionário recebe R$ 25,00 por filho.

SALÁRIO ATUAL (R$) AUMENTO
0,00 a 500,00 30%
500,01 a 1000,00 20%
Acima de 1000,00 10%

O programa encerra as atividades quando o usuário do sistema digitar um valor
negativo para o salário do funcionário. """

def reajuste_funcionario(salario, filhos):
    if salario > 0 and salario <= 500:
        salario = salario*1.3
    elif salario >= 500.01 and salario <= 1000:
        salario = salario*1.2
    elif salario > 1000:
        salario = salario*1.1

    if filhos > 0:
        salario += 25*filhos

    return salario
    
def folha_pagamento():
    while True:
        salario = float(input('Digite o salário atual do funcionário: '))
        if salario < 0:
            break

        nome = input('Digite o nome do funcionário: ')
        filhos = int(input(f'Digite a quantidade de filhos de {nome}: '))
        reajuste = reajuste_funcionario(salario,filhos)
        diferenca_sal = reajuste-salario

        print(f'{nome}, teve seu salário alterado de R${salario} para R${reajuste}.\n A diferença salarial foi de R${diferenca_sal}')
        print('----------------------------------------------------------------------')

def main():
    print('---------------------------------------------------------------------')
    input('Precione enter para começar a calcular os reajustes dos funcionários.')
    print('---------------------------------------------------------------------')
    folha_pagamento()

main()
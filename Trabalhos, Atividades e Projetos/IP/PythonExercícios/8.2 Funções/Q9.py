""" Crie a função REAJUSTE, que vai ter como entrada o salário atual e vai
retornar o novo salário reajustado, de acordo com as seguintes regras:

SALÁRIO ATUAL (R$) AUMENTO
0,00 a 500,00 30%
500,01 a 1000,00 20%
Acima de 1000,00 10%

A seguir, construa um programa que tenha como entrada o salário de um grupo
indeterminado de pessoas e use a função REAJUSTE para exibir o novo salário
e a diferença salarial (o salário antigo subtraído do novo salário). O programa
encerra as atividades quando um salário negativo for inserido """

def reajuste(sal):
    if sal > 0 and sal <= 500:
        sal = sal*1.3
    elif sal >= 500.01 and sal <= 1000:
        sal = sal*1.2
    elif sal > 1000:
        sal = sal*1.1
    else:
        return 'salário nulo' 
    return sal

def main():
    while True:
        salario = float(input('Digite o salário do funcionário: '))
    
        if salario < 0:
            break

        reaj = reajuste(salario)
        
        if reaj == 'salário nulo':
            print('O sálario é 0')

        difsal = reaj - salario
        
        print(f'O novo reajuste é R${reaj}, e a diferença salárial foi de R${difsal}')

main()








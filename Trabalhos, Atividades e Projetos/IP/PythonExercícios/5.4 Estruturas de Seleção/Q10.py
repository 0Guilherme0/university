""" 10. A empresa Serra CIA decidiu conceder um aumento de salários a seus
funcionários de acordo com a tabela abaixo:

Escrever um programa em Python que lê, para cada funcionário, o seu nome e
o seu salário atual. Após receber estes dados, o programa calcula o novo
salário e escreve na tela as seguintes informações: 
<nome do funcionário> <% de aumento> <salário atual> <novo
salário>"""

nome = input('Digite o nome do funcionário: ')
sal = float(input('Digite o salário atual do funcionário: '))
percent = None
newsal = None
if sal > 0 and sal <= 400:
    newsal = sal+(sal*0.15)
    percent = 15
elif sal > 400 and sal <= 700:
    newsal = sal+(sal*0.12)
    percent = 12
elif sal > 700 and sal <= 1000:
    newsal = sal+(sal*0.1)
    percent = 10
elif sal > 1000 and sal <= 1800:
    newsal = sal+(sal*0.07)
    percent = 7
elif sal > 1800 and sal <= 2500:
    newsal = sal+(sal*0.04)
    percent = 4
else:
    newsal = sal
    percent = 0
print('O salário de {0} teve um almento de {1}%, seu saláriio atual é de R${2} e o seu novo salário será R${3}'.format(nome,percent,sal,newsal))
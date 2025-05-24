mes = int(input('Digite o mês do ano em valor numérico: 1 - 12 '))
match (mes):
    case 1:
        mes = 'janeiro'
    case 2:
        mes = 'fevereiro'
    case 3:
        mes = 'março'
    case 4:
        mes = 'abril'
    case 5:
        mes = 'maio'
    case 6:
        mes = 'junho'
    case 7:
        mes = 'julho'
    case 8:
        mes = 'agosto'
    case 9:
        mes = 'setembro'
    case 10:
        mes = 'outubro'
    case 11:
        mes = 'novembro'
    case 12:
        mes =  'desembro'
    case _:
        print('Mês não existe.')
print('Estamos no mês de {0}.'.format(mes))
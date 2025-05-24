def menu():
    print('[1] - Questão 1')
    print('[2] - Questão 2')
    print('[3] - Sair')
    opcao = int(input('Digite a opção desejada: '))
    return opcao

def consoante(letra):
    letra = letra.lower()
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        return False
    else:
        return True
    
def questao01():
    while True:

        letra = input('Digite uma letra: ')
        if consoante(letra):
            print('A letra é uma consoante')
        else:
            print('A letra é uma vogal')

        again = int(input('Quer testar outra letra? [1] - Sim, [2] - Não'))
        
        if again == 1:
            continue
        else:
            break

def prestacao01(gasto):
    gasto = gasto * 0.9
    return gasto

def prestacao02(gasto):
    return gasto/2

def prestacao03(gasto, parcelas):
    prest = gasto + (parcelas * (gasto * 0.03))
    return prest

def questao02():
    totGasto = float(input('Digite o total gasto na loja: '))
    print('[1] - Pagamento à vista (10 por cento de desconto)')
    print('[2] - Dividido em duas vezes (valor da etiqueta)')
    print('[3] - Dividido de 3 até 10 vezes com três por cento de juros ao mês')
    opPagamento = int(input('Sua opção de pagamento: '))

    if opPagamento == 3:
        parcelas = int(input('Digite a quantidade de parcelas que deseja pagar (3 - 10): '))

        if parcelas > 10 or parcelas < 3:
            print('Quantidade de parcelas inválidas')
        else:
            total = prestacao03(totGasto, parcelas)
            valparcelas = total / parcelas
            print(f'Cada parcela será de R${valparcelas}, são {parcelas} parcelas.\n O valor total será R${total}')

    elif opPagamento == 2:
        valparcelas = prestacao02(totGasto)
        print(f'Cada parcela será de R${valparcelas}, são 2 parcelas.')

    elif opPagamento == 1:
        print(f'Seu pagamento será R${prestacao01(totGasto)} com 10% de desconto!')

    else:
        print('Opção inválida')
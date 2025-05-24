""" Crie uma calculadora simples com funções para realizar operações
básicas (soma, subtração, multiplicação, divisão). Peça ao usuário que
escolha a operação desejada e forneça os números para realizar o
cálculo. """

def questao5():
    def calculadora():
        while True:
            op = int(input('Digite a operação desejada\n [1] - SOMA \n [2] - SUBTRAÇÃO \n [3] - MULTIPLICAÇÃO \n [4] - DIVISÃO:\n'))
            if op < 1 or op > 4:
                print('Opção inválida')
                continue
            
            n1 = float(input('Digite o primeiro número a ser operado: '))
            n2 = float(input('Digite o segundo número a ser operado: '))

            if op == 1:
                return n1 + n2
            elif op == 2:
                return n1 - n2
            elif op == 3:
                return n1 * n2
            else:
                return n1 / n2
            
    print(calculadora())
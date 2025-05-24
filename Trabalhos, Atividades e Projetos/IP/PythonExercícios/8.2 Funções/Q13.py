from Q2 import questao2
from Q3 import questao3
from Q4 import questao4
from Q5 import questao5
from Q7 import questao7

def menu():
    while True:
        print("Qual questão quer rodar?")
        print('Questão [2]')
        print('Questão [3]')
        print('Questão [4]')
        print('Questão [5]')
        print('Questão [7]')
        print('Sair [0]')
        opcao = int(input('Digite sua escolha: '))

        match opcao:
            case 2:
                questao2()
            case 3:
                questao3()
            case 4: 
                questao4()
            case 5:
                questao5
            case 7:
                questao7()
            case 0: 
                break
            case _:
                print('Você não digitou um numero válido...')
menu()
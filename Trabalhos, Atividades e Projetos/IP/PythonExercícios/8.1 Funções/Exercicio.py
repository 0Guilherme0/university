from Funções import *

def main():

    while True:
        op = menu()
        if op == 1:
            questao01()
        elif op == 2:
            questao02()
        elif op == 3: 
            break
        else:
            print('Opção inválida')
    

main()    

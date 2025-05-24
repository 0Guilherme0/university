from ControlerQ1_5 import *

def main():
    while True:
        choose = menu()
        if choose == 1:
            add_expense()
        
        elif choose == 2:
            view_expenses(True,'Lista de Despesas')

        elif choose == 3:
            edit_info()
        
        elif choose == 4:
            delete_expense()
        
        elif choose == 5:
            print('Aplicação finalizada! ')

        else:
            continue

main()


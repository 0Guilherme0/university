from ControlerQ1_3 import *

def main():
    while True:
        choice = menu()

        if choice == 1:
            add_task()

        elif choice == 2: 
            show_todolist('Lista de Tarefas', True, None)

        elif choice == 3:
            mark_as_completed()
        
        elif choice == 4:
            delete_task()

        elif choice == 5:
            print('Aplicação Finalizada!')
            break
main()

from funcoes_monitoramento import *

def main():
    while True:
        choice = menu()
        if choice == 1:
            add_aluno() 
        elif choice == 2:
            show_info()
        elif choice == 3:
            update_info() 
        elif choice == 4:
            delet_aluno()
        elif choice == 5:
            while True:
                end = enter_training()
                if end == 6:
                    break       

        elif choice == 6:
            write_data()
            print(f"{'-'*130}")
            print('Até a proxima. . .')
            break
main()
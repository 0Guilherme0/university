from Funcoes_Lista_Telefonica import *



def main():
    while True:
        choise = menu()
        if choise == 1:
            add_contact()
        
        elif choise == 2:
            delet_contact()

        elif choise == 3:
            update_contact()

        elif choise == 4: 
            search_contact()

        elif choise == 5:
            show_contacts()
            
        elif choise == 6:
            print('Aplicação Finalizada')
            break
        
main()
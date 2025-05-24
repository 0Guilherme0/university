""" Agenda de Contatos: Implemente uma agenda de contatos que permita
adicionar, visualizar, editar e excluir contatos.
Base de dados da Agenda

Nome Telefone E-mail Endereço """

from ControlerQ2_1 import *

def main():
    while True:
        choice = menu()

        if choice == 0:
            print('Opção inválida tente novamente. . .')
            continue
        
        elif choice == 1:
            add_contact()
        
        elif choice == 2:
            view_contacts()

        elif choice == 3: 
            edit_contact()
        
        elif choice == 4: 
            delete_contact()
            
        elif choice == 5:
            break

main()
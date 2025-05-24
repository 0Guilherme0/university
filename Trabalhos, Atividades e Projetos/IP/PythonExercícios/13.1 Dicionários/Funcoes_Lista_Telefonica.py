# inclusão, exclusão, alteração, pesquisa e listagem.

lista_telefonica = {}

def menu():
    while True:
        print(f"{'-'*130}")
        print('O que deseja fazer? ')
        opcoes = ['Incluir Contato','Excluir Contato', 'Alterar Contato',
                'Pesquisar Contato', 'Listar Todos os Contatos','Sair']
        
        for i, opcao in enumerate(opcoes,1):
            print(f'[{i}] - {opcao}')
        
        choice = input('Digite a opção que deseja: ')   
        
        if choice.isdigit() and int(choice) <= len(opcoes):
            return int(choice)
        
        else:
            print('Opção inválida, tente novamente...')
            continue
        
def add_contact(): #1
    print(f"{'-'*130}")
    nome = input('Digite o nome do contato: ')
    
    while True:

        number = input('Digite o número do contato: ')
        number = number.replace(' ','') 

        if number.isdigit() and int(number) != TypeError:
            contact = {'nome': nome, 'numero': number}
            lista_telefonica[nome] = contact
            return contact
        
        else:
            print('Numero inválido, tente: (00 0000 0000)')
            continue

def show_contacts(title = 'Lista de Contatos',showall = True, given_contact = None): #5
    if len(lista_telefonica) > 0:
        print(f"{'-'*130}")
        print(f'{title:^130}')
        print(f"{'-'*130}")
        print(f"{'Nome:':<85}{'Número:':<45}\n")

        if showall:
            for contact in lista_telefonica.values():
                print(f"{contact.get('nome'):<85}{contact.get('numero'):<45}")
        
        else:
            if given_contact != None:
                print(f"{given_contact.get('nome'):<85}{given_contact.get('numero'):<85}")
            
    else:
        print(f"{'-'*130}")
        print('Não há contatos cadastrados...') 

def delet_contact(): #2
    print(f"{'-'*130}")
    if len(lista_telefonica) > 0:
        search = input('Digite o nome do contato para EXCLUI-LO: ')
       
        if search in lista_telefonica:
            for contact in lista_telefonica.values():
                if contact.get('nome') == search: 
                    deleted_contact = lista_telefonica.pop(search)
                    show_contacts('Contato Deletado', False, deleted_contact)

                    return

        else:
            print('O nome não tem um contato correspondente: ')      

    else:
        print('Não há contatos cadastrados...')

def update_contact(): #3
    print(f"{'-'*130}")
    if len(lista_telefonica) > 0:
        search = input('Digite o nome do contato para ALTERA-LO: ')

        if search in lista_telefonica:
            for contact in lista_telefonica.values():
                if contact.get('nome') == search:
                    print('O que deseja alterar? ')
                    print('[1] - Nome \n[2] - Número \n[3] - Alterar tudo')
                    choise = input('Digite a opção escolhida: ')
                    
                    if choise.isdigit() and int(choise) == 1 or choise.lower() == 'nome':
                        nome = input('Digite o novo nome do contato: ')
                        lista_telefonica[search]['nome'] = nome
                        lista_telefonica[search] = nome
                        show_contacts('Contato Alterado', False, lista_telefonica[search])
                        return

                    elif choise.isdigit() and int(choise) == 2 or choise.lower() == 'número' or choise.lower() == 'numero':
                        numero = input('Digite o novo número do contato: ')

                        if numero.isdigit() and int(numero) != TypeError:
                            lista_telefonica[search]['numero'] = int(numero.replace(' ',''))
                            show_contacts('Contato Alterado', False, lista_telefonica[search])
                            return
                    
                    elif choise.isdigit() and int(choise) == 3:
                        contato_alterado = add_contact()
                        show_contacts('Contato Alterado', False, contato_alterado)
                        return

                    else: 
                        print('Opção inválida')
                        continue
        
        else: 
            print('Contato não encontrado...')

    else: 
        print('Não há contatos cadastrados...')

def search_contact(): #4
    print(f"{'-'*130}")
    if len(lista_telefonica) > 0:
        search = input('Digite o nome do contato para PESQUISAR: ')

        if search in lista_telefonica:
            for contact in lista_telefonica.values():
                if contact.get('nome') == search:
                    show_contacts('Contato Pesquisado',False, contact)

        else: 
            print('Nome não encontrado ou não digitado...')
    
    else: 
        print('Não há contatos na lista...')

base_contacts = {}

def menu():
    print(f"{'-'*130}")
    print('O que deseja fazer?')
    options = ['Adicionar Contato','Visualizar Contatos','Editar Contato','Excluir Contato','Sari da Aplicação']

    for i, option in enumerate(options,1):
        print(f'[{i}] - {option}')
    
    choice = input('Digite a opção desejada: ')

    if choice.isdigit() and int(choice) <= len(options):
        return int(choice)
    
    else: 
        return 0
    
def add_contact():
    print(f"{'-'*130}")
    nome = input('Digite o nome do contato: ')
    email = input('Digite o email do contato: ')
    address = input('Digite o endereço do contato: ')
    
    while True:

        tel = input('Digite o número de telefone do contato: ')
        tel = tel.replace(' ','')

        if tel.isdigit() and int(tel) != TypeError:
            contact = {'nome':nome,'telefone':tel,'email':email,'endereço':address}
            base_contacts[nome] = contact
            return contact
        
        else: 
            print('Número digitado inválido')
    

def view_contacts(title = 'Lista de Contatos', showall = True, givencontact = None):
    if len(base_contacts) > 0: 
        print(f"{'-'*130}")
        print(f'{title:^130}')
        print(f"{'-'*130}")
        print(f"{'Nome:':<40}{'Telefone:':<15}{'Email:':<35}{'Endereço:':<40}\n")

        if showall:
            for contact in base_contacts.values():
                print(f"{contact['nome']:<40}{contact['telefone']:<15}{contact['email']:<35}{contact['endereço']:<40}")
            
        elif givencontact != None:
            print(f"{givencontact['nome']:<40}{givencontact['telefone']:<15}{givencontact['email']:<35}{givencontact['endereço']:<40}")
            
    else:
        print('Não há elementos na lista de contatos. . .')

def edit_contact():
    print(f"{'-'*130}")
    if len(base_contacts) > 0:
        search = input('Digite o nomme do contato para EDITA-LO: ')

        if search in base_contacts:
            for contact in base_contacts.values():
                if contact['nome'] == search:
                    opcoes = ['Nome','Número de Telefone','Email','Endereço','Tudo']
                    keyoptions = ['nome','telefone','email','endereço']
                    
                    while True:
                        for i, opcao in enumerate(opcoes,1):
                            print(f'[{i}] - {opcao}')
                
                        choice = input('Digite a opção desejada: ')

                        if choice.isdigit() and int(choice) <= len(opcoes) and int(choice) != 5:
                            
                            while True:
                                update = input(f'Digite a atualização do {opcoes[int(choice)-1]}: ')
                            
                                if int(choice) == 2:
                                    update = update.replace(' ','')
                                    if update != TypeError:
                                        base_contacts[search]['telefone'] = update
                                        view_contacts('Contato Atualizado', False, base_contacts[search])
                                        return
                                        
                                    else:
                                        print('Número inválido, tente novamente. . .')
                                        continue
                                else:
                                    break

                            if int(choice) == 5:
                                delete_contact(search)
                                edited_contact = add_contact()
                                view_contacts('Contato Editado', False, edited_contact)
                                return
                            
                            elif int(choice) == 1:
                                base_contacts[update] = base_contacts[search]
                                base_contacts[update][keyoptions[int(choice)-1]] = update
                                view_contacts('Contato Alterado', False, base_contacts[search])
                                return

                            else:
                                base_contacts[search][keyoptions[int(choice)-1]] = update
                                view_contacts('Contato Alterado', False, base_contacts[search])
                                return

                        else: 
                            print('Opção inválida, tente novamente. . .')
                            break
        
        else:
            print('Contato não existente. . .')

    else:
        print('Não há elementos na lista de contatos. . .')
    
def delete_contact(search = None, view = False):
    print(f"{'-'*130}")

    if len(base_contacts) > 0:
        if search == None:
            search = input('Digite o nomme do contato para DELETA-LO: ')

            if search in base_contacts:
                for contact in base_contacts.values():
                    if contact['nome'] == search:
                        view_contacts('Contato Deletado', False, base_contacts[search])
                        del base_contacts[search]
                        return

        else:
            if search in base_contacts:
                for contact in base_contacts.values():
                    if contact['nome'] == search:
                        if view:
                            view_contacts('Contato Deletado', False, base_contacts[search])

                        del base_contacts[search]
                        return
            
            else: 
                print('Contato não existe. . . ')
    
    else:
        print('Não há elementos na lista de contatos. . .')
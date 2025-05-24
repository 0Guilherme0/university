# Funções da primeira questão da lista de exercícios 12.1 (listas)

# base de contatos
base_contacts = [['Gui',87988194847, 'guilherme@mail.com', 'Rua da Fazendinha, 311']]

def menu():
    print('[1] - ADICIONAR um novo contato')
    print('[2] - VISUALIZAR contato ')
    print('[3] - EDITAR contato')
    print('[4] - EXCLUIR contato ')
    
    choise = int(input('Digite a opção desejada: '))
    return choise

def add_contact():
    print("{0:^100}".format("-" * 100))
    nome = input('Digite o nome do novo contato: ')
    tel = int(input('Digite o número do contato: '))
    email = input('Digite o e-mail do contato: ')
    aderess = (input('Digite o endereço do contato:'))
    print("{0:^100}".format("-" * 100))


    contact = [nome, tel, email, aderess]
    base_contacts.append(contact)

def view_contacts():
    tamanho = len(base_contacts)
    if tamanho > 0:
        print("{0:^130}".format("-" * 130))
        print('{0:^130}'.format('Contatos Cadastrados'))
        print("{0:^130}".format("-" * 130))
        print('{0:<30}{1:<14}{2:<30}{3:<40}'.format('Nome', 'Telefone', 'E-mail', 'Endereço'))

        for contact in base_contacts:
            print('\n{0:<30}{1:<14}{2:<30}{3:<40}'.format(contact[0], contact[1], contact[2], contact[3]))
        print("{0:^130}".format("-" * 130))
    else:
        print('Não há contatos na lista')

def print_contact(title,contact):
    print('{0:^130}'.format('-'*130))
    print('{0:^130}'.format(title))
    print('{0:^130}'.format('-'*130))
    print('{0:<30}{1:<14}{2:<30}{3:<40}'.format('Nome', 'Telefone', 'E-mail', 'Endereço\n'))
    print('{0:<30}{1:<14}{2:<30}{3:<40}'.format(contact[0], contact[1], contact[2], contact[3]))
    print('{0:^130}'.format('-'*130))

def edit_contact():
    if len(base_contacts) > 0:
        search = int(input('Digite o número para pesquisar o contato: '))
        
        for i, contact in enumerate(base_contacts):
            if contact[1] == search:
                print('O que quer editar?')
                print('[1] - Nome \n[2] - Telefone \n[3] - E-mail \n[4] - Endereço \n[5] - Todos')
                op = int(input('Digite a opção desejada: '))

                if op == 1:
                    base_contacts[i][0] = input('Digite o novo nome do contato: ')
                    print('Nome editado com sucesso!')
                    altered_contact = base_contacts[i]
                elif op == 2: 
                    base_contacts[i][1] = int(input('Digite o novo número do contato: '))
                    print('Telefone editado com sucesso!')
                    altered_contact = base_contacts[i]
                elif op == 3:
                    base_contacts[i][2] = input('Digite o novo e-mail do contato: ')
                    print('E-mail alterado com sucesso!')
                    altered_contact = base_contacts[i]
                elif op == 4:
                    base_contacts[i][3] = input('Digite o novo endereço do contato: ')
                    print('Endereço alterado com sucesso!')
                    altered_contact = base_contacts[i]
                elif op == 5:
                    add_contact()
                    altered_contact = base_contacts.pop(i)
                else:
                    print('Opção inválida!')
                    break

                print_contact('Contato Alterado', altered_contact)
                return
        else:
            print('Contato não existe!')
    else:
        print('Lista não possui contatos cadastrados! ')


def delet_contact():
    if len(base_contacts) > 0:
        search = int(input('Digite o número para DELETAR o contato: '))
        for i, contact in enumerate(base_contacts):
            if contact[0] == search:
                deleted_contact = base_contacts.pop(i)
                print_contact('Contato Deletado', deleted_contact)
                break
            else:
                print('Contato não existente!')
    else:
        print('Lista de Contatos vazia!')

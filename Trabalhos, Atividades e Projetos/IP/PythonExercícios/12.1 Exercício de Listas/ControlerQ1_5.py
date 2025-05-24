base_despesas = []

def menu():
    print(f"{'-'*130:^130}")    
    opcoes = ['Adicionar despesa','Visualizar Resumo','Edtar informações','Deletar despesa','Sair da aplicação']
    print('Qual ação deseja fazer no gerenciamento de despesas?')
    for i, opcao in enumerate(opcoes,1):
        print(f'[{i}] - {opcao}')
    
    op = input('Digite a opção desejada: ')

    if op.isdigit() and int(op) <= len(opcoes):
        return int(op)
    else:
        print('Opção inválida, tente novamente. . . ')
        return
    
def add_expense():
    print(f"{'-'*130:^130}")    
    desc_expense = input('Digite a descriação da despesa: ')
    value = float(input('Digite o valor da despesa: '))
    date = input('Digite a data da despesa: ')
    obs = input('Digite uma observação (opcional): ')
    despesa = [desc_expense,value,date,obs]
    base_despesas.append(despesa)
    return despesa
    
def view_expenses(showall, title, given_expense = None):
    print(f"{'-'*130:^130}")    
    
    if len(base_despesas) > 0:
        print(f"{title:^130}")
        print(f"{'-'*130:^130}")    
        print(f"{'Descrição:':<55}{'Valor:':<15}{'Data da Despesa:':<20}{'Observação:':<40}\n")

        if showall:
            for despesa in base_despesas:
                print(f"{despesa[0]:<55}{despesa[1]:<15}{despesa[2]:<20}{despesa[3]:<40}")
        else:
            if given_expense is not None:
                print(f"{given_expense[0]:<55}{given_expense[1]:<15}{given_expense[2]:<20}{given_expense[3]:<40}")

    else:
        print('Não há elementos na lista. . .')

def edit_info():
    print(f"{'-'*130:^130}")    

    if len(base_despesas) > 0:
        search = float(input('Digite o valor da despesa: '))
        for i, despesa in enumerate(base_despesas):
            
            if search == despesa[1]:
                print('Opções de alteração: ')
                opcoes = ['Descrição', 'Valor','Data da despesa','Observação','TUDO']                
                
                for numb, opcao in enumerate(opcoes,1):
                    print(f'[{numb}] - {opcao}')

                op = input('Digite a opção desejada')
                
                if op.isdigit() and int(op) <= len(opcoes):
                    for numb, opcao in enumerate(opcoes,1):
                        if int(op) == numb:
                            if int(op) == 5:
                                despesa = add_expense()
                                del base_despesas[i]
                                break

                            else:
                                edited_info = input(f'Digite o(a) {opcao} editado(a): ')
                                
                                if int(op) == 2:
                                    base_despesas[i][numb-1] = float(edited_info)
                                else:
                                    base_despesas[i][numb-1] = edited_info
                            break

                            view_expenses(False,'Despesa Editada',despesa)
                else: 
                    print('Opção inválida, Tente novamente. . .')
                    return  
    else: 
        print('Não há despesas para semrem alteradas. . .')

def delete_expense():
    if len(base_despesas) > 0:
        search = input('Digite o valor da despesa para Deleta-la: ')
        
        for i, despesa in enumerate(base_despesas):
            if search.isdigit() and float(search) == despesa[1]:
                view_expenses(False,'A ser apagada...', despesa)
                sure = input('Quer mesmo apagar os dados dessa despesa?? \n[1] - Sim \n[2] - Não\n   ')

                if sure == 1: 
                    deleted_expense = base_despesas.pop(i)

                else:
                    print('\nDespesa não deletada. . .')
                    return
                
                view_expenses(False,'Despesa Deletada',deleted_expense )
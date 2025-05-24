from datetime import datetime

todo_list = []

def menu():
    print('{0:130}'.format('-'*130))
    print('O que quer fazer na sua lista de a fazeres?')
    print('[1] - Adicionar uma nova tarefa')
    print('[2] - Visualizar sua lista de tarefas')
    print('[3] - Marcar tarefa como concluida')
    print('[4] - Deletar tarefa da lista')
    print('[5] - Finalizar lista')
    op = int(input('Digite a opção desejada: ')) 
    return op

def add_task():
    print('{0:^130}'.format('-'*130))
    todo_desc = input('Dê uma breve descrição da tarefa: ')
    creation_date = datetime.now()
    creation_date = creation_date.strftime('%d/%m/%Y')
    priority_options = ['Alta', 'Media', 'Baixa']
    print('\nOpções de prioridade: ')
    for i, options in enumerate(priority_options,1):
        print(f'[{i}] - {options}')
    
    op = int(input('Digite a opção de prioridade para a tarefa: '))
    if op <= len(priority_options):
        completed_task_date = int(input('\nAdicionar tarefa já concluida? \n[1]-SIM \n[2]-NÃO\n'))
        
        if completed_task_date == 1:
            completed_task_date = datetime.now()
            completed_task_date = completed_task_date.strftime('%d/%m/%Y')
        else:
            completed_task_date = 'A concluir'

    priority = None
    if op == 1:
        priority = 'Alta'
    elif op == 2:
        priority = 'Media'
    elif op == 3:
        priority = 'Baixa'
            
    task =  [todo_desc, creation_date, completed_task_date, priority]
    todo_list.append(task)

def show_todolist(title,all_list,i):
    if len(todo_list) > 0:
        print('{0:^130}'.format('-'*130))
        print('{0:^130}'.format(title))
        print('{0:^130}'.format('-'*130))
        print('{0:<70}{1:<20}{2:<20}{3:<20}'.format('Descrição:','Data de Criação','Data de conclusão', 'Prioridade'))
        print('{0:^130}'.format('-'*130))

        if all_list:
            for task in todo_list:
                print('\n{0:<70}{1:<20}{2:<20}{3:<20}'.format(task[0],task[1],task[2],task[3]))
        else:
            for task in todo_list:
                if task == todo_list[i]:
                    print('\n{0:<70}{1:<20}{2:<20}{3:<20}'.format(task[0],task[1],task[2],task[3]))
                    break
                
    else: 
        print('{0:^130}'.format('-'*130))
        print('Não há tarefas na lista. . .')

def mark_as_completed():
    if len(todo_list) > 0:
        search = input('Digite a descrição da tarefa para marcar como concluida: ')
        
        for i, task in enumerate(todo_list):
            if search == task[0]:
                input('Press enter to continue...')
                taskcompleted = datetime.now()
                taskcompleted = taskcompleted.strftime('%d/%m/%Y')
                todo_list[i][2] = taskcompleted
                show_todolist('Tarefa Concluida', False, i)
                return
            
            else:
                print('Tarefa não encontrada. . .')
    
    else: 
        print('Não há tarefas na lista. . .')

def delete_task():
    if len(todo_list) > 0:
        search = input('Digite a descrição para deletar a tarefa: ')
        for i, task in enumerate(todo_list):
            if search == task[0]:
                sure = input('\nQuer realmente deletar a tarefa? \n[1]-Sim \n[2]-Não\n     ')
                if sure == 1:
                    deleted_task = todo_list.pop(i)
                    show_todolist('Tarefa Apagada', False, None)
                    return
                elif sure == 2:
                    break
                else:
                    print('\nOpção inválida')
                    break
            
            else:
                print('Tarefa não encontrada. . .')
    else:
        print('Não há tarefas na lista. . .')
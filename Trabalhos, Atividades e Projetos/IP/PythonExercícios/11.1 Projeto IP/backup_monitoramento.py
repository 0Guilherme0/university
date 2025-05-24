import json
import os

cadastro_alunos = {}
data_file = 'cadastro_alunos.json'

def write_data():
    with open(data_file, 'w') as arquivojson:
        json.dump(cadastro_alunos, arquivojson, indent=4)

def load_data():
    if not os.path.exists(data_file):
        with open(data_file, 'w') as arquivojson:
            global cadastro_alunos
            json.dump(cadastro_alunos, arquivojson, indent=4)
    with open(data_file, 'r') as arquivojson:
        cadastro_alunos = json.load(arquivojson)
        

def menu(nome:str=None, treino:bool=False):
    print(f"{'-'*130}")
    while True:
        if not treino:
            print('O que deseja fazer no Monitoramento de Exercícios? \n')
            options = ['Adicionar Aluno','Visualizar Alunos Cadastrados','Atualizar Cadastro','Deletar aluno',
                    'Entrar na Lista de Treino de um Aluno','Sair da Aplicação\n']
        else:
            print(f'O que deseja fazer na ficha de treino de {nome}')
            options = ['Adicionar Exercício', 'Visualizar Ficha de Treino', 'Atualizar informações','Remover Exercícios',
                       'Voltar Para o cadastro de Alunos\n' ]
            
        for i, option in enumerate(options,1):
            print(f"[{i}] - {option}")

        choice = input('Digite a opção desejada: ')
        if choice.isdigit() and int(choice) <= len(options):
            return int(choice)

def add_aluno(returnmat: bool=False):
    load_data()
    print(f"\n{'-'*130}")
    nome = input('Digite o nome do aluno: ')
    while True:
        mat = input('Digite a matricula (5 digitos) do aluno: ')
        mat = mat.replace(' ', '')  
        if len(mat) == 5 and mat.isdigit() and int(mat) != TypeError:  
            if mat in cadastro_alunos:
                print('Matricula já existe, tente novamente...')
                continue
            break

    idade = input('Digite a idade do aluno: ')
    if idade.isdigit() and int(idade) is not TypeError:
        idade = int(idade)

    instituicao = input('Digite o nome do local de treino: ')
    treino = {}
    aluno = {'nome': nome, 'mat': mat, 'idade': idade, 'instituicao': instituicao, 'treino': treino}
    cadastro_alunos[mat] = aluno
    write_data()
    if returnmat:
        return mat
    else:
        return aluno

def show_info(title:str='Alunos Cadastrados', showall:bool=True, alunomat:str=None, treino:bool=False, exercise:str=None): 
        load_data()   
        if len(cadastro_alunos) > 0:
            print(f"\n{'-'*130}")
            print(f"{title:^130}")
            print(f"{'-'*130}")

            if not treino:
                print(f"{'Nome':<55}{'Matricula':<15}{'Idade':<10}{'Instituição':<50}\n")
                if showall:
                    for aluno in cadastro_alunos.values():
                        print(f"{aluno['nome']:<55}{aluno['mat']:<15}{aluno['idade']:<10}{aluno['instituicao']:<50}")
                
                elif alunomat is not None:
                    aluno = cadastro_alunos[alunomat]
                    if aluno:
                        print(f"{aluno['nome']:<55}{aluno['mat']:<15}{aluno['idade']:<10}{aluno['instituicao']:<50}")
            else:
                aluno = cadastro_alunos.get(alunomat)
                if aluno and 'treino' in aluno and len(aluno['treino']) > 0:
                    print(f"{'Exercicio':<44}{'Séries':<43}{'Repetições':43}\n")
                    if showall:
                        for exercicio in aluno['treino'].values():
                            print(f"{exercicio['nomeex']:<44}{exercicio['series']:<43}{exercicio['reps']:<43}")

                    elif exercise is not None and exercise in aluno['treino']:
                        exercicio = aluno['treino'][exercise]
                        print(f"{exercicio['nomeex']:<44}{exercicio['series']:<43}{exercicio['reps']:<43}")
                    else:
                        print('Exercício não encontrado.')       
                else:
                    print('Não há exercícios cadastrados para este aluno.')
        else: 
            print(f"\n{'-'*130}")
            print('Não há nada para ver aqui...')

def update_info():
    load_data()
    print(f"\n{'-'*130}")
    if len(cadastro_alunos) > 0:
        search = input('Digite a matricula do aluno para ALTERAR SEUS DADOS: \n')

        if search.isdigit() and search in cadastro_alunos:
            print(f"{'-'*130}")
            options = ['Nome','Matricula','Idade','Instituição','TUDO\n']
            keys = ['nome','matricula','idade','instituicao']
            print('O que deseja alterar?\n')
            for i, op in enumerate(options,1):
                print(f'[{i}] - {op}') 

            choice = input('Digite a opção desejada: ')
            if choice.isdigit() and int(choice) is not TypeError and int(choice) <= len(options):
                choice = int(choice)
                if choice == 5:
                    del cadastro_alunos[search]
                    added_aluno_mat = add_aluno(returnmat=True)
                    show_info('Aluno Alterado', False, added_aluno_mat)
                else:
                    update = input(f'Digite o(a) {options[choice-1]} atualizado(a): ')
                    if choice == 2:
                        cadastro_alunos[update] = cadastro_alunos[search]
                        cadastro_alunos[update]['mat'] = int(update)
                        del cadastro_alunos[search]
                        write_data()
                        show_info('Aluno Alterado', False, update)
                        return
                    elif choice == 3:
                        cadastro_alunos[search]['idade'] = int(update)
                        write_data()
                    else:
                        cadastro_alunos[search][keys[choice-1]] = update
                        write_data()
                    print('Aluno Alterado:')
                    show_info('Aluno Alterado', False, search)
            else:
                print('Opção inválida! Tente novamente. . .')
        else:
            print('Matricula não encontrada. . .')
    else:
        print('Não há alunos cadastrados no monitoramento. . .')
    
def delet_aluno():
    load_data()
    print(f"\n{'-'*130}")
    if len(cadastro_alunos) > 0:
        while True:
            search = input('Digite a matricula do aluno para DELETA-LO: ')
            if int(search) != TypeError:
                if search in cadastro_alunos:
                    for aluno in cadastro_alunos.values():
                        if int(search) == aluno['mat']:
                            show_info('Aluno Deletado', False, search)
                            del cadastro_alunos[search]
                            write_data()
                            return
                else:
                    print('Matricula não encontrada. . .')
                    return
            else:
                print('Matricula incorreta, tente novamente...')
    else:
        print('Não há alunos cadastrados')

def add_exercise(search:str):
    load_data()
    print(f"\n{'-'*130}")
    print('Preencha os dados do exercício: ')
    while True:
        nomeex = input('Digite o nome do Exercício: ')
        if nomeex in cadastro_alunos[search]['treino']:
            print('Exercício já está na ficha... Tente outro nome. ')
            continue
        break
    
    while True:
        series = input('Digite o número de séries: ')
        if series.isdigit() and int(series) > 0:
            series = int(series)
            break
        else:
            print('Número inválido de séries. Deve ser um número inteiro positivo.')

    while True:
        reps = input('Digite a quantidade de repetições: ')
        if reps.isdigit() and int(reps) > 0:
            reps = int(reps)
            break
        else:
            print('Número de repetições inválido. Deve ser um número positivo.')

    exercise = {'nomeex': nomeex, 'series': series, 'reps': reps}
    cadastro_alunos[search]['treino'][nomeex] = exercise
    print('Exercício cadastrado')
    write_data()
    return cadastro_alunos[search]['treino'][nomeex]

def update_training_info(search:str):
    load_data()
    print(f"\n{'-'*130}")
    if len(cadastro_alunos[search]['treino']) > 0:
        nomeex = input('Qual o nome do exercício que deseja alterar? ')
        if nomeex in cadastro_alunos[search]['treino']:
            print(f"{'-'*130}")
            print('O que deseja alterar no exercício? ')
            options = ['Nome do Exercício','Número de séries', 'Quantidade de Repetições', 'Alterar tudo\n']
            keys = ['nomeex','series','reps']
            for i, option in enumerate(options,1):
                print(f'[{i}] - {option}')

            choice = input('Digite a opção desejada: ')
            if choice.isdigit() and int(choice) is not TypeError and int(choice) <= len(options):
                choice = int(choice)
                if choice == 4:
                    del cadastro_alunos[search]['treino'][nomeex]
                    updated_exercise = add_exercise(search)
                    write_data()
                    show_info('Aluno Alterado', False, search, True, updated_exercise)
                else: 
                    update = input(f'Digite o(a) {options[choice-1]} atualizado(a): ')
                    if choice == 2 or choice == 3:
                        cadastro_alunos[search]['treino'][nomeex][keys[choice-1]] = update
                        write_data()
                        show_info('Aluno Alterado', False, search, True, cadastro_alunos[search]['treino'][nomeex]['nomeex'])
                    else:
                        cadastro_alunos[search]['treino'][update] = cadastro_alunos[search]['treino'].pop(nomeex)
                        cadastro_alunos[search]['treino'][update]['nomeex'] = update
                        write_data()
                        show_info('Aluno Alterado', False, search, True, cadastro_alunos[search]['treino'][update]['nomeex'])
            else:
                print('Opção inválida, tente de novo...')
        else:
            print('Exercício não existe.')
    else:
        print('Não há exercícios cadastrados para este aluno.')

def delete_exercise(search:str):
    load_data()
    print(f"\n{'-'*130}")
    if len(cadastro_alunos[search]['treino']) > 0:
        searchex = input('Digite o nome do exercício que deseja remover: ')
        if searchex in cadastro_alunos[search]['treino']:
            show_info('Exercício Deletado', False, search, True, searchex)
            del cadastro_alunos[search]['treino'][searchex]
            write_data()
        else:
            print('Exercício não existe na ficha de treino.')
    else:
        print('Não há treinos na ficha.')

def enter_training(first_time:bool=True, search:str=None):
    load_data()
    if len(cadastro_alunos) > 0:
        while True:
            if first_time:
                print(f"\n{'-'*130}")
                search = input('Digite a matricula do aluno para acessar a ficha de treino: \n')
            elif search is None:
                return 5

            if search.isdigit() and search in cadastro_alunos:
                choice = menu(cadastro_alunos[search]['nome'], True)
                if choice == 1:
                    add_exercise(search)
                elif choice == 2:
                    show_info('Ficha de Treino', True, search, True)
                elif choice == 3:
                    update_training_info(search)
                elif choice == 4:
                    delete_exercise(search)
                elif choice == 5:
                    return 5
    
                end = enter_training(False, search)
                if end == 5:
                        return 5
            else:
                print('Aluno não encontrado. . .')
                return 5
    else:
        print(f"\n{'-'*130}")
        print('Não há alunos cadastrados. . .')
base_alunos = []

def menu():
    print('{0:^130}'.format('-'*130))
    opcoes = ['Adicionar um Aluno','Visualizar todos os alunos','Informações detalhadas','Editar Aluno','Excluir Aluno','Sair da aplicação']
    for i, op in enumerate(opcoes,1):
        print(f'[{i}] - {op}')

    choose = input('Digite a opção desejada: ')
    if choose.isdigit() and int(choose) <= len(opcoes):
        return int(choose)
    else: 
        print('Opção inválida\n')
        return 'continue'


def add_aluno():
    print('{0:^130}'.format('-'*130))
    mat = int(input('Digite a matricula do aluno: '))
    nome = input('Digite o nome do aluno: ')
    idade = int(input('Digite a idade do aluno: '))
    curso = input('Digite o curso em que está o aluno: ')
    inst = input('Digite a instituição do discente: ') 
    
    while True:
        n1 = float(input('\nDigite a primeira nota do aluno: '))
        n2 = float(input('Digite a segunda nota do aluno: '))
        if n1 <= 10.0 and n2 <= 10.0:
            break
        else: 
            print('\nxNotas em formato inválido XX,x . Tente de novo...')

    media = (n1+n2)/2
    aluno = [mat,nome,idade,curso,inst,n1,n2,media]
    base_alunos.append(aluno)
    return aluno

def show_aluno(showall,title,search,aluno_given):
    if len(base_alunos) > 0:
        print('{0:^130}'.format('-'*130))
        print('{0:^130}'.format(title))
        print('{0:^130}'.format('-'*130))
        if showall:
            print('{0:<10}{1:<40}{2:<40}{3:<40}\n'.format('Matricula','Nome','Curso','Instituição'))
            for aluno in base_alunos:
                print('{0:<10}{1:<40}{2:<40}{3:<40}'.format(aluno[0],aluno[1],aluno[3],aluno[4]))

        if not showall:
            print('{0:<10}{1:<35}{2:<10}{3:<15}{4:<20}{5:<10}{6:<10}{7:<10}\n'.format('Matricula','Nome','Idade','Curso','Instituição','1º Nota','2º Nota','Media'))
            for i, aluno in enumerate(base_alunos):
                if not (search == None):
                    if int(search) == base_alunos[i][0]:
                        print('{0:<10}{1:<35}{2:<10}{3:<15}{4:<20}{5:<10}{6:<10}{7:<10}'.format(aluno[0],aluno[1],aluno[2],aluno[3],aluno[4],aluno[5],aluno[6],aluno[7]))
                        return
                    
                    else:
                        print('Aluno não encontrado!')
                        return

                else:
                    print('{0:<10}{1:<35}{2:<10}{3:<15}{4:<20}{5:<10}{6:<10}{7:<10}'.format(aluno_given[0],aluno_given[1],aluno_given[2],aluno_given[3],aluno_given[4],aluno_given[5],aluno_given[6],aluno_given[7]))
                    return
    else:
        print('Não há elementos na lista. . .')

def update_aluno():
    if len(base_alunos) > 0:
        search = input('Digite a MATRICULA ou NOME do aluno para alterar informações: ')
        for i, aluno in enumerate(base_alunos):
            if int(search) == aluno[0] or search == aluno[1]:
                opcoes = ['Matricula','Nome','Idade','Curso','Instituição','1º Nota','2º Nota','TUDO']
                
                print('O que deseja alterar?')
                for indx, op in enumerate(opcoes,1):
                    print(f'[{indx}] - {op}')
                    
                choose = int(input('Digite a opção desejada: '))
                
                if choose <= len(opcoes):
                    for indx, peer in enumerate(opcoes,1):
                        if choose == indx:
                            if choose == 8:
                                print('Insira os dados do aluno: ')
                                aluno = add_aluno()
                                del base_alunos[i]
                                break

                            update = input(f'Digite a atualização do(a) {peer}: ')
                            if indx == 1 or indx == 3: 
                                base_alunos[i][indx-1] = int(update)
                                break 

                            elif indx == 6 or indx == 7: 
                                base_alunos[i][indx-1] = float(update)
                                base_alunos[i][7] = (base_alunos[i][6]+base_alunos[i][5])/2
                                break

                            elif indx == 2 or indx == 4 or indx == 5:
                                base_alunos[i][indx-1] = update
                                break

                    show_aluno(False,'Aluno Atualizado',None,aluno)
                
                else:
                    print('Opção inválida')
                    return
                
            else:
                print('Aluno não encontrado!')

    else:
        print('Não há elementos na lista. . .')

def delete_aluno():
    if len(base_alunos) > 0:
        search = input('Digite a MATRICULA ou NOME do aluno para deleta-lo: ')
        for i, aluno in enumerate(base_alunos):
            if search == aluno[0] or int(search) == aluno[2]:
                sure = input(f'Tem serteza que deseja apagar o aluno: {aluno[1]}? \n[1]-SIM \n[2]-NÃO\n   ')
                if sure == 1:
                    deleted_aluno = base_alunos.pop(i)
                    show_aluno(False, 'Aluno Deletado',None,deleted_aluno)
                else:
                    return
            
            else: 
                print('Aluno não encontrado! ')
    
    else: 
        print('Não há elementos na lista. . .')
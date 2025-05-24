# Base de Alunos - Lista vazia 
base_alunos = []

# Implementação das funções do controlador

def menu():
    print('[1] - Cadastrar novo aluno ')
    print('[2] - Listar alunos cadastrados')
    print('[3] - Pesquisar uma Aluno')
    print('[4] - Excluir um cadastro')
    print('[5] - Sair da aplicação')
    chose = int(input('Digite a opção: '))
    return chose

def new_aluno():
    print('-------------------------------------')
    
    nome = input('Digite o nome do novo aluno: ')
    matricula = int(input(f'Digite a matricula de {nome}: '))
    n1 = float(input('Digite a 1º nota do aluno: '))
    n2 = float(input('Digite a 2º nota do aluno: '))
    media = (n1+n2)/2
    aluno = [matricula,nome,n1,n2,media]
    base_alunos.append(aluno)

    print('-------------------------------------')
    print('Aluno cadastrado com sucesso!')
    print(aluno)
    print('-------------------------------------')

def print_alunos():
    print('-------------------------------------')
    
    if len(base_alunos) > 0:
        
        for i in range(0,len(base_alunos)):
            print(base_alunos[i])
    
    else:
        print('Não há alunos cadastrados...')
    print('-------------------------------------')

def search_aluno(matricula):
    print('-------------------------------------')
    if len(base_alunos) > 0:
        
        for i in range(0,len(base_alunos)):
            
            if matricula == base_alunos[i][0]:
                print('Aluno encontrado: ', base_alunos[i])
            else:
                print('Aluno não encotrado...')

    else:
        print('Não há alunos cadastrados...')
    
    print('-------------------------------------')

def delet_aluno(matricula):
    print('-------------------------------------')
    if len(base_alunos) > 0:
        
        for i in range(0,len(base_alunos)):
            
            if matricula == base_alunos[i][0]:
                confirm = int(input(f'Quer mesmo deletar o aluno: {base_alunos[i][1]}?\n [1] - SIM\n [2] - NÃO\n '))
                print('-------------------------------------')
                
                if confirm == 1:
                    deleted_aluno = base_alunos.pop(i)
                    print(f'Aluno deletado: {deleted_aluno}')
                else:
                    print('Aluno não deletado...')
                    break
                
            else:
                print('Aluno não encotrado...')
                print('-------------------------------------')

    else:
        print('Não há alunos cadastrados...')
    
    print('-------------------------------------')
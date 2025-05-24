from ControlerQ1_4 import *

def main():
    while True:
        choose = menu()
        if choose == 'continue':
            continue
        if choose == 1:
            add_aluno()

        elif choose == 2:
            show_aluno(True,'Alunos Cadastrados',None,None)
        
        elif choose == 3:
            search = input('\nDigite a matricula do aluno para Pesquisar informações específicas: ')
            show_aluno(False,'Informações Especificas',search, None)

        elif choose == 4: 
            update_aluno()
        
        elif choose == 5:
            delete_aluno()
        
        elif choose == 6:
            print('Aplicação finalizada!')
            break
main()
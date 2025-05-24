from Controler_alunoEx2 import *

def main():
    while True:
        chose = menu()
        match chose:
            case 1:
                new_aluno()
            case 2:
                print_alunos()
            case 3:
                matricula = int(input('Digite a matricula do aluno para VISUALIZAR os dados: '))
                search_aluno(matricula)
                pass
            case 4: 
                matricula = int(input('Digite a matricula do aluno para EXCLUIR seus dados: '))
                delet_aluno(matricula)
                pass
            case 5:
                print('Aplicação finalizada!')
                break

main()
from FuncoesZildo import *

# Função Principal

def main():
    while True:
        opcaoMenu=menu()
        if opcaoMenu==1:
            cadastrarAluno()
        elif opcaoMenu==2:
            listarAlunos()
            # pass
        elif opcaoMenu == 3:
            matPesquisa=int(input("Digite matrícula para pesquisa: "))
            pesquisarPorMatricula(matPesquisa)
            pass

        elif opcaoMenu == 4:
            matPesquisa = int(input("Digite matrícula para exclusão: "))
            excluirPorMatricula(matPesquisa)
            pass

        elif opcaoMenu == 5:
            print("Aplicação finalizada!!!")
            break
        else:
            print("Opção inválida!!!")


main()
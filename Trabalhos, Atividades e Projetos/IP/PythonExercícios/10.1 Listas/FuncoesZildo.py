
""" 11.1 - Exemplo de cadastro de aluno com lista - Parte 1
ZILDOMAR FELIX
•
13 de dez.
Segue a solução criada em sala para o problema de cadastro de alunos com listas em Python """


# Lista de alunos (lista de listas)
baseAlunos=[[222, 'Zildomar', 6.0, 7.0],[333, 'Felipe', 7.0, 8.0]]

def menu():
    print("[1] - Cadastrar Aluno")
    print("[2] - Listar Alunos")
    print("[3] - Pesquisar aluno por matrícula")
    print("[4] - Excluir aluno por matrícula")
    print("[5] - Sair")
    opcao=int(input("Opção:"))
    return opcao

def cadastrarAluno():
    matricula = int(input("Digite a matrícula do aluno:"))
    nome = input("Digite o nome do aluno:")
    n1 = float(input("Digite a nota 1 do aluno:"))
    n2 = float(input("Digite a nota 2 do aluno:"))
    aluno=[matricula,nome,n1,n2]
    baseAlunos.append(aluno)

def listarAlunos():
    print("{0:^80}".format("-" * 80))
    print("{0:^80}".format("Listagem de Alunos"))
    print("{0:^80}".format("-" * 80))
    print("{0:<15}{1:<20}{2:<5}{3:<5}".format("Matrícula", "Nome","N1","N2"))

    for aluno in baseAlunos:
        print("{0:<15}{1:<20}{2:<5}{3:<5}".format(aluno[0], aluno[1], aluno[2], aluno[3]))
    print("{0:^80}".format("-"*80))

def imprimeAluno(titulo, aluno):
    print("{0:^80}".format("-" * 80))
    # print("{0:^80}".format("Listagem de Alunos"))
    print("{0:^80}".format(titulo))
    print("{0:^80}".format("-" * 80))
    print("{0:<15}{1:<20}{2:<5}{3:<5}".format("Matrícula", "Nome", "N1", "N2"))
    print("{0:<15}{1:<20}{2:<5}{3:<5}".format(aluno[0], aluno[1], aluno[2], aluno[3]))
    print("{0:^80}".format("-" * 80))

def pesquisarPorMatricula(matPesq):
    for aluno in baseAlunos:
        if aluno[0]==matPesq:
            imprimeAluno("Aluno Pesquisado", aluno)
            return
    print("Aluno não encontrado!!!!")

def excluirPorMatricula(matPesq):
    for i, aluno in enumerate(baseAlunos):
        if aluno[0]==matPesq:
            # print("Índice do Aluno:", i)
            # print("Aluno:", aluno)
            # del baseAlunos[i]
            alunoExcluido= baseAlunos.pop(i)
            imprimeAluno("Lista de Alunos Excluídos",alunoExcluido)
            print("Dados excluídos:", alunoExcluido)
            return
    print("Aluno não encontrado!!!!")

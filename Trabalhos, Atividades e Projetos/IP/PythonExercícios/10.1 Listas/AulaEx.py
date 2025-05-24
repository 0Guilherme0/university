list_nome = []
list_matricula = []
list_n1 = []
list_n2 = []
list_media = []


def tabela_aluno():
    tamanho = int(input('Digite a quantidade de alunos que quer cadastrar: '))

    for i in range(0,tamanho):
        nome = input(f'Digite o nome do {i+1}º aluno: ')
        list_nome.append(nome)

        matricula = input(f'Digite a matricula do aluno {nome}: ')
        list_matricula.append(matricula)

        nota1 = float(input(f'Digite a primeira nota de {nome}: '))
        list_n1.append(nota1)

        nota2 = float(input(f'Digite a segunda nota de {nome}: '))
        list_n2.append(nota2)
        
        media = (nota1+nota2)/2
        list_media.append(media)

        print('--------------------------------------------------')
    
    for i in range(0,tamanho):
        print(f'Matricula: {list_matricula[i]}')
        print(f'Nome: {list_nome[i]}')
        print(f'Nota1: {list_n1[i]}')
        print(f'Nota2: {list_n2[i]}')
        print(f'Media: {list_media[i]}')

        print('------------------------------')

def pesquisa_mat():
    search = int(input('Digite a matricula para ser encontrada: '))
    status = False
    for i in range(0,len(list_matricula)):
        if search == list_matricula[i]:
            print(f'Match da matricula {search} é {list_nome[i]}')
            status = True
    
    if not status:
        print('Matricula não encontrada!!!')




def main():  
    tabela_aluno()
    pesquisa_mat()

main()

        
        
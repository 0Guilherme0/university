# Funções da segunda questão de listas: Biblioteca

base_books = []

def menu():
    print('{0:^130}'.format('-'*130))
    print('O que deseja fazer na sua biblioteca? ')
    print('[1] - Adicionar Livro')
    print('[2] - Pesquisar Livro')
    print('[3] - Atualizar Informações ')
    print('[4] - Remover Livro')
    print('[5] - Sair da Aplicação')
    op = int(input('Digite a opção desejada: '))
    return op

def add_book(argue):
    print('{0:^130}'.format('-'*130))
    title = input('Digite o titulo da obra: ')
    autor = input('Digite o Nome do Autor: ')
    gender = input('Digite o Genero da obra: ')
    date = input('Digite a data de publicação: ')
    book = [title, autor, gender, date]
    
    if not argue:
        base_books.append(book)
    else:
        return book
    
    print('Livro adicionado com sucesso!')

def show_book(title,book):
    print('{0:^130}'.format('-'*130))
    print('{0:^130}'.format(title))
    print('{0:^130}'.format('-'*130))
    print('{0:<45}{1:<45}{2:<20}{3:<20}'.format('Titulo','Autor','Genero','Data de Publicação\n'))
    print('{0:<45}{1:<45}{2:<20}{3:<20}'.format(book[0],book[1],book[2],book[3]))

def search_book():
    print('{0:^130}'.format('-'*130))
    if len(base_books) > 0:
        search = input('Digite o TITULO da obra ou o AUTOR para VISUALIZAR o livro: ')
        search = search.lower()
        for i, book in enumerate(base_books):
            if search == book[0] or search == book[1]:
                show_book('Livro Pesquisado', base_books[i])
                return
            
            else:
                print('Sem matchs para pesquisa ')
    else:
        print('Não há livros cadastrados. . .')
            
def update_book():
    print('{0:^130}'.format('-'*130))
    if len(base_books) > 0:
        search = input('Digite o TITULO ou o AUTOR da obra para ATUALIZAR os dados do livro: ')
        
        for i, book in enumerate(base_books):
            if search == book[0] or search == book[1]:
                print('O que quer editar?')
                print('[1] - Titulo \n[2] - Autor \n[3] - Genero \n[4] - Data de Publicação \n[5] - Tudo')
                op = int(input('Digite a opção desejada: '))
                
                if op == 1:
                    new_title = input('Digite o titulo atualizado: ')
                    book[0] = new_title
                    print('Titulo alterado com sucesso! ')

                elif op == 2: 
                    new_autor = input('Digite o nome do autor atualizado! ')
                    book[1] = new_autor
                    print('Nome do autor atualizado com sucesso! ')

                elif op == 3: 
                    new_gender = input('Digite o genero atualizado: ')
                    book[2] = new_gender
                    print('Genero alterado com sucesso!')
                
                elif op == 4: 
                    new_date = input('Digite a data de publicação atualizada: ')
                    book[3] = new_date
                    print('Data de Publicação atualizada com sucesso! ')
                
                elif op == 5:
                    base_books[i] = add_book(True)
                    print('Livro alterado com sucesso!')
                
                else:
                    print('Opção Iválida! ')
                    break

                show_book('Livro Atualizado', base_books[i])
                return
    else:
        print('Não há livros cadastrados. . .')

def delete_book():
    print('{0:^130}'.format('-'*130))
    if len(base_books) > 0:
        search = input('Digite o TITULO ou AUTOR da obra para DELETAR o livro: ')
        search = search.lower()

        for i, book in enumerate(base_books):
            if search == book[0] or search == book[1]:
                sure = int(input('Tem certeza que quer deletar o livro?\n [1] - SIM\n [2] - NÃO\n  ')) 
                
                if sure == 1:
                    del base_books[i]
                    show_book('Livro Deletado', book)
                    return
                else:
                    return
            
            else:
                print('Não livro não cadastrado!')
    
    else:
        print('Não há livros cadastrados. . .')
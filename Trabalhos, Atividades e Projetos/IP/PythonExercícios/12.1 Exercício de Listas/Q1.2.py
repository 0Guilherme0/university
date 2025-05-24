""" Biblioteca de Livros: Crie um programa para gerenciar uma biblioteca
de livros. Permita adicionar novos livros, buscar livros pelo título ou autor,
atualizar informações e remover livros.
Base de dados da Biblioteca

Título Autor Gênero Ano de Publicação """

from ControlerQ1_2 import *

def main():
    while True:
        choice = menu()
        
        if choice == 1:
            add_book(False)
            pass 
        
        elif choice == 2:
            search_book()
            pass

        elif choice == 3:
            update_book()
            pass

        elif choice == 4:
            delete_book()
            pass 
        
        elif choice == 5:
            break
        
        else:
            print('Opção inválida! ')

main()

""" 10.Escreva um programa que leia uma lista de strings do usuário e exiba
todas as strings que começam com a letra "A". """

def strings_com_A(lista):
    return [s for s in lista if s.lower().startswith('a')]


def main():
    entrada_usuario = input("Digite uma lista de strings separadas por vírgula: ")
    lista_de_strings = entrada_usuario.split(',')
    strings_comecando_com_A = strings_com_A(lista_de_strings)

    print("Strings que começam com 'A':")
    for string in strings_comecando_com_A:
        print(string)

if __name__ == "__main__":
    main()

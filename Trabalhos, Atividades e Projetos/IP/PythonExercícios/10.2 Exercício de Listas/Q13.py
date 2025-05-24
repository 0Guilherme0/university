""" 13.Escreva uma função chamada inverte_lista que receba uma lista como
parâmetro e retorne uma nova lista contendo os elementos da lista
original, porém na ordem inversa. """

def main():
    entrada_usuario = input("Digite strings separados por virgula: ")
    entrada = entrada_usuario.split(',')
    lista = [string for string in entrada]
    lista_invertida = list(reversed(lista))

    print("Lista de números na ordem inversa:", lista_invertida)

main()
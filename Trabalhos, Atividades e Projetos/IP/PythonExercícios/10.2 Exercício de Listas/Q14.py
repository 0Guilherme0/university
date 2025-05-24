""" 14.Escreva um programa que leia uma lista de números inteiros do usuário
e exiba o segundo maior número da lista. """

def segundo_maior(numbers):
    # Converte as strings para inteiros
    numeros = [int(numero) for numero in numbers]

    # Remove duplicatas para lidar com casos como [2, 2, 1]
    numeros_unicos = list(set(numeros))

    if len(numeros_unicos) < 2:
        print("Não há segundo maior número.")
    else:
        numeros_unicos.sort()
        segundo_maior_numero = numeros_unicos[-2]
        print(f'O segundo maior número é {segundo_maior_numero}')

def main():
    entrada = input('Digite uma lista de números inteiros separados por vírgula: ')
    lista_numbers = entrada.split(',')
    segundo_maior(lista_numbers)

if __name__ == "__main__":
    main()

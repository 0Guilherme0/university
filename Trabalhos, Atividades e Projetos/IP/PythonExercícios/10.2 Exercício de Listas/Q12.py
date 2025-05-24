def main():
    entrada_usuario = input("Digite 5 números inteiros separados por espaço: ")
    numeros_str = entrada_usuario.split()
    numeros_inteiros = [int(numero) for numero in numeros_str]
    numeros_inteiros_invertidos = list(reversed(numeros_inteiros))

    print("Lista de números na ordem inversa:", numeros_inteiros_invertidos)

main()

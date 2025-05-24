""" 11.Escreva um programa que leia uma lista de números inteiros do usuário
e exiba todos os números que são múltiplos de 3 e 5. """

def multiplosde15(numbers):
    for test in numbers:
        if int(test) % 15 == 0:
            return True
    return False

def main():
    numbers = input('Digite uma lista de números inteiros separados por vírgula: ')
    lista_de_numeros = numbers.split(',')
    
    print('É múltiplo de 3 e de 5: ')
    
    encontrou_multiplo = False
    for number in lista_de_numeros:
        if multiplosde15(number):
            print(number)
            encontrou_multiplo = True
    
    if not encontrou_multiplo:
        print('Nenhum número é múltiplo de 3 e de 5 na lista.')

main()

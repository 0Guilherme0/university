""" Implemente uma função que conte o número de vogais em uma palavra
ou frase. Teste a função com diferentes entradas. """


def questao7():
    def count_voagais():
        char = input('Digite uma palavra ou frase: ')
        vogais = 'aeiou'
        count_voagais = 0

        char = char.lower()

        for char_in_input in char:
            if char_in_input in vogais:
                count_voagais += 1

        return count_voagais

    result = count_voagais()
    print(f'O número de vogais na palavra ou frase é: {result}')
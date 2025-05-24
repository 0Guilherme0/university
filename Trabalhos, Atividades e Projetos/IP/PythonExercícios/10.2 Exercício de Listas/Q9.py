""" Escreva um programa que leia uma lista de nomes do usuário e exiba o
nome mais longo e o nome mais curto da lista. """

def maior_menor_nome(nomes):
    maioremenorNomes = []
    maiorNome, menorNome = '', ' '*100

    for nome in nomes:
        if len(maiorNome) < len(nome):
            maiorNome = nome
        
        if len(menorNome) > len(nome):
            menorNome = nome
    maioremenorNomes.append(maiorNome)
    maioremenorNomes.append(menorNome)
    return maioremenorNomes

a = maior_menor_nome(['Guilherme Pereira Souza', 'Mariane','Jhon Herison'])
print(a)
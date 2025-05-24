""" Escreva uma função chamada separa_positivos_negativos que receba
uma lista de números inteiros como parâmetro e retorne duas listas: uma
contendo os números positivos e outra contendo os números negativos. """

def separa_positivos_negativos(numbers):
    positives = []
    negatives = []
    positivos_negativos = []

    for numb in numbers:
        if numb > 0:
            positives.append(numb)
        else:
            negatives.append(numb)

    positivos_negativos.append(positives)
    positivos_negativos.append(negatives)
    
    return positivos_negativos

a = separa_positivos_negativos([5,9,-5,-9,8,-10,-2689,1000])

print(a)
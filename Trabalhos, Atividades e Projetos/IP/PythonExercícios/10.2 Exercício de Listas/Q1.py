numeros = [10,7,9]

def calcula_media(numeros):
    soma = 0
    for i, numb in enumerate(numeros):
        soma += numb
    
    media = soma/(i+1)
    return media

media = calcula_media(numeros)
print(media)

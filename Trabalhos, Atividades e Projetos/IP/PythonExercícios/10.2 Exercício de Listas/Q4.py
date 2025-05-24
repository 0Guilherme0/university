def maioremenor():
    maior, menor = 0,0
    lista = input('Digite números inteiros: ')
    lista = lista.split()
    
    for i in lista:
        i = int(i)
        if maior < i:
            maior = i
        if menor > i:
            menor = i
    print(maior, menor)

maioremenor()
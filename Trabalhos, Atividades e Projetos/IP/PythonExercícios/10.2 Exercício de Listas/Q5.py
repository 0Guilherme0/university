def npar():
    lista = input('Digite números inteiros: ')
    lista = lista.split()
    par = []
    for i in lista:
        i = int(i)
        if i % 2 == 0:
            par.append(i)
        
    print(par)

npar()
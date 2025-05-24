def maioresQ5():
    string = input('Digite uma frase ou palavras: ')
    string = string.split()
    bigword = []
    for i, maiorq5 in enumerate(string):
        if len(maiorq5) > 5:
            bigword.append(string[i])
    print(bigword)

maioresQ5()

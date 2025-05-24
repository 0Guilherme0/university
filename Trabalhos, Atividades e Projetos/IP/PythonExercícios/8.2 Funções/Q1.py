""" Faça uma função que recebe um número inteiro como argumento. A
função retorna o caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu
argumento for zero ou negativo. """

def positivo(numb):
    if numb > 0:
        return 'P'
    else:
        return 'N'
    
numb = int(input('Digite um número inteiro: '))
print(positivo(numb))

""" Faça um programa que recebe três números do usuário, e identifica o
maior através de uma função e o menor número através de outra função. """

def maior_numb(n1,n2,n3):
    maiorN = n1

    if maiorN < n2:
        maiorN = n2
    if maiorN < n3:
        maiorN = n3
    
    return maiorN

def menor_numb(n1,n2,n3):
    menorN = n1

    if menorN > n2:
        menorN = n2
    if menorN > n3:
        menorN = n3
    
    return menorN

n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
n3 = float(input('Digite outro valor: '))

print(menor_numb(n1,n2,n3))
print(maior_numb(n1,n2,n3))







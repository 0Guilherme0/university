""" Crie uma função que calcule o Índice de Massa Corporal (IMC) com base
no peso e altura fornecidos pelo usuário. """

def imc():
    altura = float(input('Digite sua altura em metros: '))
    massa = float(input('Digite seu peso em Kg: '))
    return (massa/altura**2)

print(imc())
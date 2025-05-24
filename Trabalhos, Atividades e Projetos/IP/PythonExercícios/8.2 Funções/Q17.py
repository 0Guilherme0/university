""" Crie uma função que receba 3 valores e calcula as raízes da fórmula de
Bháskara. """

import math

def bhaskara(a,b,c):
    delta = (b**2)-4*a*c
    if a == 0:
        print('A função não é quadrática')
    if delta < 0:
        print('A função não tem raizes reais...')
    else:
        x1 = (-(b) +(math.sqrt(delta)))/2*a
        x2 = (-(b) -(math.sqrt(delta)))/2*a
        print(x1, x2)

def main():
    print('Digite os valores de a, b e c de uma função quadrática: ')
    a = float(input('Digite o valor de a: '))
    b = float(input('Digite o valor de b: '))
    c = float(input('Digite o valor de c: '))
    bhaskara(a,b,c)

main()
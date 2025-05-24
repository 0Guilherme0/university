""" Faça uma função que calcule a área de um círculo. Insira o raio como
argumento. """

def questao3():
    def area_circulo(raio):
        a = 3.14159265359*(raio)**2
        return a 

    raio = float(input('Digite o raio da circunferência: '))
    print(area_circulo(raio))
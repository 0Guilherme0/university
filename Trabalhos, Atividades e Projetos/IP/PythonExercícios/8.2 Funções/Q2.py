""" Faça uma função que determina se um número é par ou ímpar. A função
deve retornar True (valor lógico) se for par e False (valor lógico) se for
ímpar. """
def questao2():
    def parimpar(numb):
        if numb%2 == 0:
            return True
        else:
            return False
        
    numb = float(input('Digite um número: '))
    print(parimpar(numb)) 
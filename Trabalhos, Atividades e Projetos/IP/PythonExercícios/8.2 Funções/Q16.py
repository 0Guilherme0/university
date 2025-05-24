""" Desenvolva uma função que determine se um ano é bissexto. Peça ao
usuário para inserir o ano e exiba o resultado. """

def anobissexto(ano):
    if ano % 4 == 0:
        print('Ano bissexto!')
    else:
        print('Ano não bissexto!')
    
def main():
    ano = int(input('Digite um ano qualquer: '))
    anobissexto(ano)

main()
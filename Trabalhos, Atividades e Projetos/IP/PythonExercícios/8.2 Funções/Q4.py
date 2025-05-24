""" Implemente funções para converter temperatura entre Celsius e
Fahrenheit. Peça ao usuário para inserir a temperatura e a unidade
desejada (C ou F) e exiba o resultado da conversão. """

def questao4():
    def convercao():
        op = int(input('Digite a opção para a converção: \n [1] - Celcius par Fahrenheit \n [2] - Fahrenheit para Celcius '))
    
        if op == 1:
            temp = float(input('Digite a temperatura em Celcius: '))
            temp = ((temp/5)*9)+32
            return temp
        else:
            temp = float(input('Digite a temperatura em Fahrenheit: '))
            temp = ((temp-32)/9)*5
            return temp
        
    print(convercao())
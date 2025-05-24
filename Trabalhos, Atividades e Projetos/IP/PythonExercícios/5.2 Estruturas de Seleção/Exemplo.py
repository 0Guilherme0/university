print('Qual a operação desejada\n [1] - Somar os dois números ')
print(' [2] - Subtrair os dois números\n [3] - Multiplicar os dois números\n [4] - Dividir os dois números')
escolha=int(input())
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
result = None
if escolha == 1:
    result = n1+n2
    print('A soma é: ',result)
elif escolha == 2:
    result = n1-n2
    print('A subtração é: ',result)
elif escolha == 3:
    result = n1*n2
    print('A multiplicação entre os dois números é: ', result)
elif escolha == 4: 
    reslut = n1/n2
    print('A divisão entre os dois números é: ',reslut)
else:
    print('Opção inválida')
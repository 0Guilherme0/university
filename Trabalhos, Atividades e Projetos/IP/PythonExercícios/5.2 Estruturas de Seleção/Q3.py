idade = int(input('Digite a sua idade: '))
#if int(idade) == ValueError:
#    print('Idade inválida')           ????????????????
#else:
if idade <= 15:
    parentslicence = input('Seus pais tem uma licença de pesca? S ou N ')
    if parentslicence == 'S' or 's':
        print('Você pode pescar!! ')
    elif parentslicence == 'N' or 'n': 
        print('Você não pode pescar...')
    else:
        print('Resposta inválida')
elif idade > 15:
    perslicence = input('Voçê possui licença de pesca?? S ou N ')
    if perslicence == 'N' or 'n':
        print('Você não pode pescar...')
    elif perslicence == 'S' or 's': #Resultado sai errado#
        print('Você pode pescar!!')
    else:
        print('Resposta inválida')

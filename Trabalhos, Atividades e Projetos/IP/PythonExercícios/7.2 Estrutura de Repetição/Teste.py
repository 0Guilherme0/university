qH, qM, qG, hy, my, soma_idadeH, soma_idadeM, media_idadeH, media_idadeM, idade_mediaG, idade  = 0,0,0,0,0,0,0,0,0,0,0

sexo = None
numb_pessoas = int(input('Digite a quantidade de pessoas '))

for pessoas in range(1,(numb_pessoas + 1)):
    sexo = int(input('Homem [1] ou Mulher [2]: '))

    if sexo == 1:
        idade = int(input('Digite a idade da pessoa: '))
        soma_idadeH += idade
        qH += 1
    elif sexo == 2:
        idade = int(input('Digite a idade da pessoa: '))
        soma_idadeM += idade   
        qM += 1
    else: 
        print('Sexo inválido ')
        break
    
qG = qM + qH
idade_mediaG = (soma_idadeH + soma_idadeM)/qG
media_idadeH = soma_idadeH/qH
media_idadeM = soma_idadeM/qM
print('A idade média dos homens é: ',media_idadeH)
print('A idade média das mulheres é: ',media_idadeM)
print('A média do grupo é: ',idade_mediaG)
print(f'São {qH} pessoas do sexo masculino')
print(f'São {qM} pessoas do sexo feminino')
quantalunos = int(input('Digite a quantidade de alunos: '))
n1 = 0
n2 = 0
media = 0
naprovados = 0
nreprovados = 0
mediageral = 0

# while quantalunos != 0:
#     quantalunos -= 1
#     n1 = float(input('Digite a primeira nota: '))
#     n2 = float(input('Digite a segunda nota: '))
#     print('--------------------------------------')
#     media = (n1+n2)/2
#     mediageral += media
#     
#     if media >= 7:
#         naprovados += 1
#     else:
#         nreprovados += 1
# quantalunos

# mediageral = mediageral/quantalunos
# print('O número de alunos aprovados foi {0} e o número de alunos reprovados foi {1}'.format(naprovados,nreprovados))
# print('A media geral da turama foi ',mediageral)

for quantalunos in quantalunos:
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    print('--------------------------------------')
    media = (n1+n2)/2
    mediageral += media
   
    if media >= 7:
        naprovados += 1
    else:
        nreprovados += 1

mediageral = mediageral/quantalunos
print('O número de alunos aprovados foi {0} e o número de alunos reprovados foi {1}'.format(naprovados,nreprovados))
print('A media geral da turama foi ',mediageral)

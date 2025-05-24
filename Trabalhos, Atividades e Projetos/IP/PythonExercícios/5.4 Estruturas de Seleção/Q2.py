""" Crie um programa em Python que simule um menu de 5 opções. Ao
digitar a opção desejada o programa deverá imprimir na tela: “Você
escolheu a opção X” e aguardar que o usuário pressione alguma tecla
para encerrar o programa. O programa não deverá aceitar opções que
não fazem parte do menu.
Menu: [1] – Cadastrar
[2] – Pesquisar
[3] – Remover
[4] – Editar
[5] – Sair """

print('Menu: [1] - Cadastrar')
print('      [2] - Pesquisar')
print('      [3] - Remover')
print('      [4] - Editar ')
print('      [5] - Sair')
choice = int(input('Escolha a opção: '))
match (choice):
    case 1:
        print('Você escolheu a opção [1] - Cadastrar')
    case 2:
        print('Você escolheu a opção [2] - Pesquisar')
    case 3:
        print('Você escolheu a opção [3] - Remover')
    case 4:
        print('Você escolheu a opção [4] - Editar')
    case 5: 
        print('Você escolheu a opção [5] - Sair')
    case _:
        print('Opção inválida')
input()
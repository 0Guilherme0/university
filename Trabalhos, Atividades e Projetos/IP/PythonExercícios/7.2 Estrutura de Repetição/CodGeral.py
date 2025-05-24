while True:
    print('[1] - Questão 1')
    print('[2] - Questão 2')
    print('[3] - Questão 3')
    print('[4] - Questão 4')
    print('[5] - Questão 5')
    print('[6] - Questão 6')
    print('[7] - Questão 7')
    print('[8] - Questão 8') 
    print('[9] - Sair')
    menu = int(input('Selecione a opção: '))
    print('----------------------------------')

    match menu:
        case 1:
            soma = 0
            for count in range(101):
                soma += count
            print(soma)
            print('-------------------------------')
        
        case 2:
            numb = int(input('Quantos valores quer colocar na lista? '))
            
            if numb == 0:
                print('Nenhum ítem na lista')
                break

            menorN = 0
            for count in range (numb):
                lista = int(input('Digite um número inteiro: '))
                if count == 0:
                    menorN = lista
                    continue

                if menorN < lista:
                    continue
                else:
                    menorN = lista
            
            print(f'Print o menor número foi {menorN}')              

        case 3:
            qtd = 0
            for cont in range(10):
                numb = float(input('Digite um número: '))
                if numb >= 10 and numb <= 50:
                    qtd += 1
            
            print(f'A quantidade de números entre 10 e 50 foi de {qtd}')
 
        case 4:
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
            
            if sexo != 1 and sexo != 2:
                print('-------------------------------------------')
                continue
                
            if qH == 0:
                media_idadeH = 0
            if qM == 0: 
                media_idadeM = 0
            if qH != 0:
                media_idadeH = soma_idadeH/qH
            if qM != 0:
                media_idadeM = soma_idadeM/qM

            qG = qM + qH
            idade_mediaG = (soma_idadeH + soma_idadeM)/qG
            print('--------------------------------------------')
            print('A idade média dos homens é: ',media_idadeH)
            print('A idade média das mulheres é: ',media_idadeM)
            print('A média do grupo é: ',idade_mediaG)
            print(f'É(são) {qH} pessoa(s) do sexo masculino')
            print(f'É(são) {qM} pessoa(s) do sexo feminino')
            print('---------------------------------------------')

        case 5:
            numb_empregados = int(input('Digite quantos empregados quer registrar: '))
            matricula = 0
            sal, salB, salS = 0,0,0
            nome, nome_BS, nome_SS = None, None, None
            
            for empregados in range(numb_empregados):
                nome = input('Digite o nome do empregado: ')
                # matricula = input('Digite a matricula do empregado: ')
                sal = float(input('Digite o salário do empregado: '))

                if empregados == 0:
                    salB, salS = sal,sal
                    nome_BS, nome_SS = nome,nome
                
                if salB > sal:
                    pass
                elif salB < sal:
                    salB = sal
                    nome_BS = nome
                
                if salS < sal:
                    continue
                elif salS > sal:
                    salS = sal
                    nome_SS = nome
            
            print('------------------------------------------------------------------------')
            print(f'O empregado com o maior salário foi {nome_BS} e seu salário é R${salB}')
            print(f'O empregado com o maior salário foi {nome_SS} e seu salário é R${salS}')
            print('------------------------------------------------------------------------')

        case 6: 
            print('Digite uma lista de números inteiros terminada por -1')
            numb_list = int(input('Digite o primeiro numero inteiro: '))
            lista = ''

            if numb_list == -1:
                print('A lista está vazia ')
            else:
                lista += str(numb_list) + ', '

            while True:
                numb_list = int(input('Digite mais um número inteiro: '))

                if numb_list == -1:
                    break

                lista += str(numb_list) + ', '

            print(f'A lista de inteiros foi {lista}')
            
            # Initialize an empty list to store the integers
            # integers = []

            # while True:
            #     num_str = input("Enter an integer (enter -1 to terminate): ")

            #     if num_str == "-1":
            #         break

            #     num = int(num_str)
            #     integers.append(num)

            # print("List of integers:", integers)

        case 7:
            lista = input('Digite uma lista de números separados por espaço: ')
            lista = lista.split()
            # Separa os componentes digitados por um espaço apenas

            count, soma = 0,0

            for numb_lista in lista:
                # numb_lista percorre os valores str na 'lista'
                num = float(numb_lista)
                # transforma os 'números str' em números float
                count += 1
                soma += num
            
            media = soma/count

            print(f'A quantidade de números na lista foi {count}')
            print(f'A média dos valores da lista foi {media }')

        case 8:
            print('What do you want to do?')
            print('[1] - Somatório dos números de 1 á 100')
            print('[2] - Tabuada do 8')
            escolha = int(input('Escolha: '))
            
            if escolha == 1:
                soma = 0
                for count in range(101):
                    soma += count
                print(soma)
                print('-------------------------------')

            elif escolha == 2:
                print('---------------------------------')
                for tabuada in range(1,11):
                    mult = 8*tabuada
                    print(f'{tabuada} x 8 = {mult}')
                print('---------------------------------')

        case 9:
            break
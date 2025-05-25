import math

# m = int(input("Número de linhas (m): "))
# n = int(input("Número de colunas (n): "))

# matriz = []
# for i in range(m):
#     linha = list(map(int, input(f"Digite os {n} elementos da linha {i+1}, separados por espaço: ").split()))
#     if len(linha) != n:
#         print("Número de elementos inválido!")
#         exit()
#     matriz.append(linha)
    
matriz = [[1,3,4],
          [0,4,5],
          [4,6,0]]
    
def forma_escada_reduzida(matriz):
    num_linhas = len(matriz) # Atribui o número de linhas da matriz
    num_colunas = len(matriz[0]) # Atribui o número de colunas da matriz
    linha = 0 # Essa é a linha inicial que vai procurar os pivôs
    # A variável linha vai ser usada para percorrer as linhas da matriz e encontrar os pivôs

    for col in range(num_colunas):
        # Encontrar linha com pivô não-nulo
        linha_pivo = linha #Começa a procurar o pivô na linha atual
        while linha_pivo < num_linhas and matriz[linha_pivo][col] == 0: 
            # Enquanto a linha_pivo for menor que o número de linhas e o elemento da coluna atual for igual a 0, incrementa a linha_pivo
            linha_pivo += 1

        if linha_pivo == num_linhas:
            continue  # Nenhum pivo nesta coluna

        # Trocar linhas
        matriz[linha], matriz[linha_pivo] = matriz[linha_pivo], matriz[linha]

        # Tornar o pivo igual a 1
        fator_pivo = matriz[linha][col] # Pega o valor do pivo
        matriz[linha] = [x / fator_pivo for x in matriz[linha]] # Divide o pivo por ele mesmo (e todo o resto da linha)

        # Zerar elementos acima e abaixo do pivo
        for i in range(num_linhas): # Percorre todas as linhas
            if i != linha: #i é o index da linha atual
                fator = matriz[i][col] # Pega o fator que vai zerar o elemento nas colunas
                matriz[i] = [matriz[i][j] - fator * matriz[linha][j] for j in range(num_colunas)] 
                # matriz [i] recebe uma nova linha, onde o elemento da linha i é subtraído do elemento da linha atual multiplicado pelo fator

        linha += 1 # Incrementa a linha para procurar o próximo pivô
        
        if linha == num_linhas: # Acabou a matriz
            break

    return matriz

 
                    
            
        
            









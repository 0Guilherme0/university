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
    
def escalonar(matriz):
    num_linhas = len(matriz)        
    num_colunas = len(matriz[0])   
    linha_pivo_atual = 0           

    for coluna_atual in range(num_colunas):
        if linha_pivo_atual >= num_linhas:
            break  
      
        linha_com_pivo = linha_pivo_atual
        while linha_com_pivo < num_linhas and matriz[linha_com_pivo][coluna_atual] == 0:
            linha_com_pivo += 1

        if linha_com_pivo == num_linhas:
            continue

        matriz[linha_pivo_atual], matriz[linha_com_pivo] = matriz[linha_com_pivo], matriz[linha_pivo_atual]

        valor_pivo = matriz[linha_pivo_atual][coluna_atual]
        matriz[linha_pivo_atual] = [elemento / valor_pivo for elemento in matriz[linha_pivo_atual]]

        for linha_para_zerar in range(linha_pivo_atual + 1, num_linhas):
            fator = matriz[linha_para_zerar][coluna_atual]
            matriz[linha_para_zerar] = [
                elemento - fator * pivô_elemento
                for elemento, pivô_elemento in zip(matriz[linha_para_zerar], matriz[linha_pivo_atual])
            ]

        linha_pivo_atual += 1

    return matriz

matrizEscalonada = escalonar(matriz)
for i in range(len(matrizEscalonada)):
    print(matrizEscalonada[i])
            
                    
            
        
            









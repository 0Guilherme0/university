
# Codigo do GPTchat

def eh_primo(num):
    """Verifica se um número é primo."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filtrar_primos(lista_entrada):
    """Filtra números primos da lista de entrada."""
    return [num for num in lista_entrada if eh_primo(num)]

# Exemplo de uso:
numeros_entrada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = filtrar_primos(numeros_entrada)
print("Lista de Entrada:", numeros_entrada)
print("Números Primos:", resultado)


""" Elevar o número ao meio (ou 0.5) é uma técnica conhecida para encontrar a raiz
quadrada de um número em Python. O motivo de usar a raiz quadrada está
relacionado à propriedade matemática dos números primos.

Aotestar a primalidade de um número n,, não é necessário verificar divisões por todos
os números até n — 1. Se n não for primo, ele terá pelo menos um fator primo que é
menor ou igual à sua raiz quadrada.

Assim, ao invés de verificar divisibilidade até nº — 1, o código verifica até Vn porque
qualquer fator primo de nº deve ser menor ou igual à sua raiz quadrada. Isso
economiza tempo e melhora a eficiência do algoritmo.

Em Python, ** é o operador de exponenciação. Portanto, *num**0.5' significa
"elevar num a 0.5", que é a mesma coisa que calcular a raiz quadrada de * num”. Este
valor é convertido para inteiro usando *int()* para garantir que o loop inclua todos os
números necessários na verificação de divisibilidade. """



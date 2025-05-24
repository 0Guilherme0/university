""" Sabemos que um triângulo é formado por três lados que possuem uma
determinada medida, mas essas não podem ser escolhidas
aleatoriamente como os lados de um quadrado ou de um retângulo, é
preciso seguir uma regra. Só existirá um triângulo se, somente se, os
seus lados obedeceram à seguinte regra: um de seus lados deve ser
maior que o valor absoluto (módulo) da diferença dos outros dois lados e
menor que a soma dos outros dois lados. Veja o resumo da regra
abaixo:
| b - c | < a < b + c
| a - c | < b < a + c
| a - b | < c < a + b """

a = float(input('Digite o primeiro lado: '))
b = float(input('Digite o segundo lado: '))
c = float(input('Digite o terceiro lado: '))
modbc = b-c
modac = a-c
modab = a-b
if modbc < 0:
    modbc = modbc*(-1)
elif modac < 0:
    modac = modac*(-1)
elif modab < 0:
    modab = modab*(-1)

if (a > modbc and a < b+c) and (b > modac and b < a+c) and (c > modab and c < a-b):
    print('Os lados compõem um triângulo')
else:
    print('Os lados NÃO compõem um triângulo')

#Código não funciona

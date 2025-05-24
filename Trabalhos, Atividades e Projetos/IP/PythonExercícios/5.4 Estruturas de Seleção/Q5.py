""" Write a Python program to convert temperatures to and from celsius,
fahrenheit. [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and
f = temperature in fahrenheit ] Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius """

op = int(input('Qual operação de converção quer fazer?\n 1 - F para C \n 2 - C para F\n'))
if op == 1:
   fah = float(input('Digite a temperatua em Fahrenheit: '))
   cel = ((fah-32)/9)*5
   print('A converção de {0}º Fahrenheit em Celsius é {1}º graus '.format(fah, cel))
elif op == 2:
   cel = float(input('Digite a temperatura em Celsius: '))
   fah = (((cel/5)*9)+32)
   print('A converção de {0}º Ceulsius em Fahrenheit é {1}º graus '.format(cel, fah))
else:
   print('Opção inválida')
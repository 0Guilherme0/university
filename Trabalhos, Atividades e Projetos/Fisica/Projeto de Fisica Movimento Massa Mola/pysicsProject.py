from vpython import *

print("="*80)
print("Simulador de Movimento Harmônico Massa-Mola!".center(80))
print("A animação só será fiel no intervalo de espaço de -46 até 46.".center(80))
print("="*80)

print("\nInsira os dados do sistema:")
m = float(input("Digite a massa do bloco (kg): "))  
k = float(input("Digite a constante elástica da mola (N/m): "))  
s_max = float(input("Digite o maximo deslocamento do bloco (m): "))
s_min = float(input("Digite o minimo deslocamento do bloco (m): "))
# b) O deslocamento máximo e mínimo (XM e Xm) ;
# c) V0 a velocidade inicial do movimento do objeto;
# x0 = float(input("Digite a posição de equilíbrio da mola (m) (pode ser negativo): "))
# amplitude = float(input(("Digite a amplitude inicial do movimento (m): ") 
# amplitude += abs(x0)


ground = box(pos=vector(0, -1, 0), size=vector(100, 1, 50), color=color.white)
wall = box(pos=vector(-47.5, 4, 0), size=vector(5, 10, 40), color=color.white)
cube = box(pos=vector(0 + x0, 3.5, 0), size=vector(8, 8, 8), color=color.red)
spring = helix(pos=wall.pos, axis=cube.pos - wall.pos, radius=2, coils=15, thickness=0.1, color=color.green)


graph1 = graph(title="Energia Cinética pelo Deslocamento", xtitle="Deslocamento (m)", ytitle="Energia Cinética (J)")
curva_cinetica1 = gcurve(color=color.blue, label="Energia Cinética", graph=graph1)

graph2 = graph(title="Energias no Sistema", xtitle="Tempo (s)", ytitle="Energia (J)")
curva_cinetica2 = gcurve(color=color.blue, label="Energia Cinética", graph=graph2)
curva_elastica = gcurve(color=color.red, label="Energia Potencial Elástica", graph=graph2)
curva_mecanica = gcurve(color=color.black, label="Energia Mecânica Total", graph=graph2)

graph3 = graph(title="Trabalho Realizado pela Mola", xtitle="Tempo (s)", ytitle="Trabalho Acumulado (J)")
curva_trabalho = gcurve(color=color.cyan, label="Trabalho Total", graph=graph3)


omega = sqrt(k / m)  
t = 0
dt = 0.01
E_total_inicial = 0.5 * k * amplitude**2 

energia_cinetica_anterior = 0  
trabalho_total = 0  
    
while True:
    rate(100)  
    
    deslocamento = amplitude * cos(omega * t)  
    velocidade = -amplitude * omega * sin(omega * t)  
    
    cube.pos.x = x0 + deslocamento
    spring.axis = cube.pos - wall.pos

    energia_cinetica = 0.5 * m * velocidade**2  
    energia_p_elastica = 0.5 * k * deslocamento**2  
    energia_mec_total = energia_cinetica + energia_p_elastica
    
    curva_cinetica1.plot(x0 + deslocamento, energia_cinetica)
    curva_cinetica2.plot(t, energia_cinetica)
    curva_elastica.plot(t, energia_p_elastica)    
    curva_mecanica.plot(t, energia_mec_total)    
    
    if t > 0:
        trabalho_instantaneo = energia_cinetica - energia_cinetica_anterior
        trabalho_total += trabalho_instantaneo 
    curva_trabalho.plot(t, trabalho_total)  
    
    energia_cinetica_anterior = energia_cinetica 
    t += dt


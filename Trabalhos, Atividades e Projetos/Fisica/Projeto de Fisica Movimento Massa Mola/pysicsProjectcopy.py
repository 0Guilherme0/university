from vpython import *

print("="*80)
print("Movimento Harmônico Massa-Mola".center(80))
print("A animação só será fiel no intervalo de espaço de -46 até 46.".center(80))
print("="*80)

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

print("\nInsira os dados do sistema:")
m = get_float("Digite a massa do bloco (kg): ")  
k = get_float("Digite a constante elástica da mola (N/m): ")  
deslocamento_max = get_float("Digite o deslocamento máximo do bloco (m): ")
deslocamento_min = get_float("Digite o deslocamento mínimo do bloco (m): ")
v0 = get_float("Digite a velocidade inicial do bloco (m/s): ")
x0 = (deslocamento_max + deslocamento_min) / 2  

ground = box(pos=vector(0, -1, 0), size=vector(100, 1, 50), color=color.white)
wall = box(pos=vector(-47.5, 4, 0), size=vector(5, 10, 40), color=color.white)
cube = box(pos=vector(0 + x0, 3.5, 0), size=vector(8, 8, 8), color=color.red)
spring = helix(pos=wall.pos, axis=cube.pos - wall.pos, radius=2, coils=15, thickness=0.1, color=color.green)

graph1 = graph(title="Energia X Deslocamento", xtitle="Deslocamento (m)", ytitle="Energia (J)")
curva_cinetica = gcurve(color=color.blue, label="Energia Cinética", graph=graph1)
curva_elastica = gcurve(color=color.red, label="Energia Potencial Elástica", graph=graph1)
curva_mecanica = gcurve(color=color.black, label="Energia Mecânica Total", graph=graph1)

graph2 = graph(title="Trabalho Realizado pela Mola", xtitle="Tempo (s)", ytitle="Trabalho Acumulado (J)")
curva_trabalho = gcurve(color=color.cyan, label="Trabalho Total", graph=graph2)

graph3 = graph(title="Potência Instantânea", xtitle="Tempo (s)", ytitle="Potência (W)")
curva_potencia = gcurve(color=color.orange, label="Potência Instantânea", graph=graph3)


amplitude = abs(deslocamento_max - deslocamento_min) / 2  
omega = sqrt(k / m) 
fase_inicial = v0 / (amplitude * omega)  
t = 0
dt = 0.01
energia_cinetica_anterior = 0  
trabalho_total = 0  

while True:
    rate(100)  

    deslocamento = amplitude * cos(omega * t + fase_inicial)  
    velocidade = -amplitude * omega * sin(omega * t + fase_inicial)  
    
    cube.pos.x = x0 + deslocamento
    spring.axis = cube.pos - wall.pos
    
    energia_cinetica = 0.5 * m * velocidade**2  
    energia_p_elastica = 0.5 * k * deslocamento**2  
    energia_mec_total = energia_cinetica + energia_p_elastica

    if t > 0:
        trabalho_instantaneo = energia_cinetica - energia_cinetica_anterior
        trabalho_total += trabalho_instantaneo 


    forca = -k * deslocamento
    potencia_instantanea = forca * velocidade

    
    curva_cinetica.plot(x0 + deslocamento, energia_cinetica)
    curva_elastica.plot(x0 + deslocamento, energia_p_elastica)
    curva_mecanica.plot(x0 + deslocamento, energia_mec_total) 
    
    curva_trabalho.plot(t, trabalho_total)  
    curva_potencia.plot(t, potencia_instantanea)
    
    energia_cinetica_anterior = energia_cinetica 
    t += dt

from vpython import *

ground = box(pos=vector(0, -1, 0), size=vector(100, 1, 50), color=color.white)
wall = box(pos=vector(-47.5, 4, 0), size=vector(5, 10, 40), color=color.white)
cube = box(pos=vector(0 , 3.5, 0), size=vector(8, 8, 8), color=color.red)
spring = helix(pos=wall.pos, axis=cube.pos - wall.pos, radius=2, coils=15, thickness=0.1, color=color.yellow)

while True:
    pass
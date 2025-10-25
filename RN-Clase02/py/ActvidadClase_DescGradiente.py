import numpy as np
import grafica_Grad as gr
import math

for alfa in [0.05, 0.075, 0.1, 0.2]:
    MAX_ITE = 50
    error_max = 0.0001
    ite = 1
    z = 1
    x = 0 
    y = 0 
    z_new = (x-3)**2 + 0.5 * ((y-2)**4) + 5
    
    print(f"Descenso de Gradiente para alfa = {alfa}, error máximo = {error_max}")
    print("ite |   z         |         (x,y)            |   grad_x     |   grad_y   ")
    print("-" * 74) # Línea separadora
    while ((ite<MAX_ITE) and (math.fabs(z - z_new)>error_max)):
    # while (ite<MAX_ITE):
    
        z = z_new
        PtoAnt = [x, y, z]
        grad_x = 2*(x-3)   # derivada respecto de x
        grad_y = 2*(y-2)**3   # derivada respecto de y
    
        x = x - alfa * grad_x
        y = y - alfa * grad_y
        z_new = (x-3)**2 + 0.5 * ((y-2)**4) + 5
        
        # gr.graficarPaso(PtoAnt, [x, y, z_new], h)
        ite = ite + 1
        s_xy = f"({x:.5f}, {y:.5f})"
        print(f"{ite:>3} | {z_new:11.5f} | {s_xy:>24} | {grad_x:12.5f} | {grad_y:12.5f}")
        # print(f"{ite:>3} | {z_new:.5f} | ({x:.5f}, {y:.5f}) | {grad_x:.5f} | {grad_y:.5f}")


import grafica_Grad as gr
import math
# (2,3), (1,1), (-1,-3)
X = [2, 1, -1]
Y = [3, 1, -3]

[w0, w1, dibu] = gr.graficoGradientePy(4)

alfa = 0.1
MAX_ITE = 5000  
ite = 1
ECM_ant = 1
ECM = 2
E = (1/3)*((3-2*w1-w0)**2+(1-w1-w0)**2+(-3+w1-w0)**2)

while ((ite<MAX_ITE) and (math.fabs(ECM_ant - ECM)>0.0001)):
    ECM_ant = ECM
    suma = 0
    for p in range(len(X)):
        PtoAnt = [w0, w1, E]
        salida = w1 * X[p] + w0
        Error = Y[p]-salida
        
        grad_w0 = -2*Error
        grad_w1 = -2*Error*X[p]
    
        w0 = w0 - alfa * grad_w0
        w1 = w1 - alfa * grad_w1
        
        suma = suma + Error**2 
        
        # sólo para dibujar
        E = (1/3)*((3-2*w1-w0)**2+(1-w1-w0)**2+(-3+w1-w0)**2)
        gr.graficarPaso(PtoAnt, [w0, w1, E], dibu)
        
    # error cuadrático medio aproximado    
    ECM = suma / len(X)    
    ite = ite + 1
    print(f"ite = {ite:>3}    ECM = {ECM:.5f}")


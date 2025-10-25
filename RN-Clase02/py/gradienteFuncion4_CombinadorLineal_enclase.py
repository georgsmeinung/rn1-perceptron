import grafica_Grad as gr
import numpy as np

# (2,3), (1,1), (-1,-3)
X = [2, 1, -1]
T = [3, 1, -3]

[w0, w1, h] = gr.graficoGradientePy(4)

E = (1/3)*((3-2*w1-w0)**2+(1-w1-w0)**2+(-3+w1-w0)**2)

PtoAnt = [w0, w1, E]
w0 = w0 - 2
w1 = w1 + 4
E = (1/3)*((3-2*w1-w0)**2+(1-w1-w0)**2+(-3+w1-w0)**2)

gr.graficarPaso(PtoAnt, [w0, w1, E], h)

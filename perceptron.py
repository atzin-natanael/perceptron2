from tkinter import *
from tkinter import Tk, Frame, Button,ttk, messagebox, Label
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot
import numpy as np                 #PACHECO ARELLANO ATZIN NATANAEL
import matplotlib.pyplot as plt
from pylab import *
import random
Ventana =Tk()
Ventana.geometry('900x800')
Ventana.title('Grafica')
Ventana.minsize(width=850, height=750)
frame = Frame(Ventana, bg='blue')
frame.grid(column=0,row=0,sticky='nsew')
#Clasificar
#Puntos en la grafica, variables
xs = []
ys = []
y= []
x1=[]
cont=0
w=[]
deseado =[]
error= 0
learning= 0.3
colors = ['k']
#Ancho y largo del plano
xmin, xmax, ymin, ymax = -6, 6, -6, 6
f_cuadros = 1
#Grafica
fig, ax = plt.subplots(figsize=(9, 9))
canvas= FigureCanvasTkAgg(fig,master=frame)
def actualizar(value, d):
    if(value==1):
        ax.scatter(xs[d-1], ys[d-1], c="green")
    if (value == 2):
        ax.scatter(xs[d-1], ys[d-1], c="red")
#Escalar valores
ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect='equal')
#Mover la grafica a plano cartesiano
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
# X - Y valores en los ejes (nombre, tamaño, x, y , rotacion)
ax.set_xlabel('X', size=15, labelpad=-24, x=1.02)
ax.set_ylabel('Y', size=15, labelpad=-21, y=1.02, rotation=0)
# Crea determinados valores de cuadricula
x_cuadro = np.arange(xmin, xmax+1, f_cuadros)
y_cuadro = np.arange(ymin, ymax+1, f_cuadros)
ax.set_xticks(x_cuadro[x_cuadro != 0])
ax.set_yticks(y_cuadro[y_cuadro != 0])
#Cuadricula
ax.grid()
plt.subplots_adjust(bottom=0.2)
#Boton --- izquierda, abajo, ancho, altura
def func_error(theta):
    errores = True
    while errores:
        errores = False
        for i in range (len(xs)):
            z = (( w[0] * xs[i])+ (w[1] * ys[i]))- theta
            if z >= 0:
                z = 1
            else:
                z = 0
            if z != deseado[i]:
                errores=True
                error = (deseado[i]-z)
                theta = theta + (-(error* learning))
                #w[0] = w[0] + (learning * error * x1[i])
                w[0] = w[0]+ (learning* error*xs[i])
                w[1] = w[1]+(learning* error*ys[i])
    return w, theta
def paso1():
    w.append(random.random())
    w.append(random.random())
    #w.append(random.random())
    print("w: ", w)
def f(x, m, c):
    print(m)
    print(c)
    return m*x+c
def activacion():
    paso1()
    theta = 0.4
    func_error(theta)
    c = theta
    m = -w[0]
    g = range(-10, 10)
    pyplot.plot(g, [f(i, m,c) for i in g])
    plt.draw();
def clasificar():
    activacion()
boton = ttk.Button(text="Clasificar",command=clasificar)
boton.place(x=415, y=20)

def leftClick_event(event):
            #print('x: {} and y: {}'.format(event.xdata, event.ydata))
            #print('you pressed', event.button, event.xdata, event.ydata)
            if(event.button == MouseButton.LEFT):
                deseado.append(1)
                x1.append(1)
                xs.append(event.xdata);
                ys.append(event.ydata);
                actualizar(1, len(xs));
                plt.draw();
            if (event.button == MouseButton.RIGHT):
                x1.append(1)
                deseado.append(0)
                xs.append(event.xdata);
                ys.append(event.ydata);
                actualizar(2, len(xs));
                plt.draw();
cid = fig.canvas.mpl_connect('button_press_event', leftClick_event)
canvas.draw()
canvas.get_tk_widget().grid(column=0,row=0,rowspan=1)
try:
    Ventana.mainloop()
except KeyboardInterrupt:
       print("Programa finalizado correctamente")
       raise SystemExit
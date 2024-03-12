## Clases probadas en la Prueba3

import matplotlib.pyplot as plt ## Creación de gráficas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # Juntar matplotlib con las interfaces de Qt Designer
from matplotlib.animation import FuncAnimation #Animaciones de las gráficas

class Canvas_grafica(FigureCanvas):
    def __init__(self, figure=None):

        self.fig, self.ax = plt.subplots()  # Se crea la tabla
        super().__init__(self.fig)

    def test01(self, x_v, y_v):    # Se piden las variables de otra clase para poder trabajarlos.

        self.ax.grid()  # Asigna la cudarícula
        self.ax.set_ylim(0, 15)     # Inserta límites al eje Y 
        self.ax.set_xlim(0, 45)     # Inserta límites al eje X para los valores positivos

        line, = plt.plot(x_v, y_v, marker='o', linestyle='--', color='green')

        def animation(i):     # Función para realizar los frames de la animación
            x_data1 = []
            y_data1 = []
            x_data1.append(x_v[i])  # Inserta punto a punto los valores a las listas vacias.
            y_data1.append(y_v[i])
            line.set_xdata(x_data1)
            line.set_ydata(y_data1)
            return line,

        anim01 = FuncAnimation(self.fig, animation, interval=1000, frames=10, repeat=True)
        anim01.save('test001.gif')
        self.fig.canvas.draw()

class Canvas_grafica2(FigureCanvas):
    def __init__(self, figure=None):

        self.fig, self.ax = plt.subplots()  # Se crea la tabla
        super().__init__(self.fig)

    def test02(self, y_v, x_v):    # Se piden las variables de otra clase para poder trabajarlos.

        self.ax.grid()  # Asigna la cudarícula
        self.ax.set_ylim(0, 45)     # Inserta límites al eje Y 
        self.ax.set_xlim(0, 15)     # Inserta límites al eje X para los valores positivos

        line, = plt.plot(y_v, x_v, marker='>', linestyle='--', color='red')

        def animation2(i):     # Función para realizar los frames de la animación
            x_data2 = []
            y_data2 = []
            x_data2.append(y_v[i])  # Inserta punto a punto los valores a las listas vacias.
            y_data2.append(x_v[i])
            line.set_xdata(x_data2)
            line.set_ydata(y_data2)
            return line,

        anim02 = FuncAnimation(self.fig, animation2, interval=1000, frames=10, repeat=True)
        anim02.save('test002.gif')
        self.fig.canvas.draw()
#Agregando las flechas a la animación (Prueba exitosa)

import sys
from PyQt5 import uic, QtWidgets

import matplotlib.pyplot as plt ## Creación de gráficas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # Juntar matplotlib con las interfaces de Qt Designer
from matplotlib.animation import FuncAnimation #Animaciones de las gráficas

qtCreatorFile = "graficas.ui" # Nombre del archivo aquí. Relative Path

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #------------- NUEVAS APLICACIONES --------------------------------

        x = [5, 10, 15, 20, 5, 25, 30, 15, 20, 40]
        y = [2, 4, 6, 1, 5, 8, 10, 12, 4, 14]

        self.grafica1 = Canvas_grafica()
        self.graf01.addWidget(self.grafica1)
        self.grafica1.test01(x, y)

        self.grafica2 = Canvas_grafica2()       
        self.graf02.addWidget(self.grafica2)        
        self.grafica2.test02(y, x)
        

    #----------------- NUEVAS FUNCIONES -----------------------------------

class Canvas_grafica(FigureCanvas):
    def __init__(self, figure=None):

        self.fig, self.ax = plt.subplots()  # Se crea la tabla
        super().__init__(self.fig)

    def test01(self, x_v, y_v):    # Se piden las variables de otra clase para poder trabajarlos.

        self.ax.grid()  # Asigna la cudarícula
        self.ax.set_ylim(0, 15)     # Inserta límites al eje Y 
        self.ax.set_xlim(0, 45)     # Inserta límites al eje X para los valores positivos

        line, = plt.plot(x_v,y_v, marker='o', linestyle='--', color='green')

        def animation(i):     # Función para realizar los frames de la animación
            x_data1 = []
            y_data1 = []
            x_data1.append(x_v[i])  # Inserta punto a punto los valores a las listas vacias.
            y_data1.append(y_v[i])
            line.set_xdata(x_data1)
            line.set_ydata(y_data1)
            return line,

        Qr = self.ax.quiver(x_v, y_v, 10, 10, color= ['yellow'])   # Para la creación de flechas

        def animation02(i):     # Función para realizar los frames de la animación
            x_data3 = []
            y_data3 = []
            u = x_v[i] + i 
            v = y_v[i] + i 
            x_data3.append(x_v[i])  # Inserta punto a punto los valores a las listas vacias.
            y_data3.append(y_v[i])
            Qr.set_UVC(u, v)
            return Qr,

        anim01 = FuncAnimation(self.fig, animation, interval=1000, frames=10, repeat=True)
        anim001 = FuncAnimation(self.fig, animation02, interval=1000, frames=10, repeat=True)
        anim01.save('test01.gif')
        anim001.save('test001.gif')
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
        anim02.save('test02.gif')
        self.fig.canvas.draw()

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
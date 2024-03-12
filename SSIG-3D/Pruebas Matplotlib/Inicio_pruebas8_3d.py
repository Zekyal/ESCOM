## Graficar en 3d aplicado a la interafaz, con animación. (Prueba exitosa)
## Son dos maneras diferenets de hacer la animación.

import sys
from PyQt5 import uic, QtWidgets

import matplotlib.pyplot as plt ## Creación de gráficas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # Juntar matplotlib con las interfaces de Qt Designer
from matplotlib.animation import FuncAnimation #Animaciones de las gráficas
from mpl_toolkits import mplot3d

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
        z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

        self.grafica1 = Canvas_grafica()
        self.graf01.addWidget(self.grafica1)
        self.grafica1.test01(x, y, z)

        self.grafica2 = Canvas_grafica2()       
        self.graf02.addWidget(self.grafica2)        
        self.grafica2.test02(y, x, z)
        

    #----------------- NUEVAS FUNCIONES -----------------------------------

class Canvas_grafica(FigureCanvas):
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    def test01(self, x_v, y_v, z_v):    # Solo mostramos un punto de la lista
        x_data = []      
        y_data = []  
        z_data = []  

        line, = self.ax.plot(0, 0, 0, marker='o') 

        self.ax.set_xlim(0, max(x_v))
        self.ax.set_ylim(0, max(y_v))
        self.ax.set_zlim(0, 10)

        def animation(i):     # Función para realizar los frames de la animación
            x_data.clear()
            y_data.clear()
            z_data.clear()

            x_data.append(x_v[i])
            y_data.append(y_v[i])
            z_data.append(z_v[i])

            #graph._offsets3d(x_v[i], y_v[i], z_v[i])
            line.set_data(x_data, y_data)   # Actualiza las posiciones de x, y
            line.set_3d_properties(z_data)  # Actualiza las posiciones de z
            
            return line,
            
        anim01 = FuncAnimation(self.fig, func = animation, interval=1000, frames=10,  repeat=True)
        anim01.save('test01.gif')
        self.fig.canvas.draw()


class Canvas_grafica2(FigureCanvas):
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    def test02(self, y_v, x_v, z_v):    # Mostramos un rango de puntos de las listas
        
        self.ax.set_xlim(0, max(y_v))
        self.ax.set_ylim(0, max(x_v))
        self.ax.set_zlim(0, 10)

        line, = self.ax.plot(0, 0, 0, marker='o')

        def animation2(i):     # Función para realizar los frames de la animación

            line.set_data(y_v[:i], x_v[:i])
            line.set_3d_properties(z_v[:i])
            
            return line,

        anim02 = FuncAnimation(self.fig, func = animation2, interval=1000, frames=10,  repeat=True)
        anim02.save('test02.gif')
        self.fig.canvas.draw()


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
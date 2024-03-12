## Graficar en 3d quivers aplicado a la interfaz.

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
        z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 

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
        self.ax = plt.axes(projection="3d", xlim=20, ylim=20, zlim=20)
        super().__init__(self.fig)

    def test01(self, x_v, y_v, z_v):
        self.ax.quiver(x_v, y_v, z_v, 10, 10, 10, color='red')


class Canvas_grafica2(FigureCanvas):
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    def test02(self, y_v, x_v, z_v):    

        self.ax.scatter(y_v, x_v, z_v, color='green')

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
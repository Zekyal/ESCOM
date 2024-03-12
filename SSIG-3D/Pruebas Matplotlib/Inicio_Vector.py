# Probando como agregar la función de vector con una interfaz

import sys
from PyQt5 import uic, QtWidgets
import numpy as np
import Vector as v

import matplotlib.pyplot as plt ## Creación de gráficas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # Juntar matplotlib con las interfaces de Qt Designer

qtCreatorFile = "graficas.ui" # Nombre del archivo aquí. Relative Path

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #------------- NUEVAS APLICACIONES --------------------------------

        self.Vector1 = Vector()
        self.graf01.addWidget(self.Vector1)
        self.Vector1.vector01()
        
    #----------------- NUEVAS FUNCIONES -----------------------------------

    #///////////// Creando los vectores ////////////////////#

class Vector(FigureCanvas):
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    def vector01(self):

        a = np.array([2, 3, 1])
        b = np.array([0, 5, 4])

        colors = ['red', 'green', 'blue', 'orange', 'violet']

        vectorList = {
            "a" : a,
            "b" : b
        }

        vector = list(vectorList.values())

        # Prueba de Funcion Add
        resultado = vector[0]

        compVectors = 0

        for x in range(1, len(vectorList)):
            resultado = v.Subtract(resultado, vector[x])
            
        vectorList["resultado"] = resultado

        print(vectorList)

        self.fig.set_figwidth(7.5)   # Ancho de la pantalla
        self.fig.set_figheight(6.5)  # Altura de la pantalla
        
        # Configuracion de los ejes que se mostraran en la Grafica
        # Etiquetas para cada eje
        self.ax.xaxis.set_label_text('x', color = 'b')
        self.ax.yaxis.set_label_text('y', color = 'b')
        self.ax.zaxis.set_label_text('z', color = 'b')
        
        vector = list(vectorList.values())
        labels = list(vectorList.keys())

        # Se establece como valor inicial de los limites de cada eje, el primer punto de cada eje
        # de la Grafica, enlistado en la lista de Vectores
        max_axis_x = min_axis_x = vector[0][0]
        max_axis_y = min_axis_y = vector[0][1]
        max_axis_z = min_axis_z = vector[0][2]
        
        # Se obtienen los puntos maximos y minimos de cada eje de la Grafica, recorriendo cada uno
        # de los ejes enlistados en la lista de Vectores
        for x in range(1, len(vector)):
            max_axis_x = max(max_axis_x, vector[x][0])
            max_axis_y = max(max_axis_y, vector[x][1])
            max_axis_z = max(max_axis_z, vector[x][2])
            min_axis_x = min(min_axis_x, vector[x][0])
            min_axis_y = min(min_axis_y, vector[x][1])
            min_axis_z = min(min_axis_z, vector[x][2])
        
        # En caso de que el minimo sea un num positivo, se reduce a 0, para que asi las lineas siempre
        # se grafiquen desde el eje 0
        min_axis_x = min(min_axis_x, 0)
        min_axis_y = min(min_axis_y, 0)
        min_axis_z = min(min_axis_z, 0)
        
        # Establecimiento de los limites de cada eje (Punto max y min de cada eje de la Grafica
        # que sera mostrada al momento de esta ejecutarse, y sin aplicar zoom)
        print(self.ax.set_xlim([min_axis_x, max_axis_x]))
        print(self.ax.set_ylim([min_axis_y, max_axis_y]))
        print(self.ax.set_zlim([min_axis_z, max_axis_z]))
        
        # Definicion de los ejes x, y, z que se marcaran para definir la grafica
        self.ax.plot((min_axis_x, max_axis_x), (0, 0), (0, 0), color="grey")
        self.ax.plot((0, 0), (min_axis_y, max_axis_y), color="grey")
        self.ax.plot((0, 0), (0, 0), (min_axis_z, max_axis_z), color="grey") 

        for x in range(len(vector)):
            self.ax.quiver(0, 0, 0, vector[x][0], vector[x][1], vector[x][2], color = colors[x], label = labels[x], arrow_length_ratio=0.1)
    
        ## GRAFICACION DE VECTORES COMPLEMENTARIOS PARA LA SUMA DE VECTORES
        if compVectors == 1:
            init_x = vector[0][0]
            init_y = vector[0][1]
            init_z = vector[0][2]
            
            for x in range(len(vector) - 2):
                end_x = vector[x + 1][0]
                end_y = vector[x + 1][1]
                end_z = vector[x + 1][2]
                
                self.ax.quiver(init_x, init_y, init_z, end_x, end_y, end_z, color = colors[x+1], label = labels[x+1] + "*", arrow_length_ratio=0.1, linestyle = '--')
                
                init_x = init_x + end_x
                init_y = init_y + end_y
                init_z = init_z + end_z
        
        # Impresion de la Leyenda
        plt.legend()
        

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
import sys
from PyQt5 import uic, QtWidgets
from Grafica_Practica13 import Angulo_solido
import numpy as np

qtCreatorFile = "Practica13.ui" # Nombre del archivo aquí. Relative Path

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #------------- NUEVAS APLICACIONES --------------------------------

        global lineFra
        lineFra = self.line_fraction

        self.button_cerrar.clicked.connect(self.cerrarVentana)   # Función del botón cerrar.
        self.button_simular.clicked.connect(self.simularAngulo)

        # Mostrando una gráfica de prueba
        self.graficaSolido = Angulo_solido()   # Creamos un Canvas para cada una de las gráficas.
        self.graf_ang_solid.addWidget(self.graficaSolido)     #Agregamos la gráfica al widget.
        self.graficaSolido.graficar_muestra(lineFra)   # Trabajamos con la gráfica
        

    #----------------- NUEVAS FUNCIONES -----------------------------------

    #-------- Función de cerrar-------------------------------------------------
    def cerrarVentana(self):  
        quit()
    #-------- Función de cerrar (FIN) -------------------------------------------

    def simularAngulo(self):
        self.graficaSolido.vaciar_grafica()    #Eliminamos los plt y axes existentes.   
        self.graf_ang_solid.removeWidget(self.graficaSolido)    # Eliminamos el widget creado anterioremente
        self.graficaSolido.deleteLater()
        self.graficaSolido = None

        theta_cone = float(self.sBox_thetha.text())

        self.graficaSolido = Angulo_solido()   # Creamos un Canvas para cada una de las gráficas.
        self.graf_ang_solid.addWidget(self.graficaSolido)     #Agregamos la gráfica al widget.
        self.graficaSolido.graficarAnguloSolido(np.deg2rad(theta_cone), lineFra)


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
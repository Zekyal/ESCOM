import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from Grafica_Practica13 import Angulo_solido
import numpy as np

class Prac13(QMainWindow):
    def __init__(self, parent=None):
        super(Prac13, self).__init__(parent)
        loadUi('Interfaces\Practica13.ui', self)

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
        self.parent().show()
        self.close()
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
    window = Prac13()
    window.show()
    sys.exit(app.exec_())
# Práctica 20. Ley de Gauss (SSIS-3D)

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
import numpy as np

from Grafica_Practica20 import Ley_Gauss

class Prac20(QMainWindow):
    def __init__(self, parent=None):
        super(Prac20, self).__init__(parent)
        loadUi('Interfaces\Practica20.ui', self)

        #------------- NUEVAS APLICACIONES --------------------------------

        global valor
        valor = self.line_valor

        self.button_cerrar.clicked.connect(self.cerrarVentana)      # Función del botón cerrar.
        self.button_simular.clicked.connect(self.simularGauss)

    #----------------- NUEVAS FUNCIONES -----------------------------------

    #-------- Función de cerrar----------------------------------------------
    def cerrarVentana(self):  
        if hasattr(self, 'graficaGauss'):
            self.graficaGauss.cerrarGraf()
        self.parent().show()
        self.close()

    def simularGauss(self):
        if hasattr(self, 'graficaGauss'):
            self.graficaGauss.vaciar_grafica()    #Eliminamos los plt y axes existentes.   
            self.graf_gauss.removeWidget(self.graficaGauss)    # Eliminamos el widget creado anterioremente
            self.graficaGauss.deleteLater()
            self.graficaGauss = None

        # Asignamos los valores insertados.
        theta_cone = float(self.sBox_grados.text())

        # Mostrando Ley de Gauss
        self.graficaGauss = Ley_Gauss()   
        self.graf_gauss.addWidget(self.graficaGauss)
        self.graficaGauss.graficar_gauss(np.deg2rad(theta_cone), valor)


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = Prac20()
    window.show()
    sys.exit(app.exec_())
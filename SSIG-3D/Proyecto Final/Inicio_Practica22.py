# Práctica 22. Ángulo Sólido sobre un Elipsoide (SSIS-3D)

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
import numpy as np

from Graficas_Practica22 import Angulo_Solido

class Prac22(QMainWindow):
    def __init__(self, parent=None):
        super(Prac22, self).__init__(parent)
        loadUi('Interfaces\Practica22.ui', self)

        #------------- NUEVAS APLICACIONES --------------------------------

        global valor
        valor = self.line_valor

        self.button_cerrar.clicked.connect(self.cerrarVentana)      # Función del botón cerrar.
        self.button_simular.clicked.connect(self.simularGauss)

    #----------------- NUEVAS FUNCIONES -----------------------------------

    #-------- Función de cerrar----------------------------------------------
    def cerrarVentana(self):  
        if hasattr(self, 'graficaSolido'):
            self.graficaSolido.cerrarGraf()
        self.parent().show()
        self.close()
    #-------- Función de cerrar (FIN) ---------------------------------------

    def simularGauss(self):
        if hasattr(self, 'graficaSolido'):
            self.graficaSolido.vaciar_grafica()    #Eliminamos los plt y axes existentes.   
            self.graf_Solido.removeWidget(self.graficaSolido)    # Eliminamos el widget creado anterioremente
            self.graficaSolido.deleteLater()
            self.graficaSolido = None

        # Asignamos los valores insertados.
        theta_cone = float(self.sBox_grados.text())

        # Mostrando Ley de Gauss
        self.graficaSolido = Angulo_Solido()   
        self.graf_Solido.addWidget(self.graficaSolido)
        self.graficaSolido.graficar_solido(np.deg2rad(theta_cone), valor)


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = Prac22()
    window.show()
    sys.exit(app.exec_())
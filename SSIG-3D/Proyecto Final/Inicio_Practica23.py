# Práctica 23. Sistema de Referencia Inercial y No Inercial. (SSIS-3D)

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
import numpy as np

from Grafica_Practica23 import Inercial

class Prac23(QMainWindow):
    def __init__(self, parent=None):
        super(Prac23, self).__init__(parent)
        loadUi('Interfaces\Practica23.ui', self)

        #------------- NUEVAS APLICACIONES --------------------------------

        self.button_cerrar.clicked.connect(self.cerrarVentana)      # Función del botón cerrar.
        
        # Mostrando Sistema Inercial y no Inercial
        self.graficaInercial = Inercial()   
        self.graf_inercial.addWidget(self.graficaInercial)
        self.graficaInercial.graficar_inercial()

    #----------------- NUEVAS FUNCIONES -----------------------------------

    #-------- Función de cerrar----------------------------------------------
    def cerrarVentana(self):  
        if hasattr(self, 'graficaInercial'):
            self.graficaInercial.cerrarGraf()
        self.parent().show()
        self.close()
    #-------- Función de cerrar (FIN) ---------------------------------------

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = Prac23()
    window.show()
    sys.exit(app.exec_())
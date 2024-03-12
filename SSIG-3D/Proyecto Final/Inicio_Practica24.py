# Práctica 24. Diagrama de Cuerpo Libre. (SSIS-3D)

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl
import numpy as np

from Grafica_Practica24 import Dia_Cuerpo_Libre

class Prac24(QMainWindow):
    def __init__(self, parent=None):
        super(Prac24, self).__init__(parent)
        loadUi('Interfaces\Practica24.ui', self)

        #------------- NUEVAS APLICACIONES --------------------------------

        self.button_cerrar.clicked.connect(self.cerrarVentana)      # Función del botón cerrar.
        self.button_simular.clicked.connect(self.simularDia)
        self.link_dia.clicked.connect(self.abrir_pagina)

    #----------------- NUEVAS FUNCIONES -----------------------------------

    #-------- Función de cerrar----------------------------------------------
    def cerrarVentana(self):  
        if hasattr(self, 'graficaCLibre'):
            self.graficaCLibre.cerrarGraf()
        self.parent().show()
        self.close()
    #-------- Función de cerrar (FIN) ---------------------------------------

    def simularDia(self):
        if hasattr(self, 'graficaCLibre'):
            self.graficaCLibre.vaciar_grafica()    #Eliminamos los plt y axes existentes.   
            self.graf_dia.removeWidget(self.graficaCLibre)    # Eliminamos el widget creado anterioremente
            self.graficaCLibre.deleteLater()
            self.graficaCLibre = None

        # Asignamos los valores insertados.
        theta = float(self.sBox_theta.text())
        alpha = float(self.sBox_alpha.text())
        magnitude = float(self.sBox_magnitude.text())
        m = float(self.sBox_m.text())
        mk = float(self.sBox_mk.text())
        ms = float(self.sBox_ms.text())

        # Mostrando Diagrama de Cuerpo Libre
        self.graficaCLibre = Dia_Cuerpo_Libre()   
        self.graf_dia.addWidget(self.graficaCLibre)
        self.graficaCLibre.graficar_diagrama(np.deg2rad(theta), np.deg2rad(alpha), magnitude, m, mk, ms)

    #-------- Función de abrir una página web -------------------------------------------------------------------------
    def abrir_pagina(self):
        link = QUrl("https://acortar.link/cV9a0T") # Link  de la página de Youtube
        QDesktopServices.openUrl(QUrl(link))    # Abre la página en el navegador.
    #-------- Función de abrir una página web (FIN) -------------------------------------------------------------------


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = Prac24()
    window.show()
    sys.exit(app.exec_())
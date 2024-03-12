# Práctica 09. 2da Ley de Newton: Dinámica. (SSIS-3D)

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
import numpy as np

from Graficas_Practica09 import ley_dinamica

class Prac09(QMainWindow):
    def __init__(self, parent=None):
        super(Prac09, self).__init__(parent)
        loadUi('Interfaces\Practica09.ui', self)

        #------------- NUEVAS APLICACIONES --------------------------------
        self.frame_8.hide()
        self.frame_10.hide()

        self.button_cerrar.clicked.connect(self.cerrarVentana)      # Función del botón cerrar.
        self.button_grafica01.clicked.connect(self.primeraGrafica)     
        self.button_si.clicked.connect(self.graficaMovimientoSi)    
        self.button_no.clicked.connect(self.graficaMovimientoNo)    

    #----------------- NUEVAS FUNCIONES -----------------------------------

    #-------- Función de cerrar----------------------------------------------
    def cerrarVentana(self):  
        if hasattr(self, 'graficaMov'):
            self.graficaMov.cerrarGraf()
        if hasattr(self, 'graficaNor'):
            self.graficaNor.cerrarGraf()
        self.parent().show()
        self.close()
    #-------- Función de cerrar (FIN) ---------------------------------------

    def primeraGrafica(self):
        self.button_grafica01.setEnabled(False)
        self.frame_8.show()
        global thetha, Ms, Mk, thetha_v, x, y, thethaO, acx, t
        thetha = float(self.sBox_thetha.text())
        Ms = float(self.sBox_Ms.text())

        thetha_v = np.deg2rad(thetha)
        l = 50  # Largo 
        g = -9.81
        Mk = 0.7*Ms
        t = 4

        x = l*np.cos(thetha_v)
        y = l*np.sin(thetha_v)
        acx = g*(Mk*np.cos(thetha_v)- np.sin(thetha_v))
        thethaO = np.arctan(Ms)

        self.graficaNor = ley_dinamica()   # Creamos un Canvas para cada una de las gráficas.
        self.frame_grafica01.addWidget(self.graficaNor)     #Agregamos la gráfica al widget.
        self.graficaNor.graficaNormal(thetha_v, x, y, acx, t)   # Trabajamos con la gráfica

    def graficaMovimientoSi(self):
        self.button_si.setEnabled(False)
        self.button_no.setEnabled(False)
        self.frame_10.show()

        self.graficaMov = ley_dinamica()   # Creamos un Canvas para cada una de las gráficas.
        self.frame_grafica02.addWidget(self.graficaMov)     #Agregamos la gráfica al widget.
        self.graficaMov.graficaMovimiento(thetha, thethaO, thetha_v, x, y, acx, t)   # Trabajamos con la gráfica

        if (thetha > np.degrees(thethaO)):
            self.label_respuesta.setText("Respuesta Correcta, el objeto se puede mover")
        else: 
            self.label_respuesta.setText("Respuesta Incorrecta, el objeto no se puede mover")

        self.label_thetha.setText("θ = " + str(thetha))
        self.label_thetha0.setText("θo = " + str(np.degrees(thethaO)))

    def graficaMovimientoNo(self):
        self.button_si.setEnabled(False)
        self.button_no.setEnabled(False)
        self.frame_10.show()

        self.graficaMov = ley_dinamica()   # Creamos un Canvas para cada una de las gráficas.
        self.frame_grafica02.addWidget(self.graficaMov)     #Agregamos la gráfica al widget.
        self.graficaMov.graficaMovimiento(thetha, thethaO, thetha_v, x, y, acx, t)   # Trabajamos con la gráfica

        if (thetha > np.degrees(thethaO)):
            self.label_respuesta.setText("Respuesta Incorrecta, el objeto se puede mover")
        else: 
            self.label_respuesta.setText("Respuesta Correcta, el objeto no se puede mover")

        self.label_thetha.setText("θ = " + str(thetha))
        self.label_thetha0.setText("θo = " + str(np.degrees(thethaO)))

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = Prac09()
    window.show()
    sys.exit(app.exec_())
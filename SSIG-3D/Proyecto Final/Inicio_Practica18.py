# Práctica 18. Cargas Puntuales (SSIS-3D)   (quitar repetida)

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl

from Graficas_Practica18 import Camp_Elec_Coulumb, Camp_Elec_Flujos

class Prac18(QMainWindow):
    def __init__(self, parent=None):
        super(Prac18, self).__init__(parent)
        loadUi('Interfaces\Practica18.ui', self)

        #------------- NUEVAS APLICACIONES --------------------------------

        self.button_p1.hide()

        self.button_cerrar.clicked.connect(self.cerrarVentana)      # Función del botón cerrar.
        self.button_p1.clicked.connect(self.mostrarGraf1) 
        self.button_p2.clicked.connect(self.mostrarGraf2) 
        self.link_camp_elec.clicked.connect(self.abrir_pagina)


        # Mostrando simulaciones
        self.graficaEleCo = Camp_Elec_Coulumb()   # Creamos un Canvas para cada una de las gráficas.
        self.graf_coulumb.addWidget(self.graficaEleCo)     #Agregamos la gráfica al widget.
        self.graficaEleCo.graficar_muestra()   # Trabajamos con la gráfica

        self.graficaEleFl = Camp_Elec_Flujos()   # Creamos un Canvas para cada una de las gráficas.
        self.graf_flujos.addWidget(self.graficaEleFl)     #Agregamos la gráfica al widget.
        self.graficaEleFl.graficar_muestra()   # Trabajamos con la gráfica


    #----------------- NUEVAS FUNCIONES -----------------------------------

    #-------- Función de cerrar----------------------------------------------
    def cerrarVentana(self):  
        self.graficaEleCo.cerrarGraf()
        self.graficaEleFl.cerrarGraf()
        self.parent().show()
        self.close()
    #-------- Función de cerrar (FIN) ---------------------------------------

    #-------- Función de abrir una página web -------------------------------------------------------------------------
    def abrir_pagina(self):
        link = QUrl("https://acortar.link/4CW3O") # Link  de la página de Khan Academy
        QDesktopServices.openUrl(QUrl(link))    # Abre la página en el navegador.
    #-------- Función de abrir una página web (FIN) -------------------------------------------------------------------

    def mostrarGraf1(self):
        self.button_p1.hide()
        self.button_p2.show()
        self.stackedWidget.setCurrentWidget(self.ley_Coulumb)

    def mostrarGraf2(self):
        self.button_p1.show()
        self.button_p2.hide()
        self.stackedWidget.setCurrentWidget(self.flujo_elec)

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = Prac18()
    window.show()
    sys.exit(app.exec_())
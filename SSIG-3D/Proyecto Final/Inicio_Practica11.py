# Práctica 11. Esfera Conductora. (SSIS-3D)

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from Graficas_Practica11 import Esfera_Conductora

import Errores

class Prac11(QMainWindow):
    def __init__(self, parent=None):
        super(Prac11, self).__init__(parent)
        loadUi('Interfaces\Practica11.ui', self)

        #------------- NUEVAS APLICACIONES --------------------------------

        self.button_cerrar.clicked.connect(self.cerrarVentana)      # Función del botón cerrar.
        self.button_simular.clicked.connect(self.simularEsfera)

        # Mostrando una gráfica de prueba
        self.graficaEsfera = Esfera_Conductora()   # Creamos un Canvas para cada una de las gráficas.
        self.graf_esfera.addWidget(self.graficaEsfera)     #Agregamos la gráfica al widget.
        self.graficaEsfera.graficar_esfera_muestra()   # Trabajamos con la gráfica
        
    #----------------- NUEVAS FUNCIONES -----------------------------------

    #-------- Función de cerrar----------------------------------------------
    def cerrarVentana(self):  
        if hasattr(self, 'graficaEsfera'):
            self.graficaEsfera.cerrarGraf()
        self.parent().show()
        self.close()
    #-------- Función de cerrar (FIN) ---------------------------------------

    def simularEsfera(self):
        q = float(self.sBox_q.text())
        d = float(self.sBox_d.text())

        if (q == 0):
            Errores.Error_Carga(self)
        else:
            self.graficaEsfera.vaciar_grafica()    #Eliminamos los plt y axes existentes.   
            self.graf_esfera.removeWidget(self.graficaEsfera)    # Eliminamos el widget creado anterioremente
            self.graficaEsfera.deleteLater()
            self.graficaEsfera = None

            self.graficaEsfera = Esfera_Conductora()   # Creamos un Canvas para cada una de las gráficas.
            self.graf_esfera.addWidget(self.graficaEsfera)     #Agregamos la gráfica al widget.
            self.graficaEsfera.graficar_esfera(q, d)   # Trabajamos con la gráfica

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = Prac11()
    window.show()
    sys.exit(app.exec_())
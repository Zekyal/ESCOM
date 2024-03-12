# Práctica 15. Tiro Parabólico (Altura y Distancia de Impacto) (SSIS-3D)

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

from Grafica_Practica15 import Tiro_Parabolico

class Prac15(QMainWindow):
    def __init__(self, parent=None):
        super(Prac15, self).__init__(parent)
        loadUi('Interfaces\Practica15.ui', self)

        #------------- NUEVAS APLICACIONES --------------------------------

        self.button_cerrar.clicked.connect(self.cerrarVentana)      # Función del botón cerrar.
        self.button_simular.clicked.connect(self.simularTiro)

    #----------------- NUEVAS FUNCIONES -----------------------------------

    #-------- Función de cerrar----------------------------------------------
    def cerrarVentana(self):  
        if hasattr(self, 'graficaPar'):
            self.graficaPar.cerrarGraf()
        self.parent().show()
        self.close()
    #-------- Función de cerrar (FIN) ---------------------------------------

    def simularTiro(self):
        
        if hasattr(self, 'graficaPar'):
            self.graficaPar.vaciar_grafica()    #Eliminamos los plt y axes existentes.   
            self.graf_tiro.removeWidget(self.graficaPar)    # Eliminamos el widget creado anterioremente
            self.graficaPar.deleteLater()
            self.graficaPar = None

        Xo = float(self.sBox_Xo.text())
        Yo = float(self.sBox_Yo.text())
        Zo = float(self.sBox_Zo.text())
        Vox = float(self.sBox_Vox.text())
        Voy = float(self.sBox_Voy.text())
        Voz = float(self.sBox_Voz.text())

        # Mostrando una gráfica de prueba
        self.graficaPar = Tiro_Parabolico()   # Creamos un Canvas para cada una de las gráficas.
        self.graf_tiro.addWidget(self.graficaPar)     #Agregamos la gráfica al widget.
        self.graficaPar.graficarTiroPar(Xo, Yo, Zo, Vox, Voy, Voz)   # Trabajamos con la gráfica

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = Prac15()
    window.show()
    sys.exit(app.exec_())
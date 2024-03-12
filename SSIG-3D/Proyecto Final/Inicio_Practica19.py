# Práctica 19. Coordenadas Esféricas (SSIS-3D)  (quitar repetida)

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

from Grafica_Practica19 import Coordenadas_Esfericas
import Errores

class Prac19(QMainWindow):
    def __init__(self, parent=None):
        super(Prac19, self).__init__(parent)
        loadUi('Interfaces\Practica19.ui', self)

        #------------- NUEVAS APLICACIONES --------------------------------

        self.button_cerrar.clicked.connect(self.cerrarVentana)      # Función del botón cerrar.
        self.button_simular.clicked.connect(self.simularEsfericas)

        # Mostrando una Coor. Esférica de muestra
        self.graficaEsfe = Coordenadas_Esfericas()    
        self.graf_esfe.addWidget(self.graficaEsfe)
        self.graficaEsfe.graficar_coor_esfe_muestra()

    #----------------- NUEVAS FUNCIONES -----------------------------------

    #-------- Función de cerrar----------------------------------------------
    def cerrarVentana(self):  
        if hasattr(self, 'graficaEsfe'):
            self.graficaEsfe.cerrarGraf()
        self.parent().show()
        self.close()
    #-------- Función de cerrar (FIN) ---------------------------------------

    def simularEsfericas(self):
        # Asignamos los valores insertados.
        x = float(self.sBox_X.text())        
        y = float(self.sBox_Y.text())
        z = float(self.sBox_Z.text())

        if (x == 0 and y == 0 and z == 0):
            Errores.Error_Coordenadas_valores(self)
        else:
            self.graficaEsfe.vaciar_grafica()    #Eliminamos los plt y axes existentes.   
            self.graf_esfe.removeWidget(self.graficaEsfe)    # Eliminamos el widget creado anterioremente
            self.graficaEsfe.deleteLater()
            self.graficaEsfe = None
            
            self.graficaEsfe = Coordenadas_Esfericas()
            self.graf_esfe.addWidget(self.graficaEsfe)
            self.graficaEsfe.graficar_coor_esfe(x, y, z)


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = Prac19()
    window.show()
    sys.exit(app.exec_())
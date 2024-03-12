# Práctica 16. Tiro Parabólico Porcentaje de Distancia de Impacto (SSIS-3D)

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from Grafica_Practica16 import Tiro_Parabolico

import Errores

class Prac16(QMainWindow):
    def __init__(self, parent=None):
        super(Prac16, self).__init__(parent)
        loadUi('Interfaces\Practica16.ui', self)

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

        Vox = float(self.sBox_Vox.text())
        Voy = float(self.sBox_Voy.text())
        Voz = float(self.sBox_Voz.text())
        pord = float(self.sBox_pord.text())

        if((Vox == 0) or (Voy == 0) or (Voz == 0)):
            Errores.Error_Velocidades_Tiro_Par(self)
        else:
            if hasattr(self, 'graficaPar'):
                self.graficaPar.vaciar_grafica()    #Eliminamos los plt y axes existentes.   
                self.graf_tiro.removeWidget(self.graficaPar)    # Eliminamos el widget creado anterioremente
                self.graficaPar.deleteLater()
                self.graficaPar = None
            # Mostrando una gráfica de prueba
            self.graficaPar = Tiro_Parabolico()   # Creamos un Canvas para cada una de las gráficas.
            self.graf_tiro.addWidget(self.graficaPar)     #Agregamos la gráfica al widget.
            self.graficaPar.graficarTiroPar(Vox, Voy, Voz, pord)   # Trabajamos con la gráfica


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = Prac16()
    window.show()
    sys.exit(app.exec_())
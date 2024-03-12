# Práctica 14. Tiro con Rifle (SSIS-3D)

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from Grafica_Practica14 import Tiro_Rifle

class Prac14(QMainWindow):
    def __init__(self, parent=None):
        super(Prac14, self).__init__(parent)
        loadUi('Interfaces\Practica14.ui', self)

        #------------- NUEVAS APLICACIONES --------------------------------

        global v_vox, v_voy, v_voz, v_gamma, v_betha, v_alpha

        v_vox = self.lcd_vox
        v_voy = self.lcd_voy
        v_voz = self.lcd_voz
        v_gamma = self.lcd_gamma
        v_betha = self.lcd_betha
        v_alpha = self.lcd_alpha

        self.button_cerrar.clicked.connect(self.cerrarVentana)      # Función del botón cerrar.
        self.button_tirar.clicked.connect(self.simularTiro)

    #----------------- NUEVAS FUNCIONES -----------------------------------

    #-------- Función de cerrar----------------------------------------------
    def cerrarVentana(self):  
        if hasattr(self, 'graficaRifle'):
            self.graficaRifle.cerrarGraf()
        self.parent().show()
        self.close()
    #-------- Función de cerrar (FIN) ---------------------------------------

    def simularTiro(self):

        if hasattr(self, 'graficaRifle'):
            self.graficaRifle.vaciar_grafica()    #Eliminamos los plt y axes existentes.   
            self.graf_tiro.removeWidget(self.graficaRifle)    # Eliminamos el widget creado anterioremente
            self.graficaRifle.deleteLater()
            self.graficaRifle = None

        zinit = float(self.sBox_zinit.text())
        vo = float(self.sBox_vo.text())
        xf = float(self.sBox_xf.text())
        yf = float(self.sBox_yf.text())
        zobj = float(self.sBox_zf.text())

        # Mostrando una gráfica de prueba
        self.graficaRifle = Tiro_Rifle()   # Creamos un Canvas para cada una de las gráficas.
        self.graf_tiro.addWidget(self.graficaRifle)     #Agregamos la gráfica al widget.
        self.graficaRifle.graficarTiroRifle(zinit, xf, yf, zobj, v_vox, v_voy, v_voz, v_gamma, v_betha, v_alpha, vo)   # Trabajamos con la gráfica


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = Prac14()
    window.show()
    sys.exit(app.exec_())
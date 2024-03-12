import sys
from PyQt5 import uic, QtWidgets
from Grafica_Practica14 import Tiro_Rifle

qtCreatorFile = "Practica14.ui" # Nombre del archivo aquí. Relative Path

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

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

        # Mostrando una gráfica de prueba
        self.graficaRifle = Tiro_Rifle()   # Creamos un Canvas para cada una de las gráficas.
        self.graf_tiro.addWidget(self.graficaRifle)     #Agregamos la gráfica al widget.
        self.graficaRifle.graficar_muestra(v_vox, v_voy, v_voz, v_gamma, v_betha, v_alpha)   # Trabajamos con la gráfica
        

    #----------------- NUEVAS FUNCIONES -----------------------------------

    #-------- Función de cerrar----------------------------------------------
    def cerrarVentana(self):  
        quit()
    #-------- Función de cerrar (FIN) ---------------------------------------

    def simularTiro(self):

        self.graficaRifle.vaciar_grafica()    #Eliminamos los plt y axes existentes.   
        self.graf_tiro.removeWidget(self.graficaRifle)    # Eliminamos el widget creado anterioremente
        self.graficaRifle.deleteLater()
        self.graficaRifle = None

        zinit = float(self.sBox_zinit.text())
        xf = float(self.sBox_xf.text())
        yf = float(self.sBox_yf.text())
        zobj = float(self.sBox_zf.text())

        # Mostrando una gráfica de prueba
        self.graficaRifle = Tiro_Rifle()   # Creamos un Canvas para cada una de las gráficas.
        self.graf_tiro.addWidget(self.graficaRifle)     #Agregamos la gráfica al widget.
        self.graficaRifle.graficarTiroRifle(zinit, xf, yf, zobj, v_vox, v_voy, v_voz, v_gamma, v_betha, v_alpha)   # Trabajamos con la gráfica


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
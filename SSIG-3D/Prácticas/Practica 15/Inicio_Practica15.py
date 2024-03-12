import sys
from PyQt5 import uic, QtWidgets

from Grafica_Practica15 import Tiro_Parabolico

qtCreatorFile = "Practica15.ui" # Nombre del archivo aquí. Relative Path

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #------------- NUEVAS APLICACIONES --------------------------------

        self.button_cerrar.clicked.connect(self.cerrarVentana)      # Función del botón cerrar.
        self.button_simular.clicked.connect(self.simularTiro)

        # Mostrando una gráfica de prueba
        self.graficaPar = Tiro_Parabolico()   # Creamos un Canvas para cada una de las gráficas.
        self.graf_tiro.addWidget(self.graficaPar)     #Agregamos la gráfica al widget.
        self.graficaPar.graficar_muestra()   # Trabajamos con la gráfica
        

    #----------------- NUEVAS FUNCIONES -----------------------------------

    #-------- Función de cerrar----------------------------------------------
    def cerrarVentana(self):  
        quit()
    #-------- Función de cerrar (FIN) ---------------------------------------

    def simularTiro(self):

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
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
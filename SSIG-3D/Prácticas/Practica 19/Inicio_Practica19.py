import sys
from PyQt5 import uic, QtWidgets

from Grafica_Practica19 import Coordenadas_Esfericas

qtCreatorFile = "Practica19.ui" # Nombre del archivo aquí. Relative Path

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

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
        quit()
    #-------- Función de cerrar (FIN) ---------------------------------------

    def simularEsfericas(self):
        self.graficaEsfe.vaciar_grafica()    #Eliminamos los plt y axes existentes.   
        self.graf_esfe.removeWidget(self.graficaEsfe)    # Eliminamos el widget creado anterioremente
        self.graficaEsfe.deleteLater()
        self.graficaEsfe = None

        # Asignamos los valores insertados.
        x = float(self.sBox_X.text())        
        y = float(self.sBox_Y.text())
        z = float(self.sBox_Z.text())

        self.graficaEsfe = Coordenadas_Esfericas()
        self.graf_esfe.addWidget(self.graficaEsfe)
        self.graficaEsfe.graficar_coor_esfe(x, y, z)


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
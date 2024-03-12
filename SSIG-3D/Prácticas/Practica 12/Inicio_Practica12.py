import sys
from PyQt5 import uic, QtWidgets

from Grafica_Practica12 import Polea

qtCreatorFile = "Practica12.ui" # Nombre del archivo aquí. Relative Path

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #------------- NUEVAS APLICACIONES --------------------------------

        #Label
        global ace
        ace = self.label_ace

        # Mostrando una gráfica de prueba
        self.graficaPolea = Polea()   # Creamos un Canvas para cada una de las gráficas.
        self.graf_polea.addWidget(self.graficaPolea)     #Agregamos la gráfica al widget.
        self.graficaPolea.graficar_muestra(ace)   # Trabajamos con la gráfica

        # Funciones de los botones        
        self.button_cerrar.clicked.connect(self.cerrarVentana)   # Función del botón cerrar.
        self.button_simular.clicked.connect(self.simulacion)
        
    #----------------- NUEVAS FUNCIONES -----------------------------------

    #-------- Función de cerrar----------------------------------------------
    def cerrarVentana(self):  
        quit()
    #-------- Función de cerrar (FIN) ---------------------------------------

    def simulacion(self):

        self.graficaPolea.vaciar_grafica()    #Eliminamos los plt y axes existentes.   
        self.graf_polea.removeWidget(self.graficaPolea)    # Eliminamos el widget creado anterioremente
        self.graficaPolea.deleteLater()
        self.graficaPolea = None

        m1 = float(self.sBox_m1.text())
        m2 = float(self.sBox_m2.text())
        l = float(self.sBox_l.text())
        muk = float(self.sBox_muk.text())
        thetha = float(self.sBox_thetha.text())

        self.graficaPolea = Polea()   # Creamos un Canvas para cada una de las gráficas.
        self.graf_polea.addWidget(self.graficaPolea)     #Agregamos la gráfica al widget.
        self.graficaPolea.graficarPolea(m1, m2, l, muk, thetha, ace)   # Trabajamos con la gráfica


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
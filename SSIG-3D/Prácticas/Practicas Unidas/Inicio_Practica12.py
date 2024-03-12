import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

from Grafica_Practica12 import Polea

class Prac12(QMainWindow):
    def __init__(self, parent=None):
        super(Prac12, self).__init__(parent)
        loadUi('Interfaces\Practica12.ui', self)

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
        self.parent().show()
        self.close()
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
    window = Prac12()
    window.show()
    sys.exit(app.exec_())
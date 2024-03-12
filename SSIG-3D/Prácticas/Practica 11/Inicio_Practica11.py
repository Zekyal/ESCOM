import sys
from PyQt5 import uic, QtWidgets
from Graficas_Practica11 import Esfera_Conductora

import Errores

qtCreatorFile = "Practica11.ui" # Nombre del archivo aquí. Relative Path

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

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
        quit()
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
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
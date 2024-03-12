import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl

from Grafica_Practica21 import Movi_Circular

qtCreatorFile = "Practica21.ui" # Nombre del archivo aquí. Relative Path

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #------------- NUEVAS APLICACIONES --------------------------------

        self.button_cerrar.clicked.connect(self.cerrarVentana)      # Función del botón cerrar.
        self.button_simular.clicked.connect(self.simular)
        self.link_video.clicked.connect(self.abrir_pagina)
        
        # Mostrando Movimiento Circular
        self.graficaCircular = Movi_Circular()   
        self.graf_circular.addWidget(self.graficaCircular)
        self.graficaCircular.graficar_muestra()
        
    #----------------- NUEVAS FUNCIONES -----------------------------------

    #-------- Función de cerrar----------------------------------------------
    def cerrarVentana(self):  
        quit()
    #-------- Función de cerrar (FIN) ---------------------------------------

    #-------- Función de abrir una página web -------------------------------------------------------------------------
    def abrir_pagina(self):
        link = QUrl("https://www.youtube.com/watch?v=JVGvzWgO5i4") # Link  de la página de Youtube
        QDesktopServices.openUrl(QUrl(link))    # Abre la página en el navegador.
    #-------- Función de abrir una página web (FIN) -------------------------------------------------------------------

    def simular(self):
        self.graficaCircular.vaciar_grafica()    #Eliminamos los plt y axes existentes.   
        self.graf_circular.removeWidget(self.graficaCircular)    # Eliminamos el widget creado anterioremente
        self.graficaCircular.deleteLater()
        self.graficaCircular = None

        # Asignamos los valores insertados.
        r = float(self.sBox_r.text())
        mass = float(self.sBox_mass.text())

        # Mostrando Movimiento Circular
        self.graficaCircular = Movi_Circular()   
        self.graf_circular.addWidget(self.graficaCircular)
        self.graficaCircular.graficar_circular(r, mass)


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
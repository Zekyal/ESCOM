import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl

from Graficas_Practica17 import Camp_Magne_Cable, Camp_Magne_Cables_Par

qtCreatorFile = "Practica17.ui" # Nombre del archivo aquí. Relative Path

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #------------- NUEVAS APLICACIONES --------------------------------

        self.button_cable.hide()

        self.button_cerrar.clicked.connect(self.cerrarVentana)      # Función del botón cerrar.
        self.button_cable.clicked.connect(self.mostrarCable)
        self.button_cables.clicked.connect(self.mostrarCables)
        self.link_Camp_Magne.clicked.connect(self.abrir_pagina)

        # Mostrando una gráficas
        self.graficaMagneC = Camp_Magne_Cable()   # Creamos un Canvas para cada una de las gráficas.
        self.graf_cable.addWidget(self.graficaMagneC)     #Agregamos la gráfica al widget.
        self.graficaMagneC.graficar_muestra()   # Trabajamos con la gráfica

        self.graficaMagneCs = Camp_Magne_Cables_Par()   # Creamos un Canvas para cada una de las gráficas.
        self.graf_cables.addWidget(self.graficaMagneCs)     #Agregamos la gráfica al widget.
        self.graficaMagneCs.graficar_muestra()   # Trabajamos con la gráfica
        
    #----------------- NUEVAS FUNCIONES -----------------------------------

    #-------- Función de cerrar----------------------------------------------
    def cerrarVentana(self):  
        quit()
    #-------- Función de cerrar (FIN) ---------------------------------------

    def mostrarCable(self):
        self.button_cable.hide()
        self.button_cables.show()
        self.stackedWidget.setCurrentWidget(self.Magne_Cable)

    def mostrarCables(self):
        self.button_cable.show()
        self.button_cables.hide()
        self.stackedWidget.setCurrentWidget(self.Magne_Cables_Par)

    #-------- Función de abrir una página web -------------------------------------------------------------------------
    def abrir_pagina(self):
        link = QUrl("https://acortar.link/kkk") # Link  de la página de Khan Academy
        QDesktopServices.openUrl(QUrl(link))    # Abre la página en el navegador.
    #-------- Función de abrir una página web (FIN) -------------------------------------------------------------------


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
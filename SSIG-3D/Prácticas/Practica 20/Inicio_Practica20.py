import sys
from PyQt5 import uic, QtWidgets
import numpy as np

from Graficas_Practica20 import Ley_Gauss, Angulo_Solido

qtCreatorFile = "Practica20.ui" # Nombre del archivo aquí. Relative Path

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #------------- NUEVAS APLICACIONES --------------------------------

        global valor
        valor = self.line_valor

        self.button_cerrar.clicked.connect(self.cerrarVentana)      # Función del botón cerrar.
        self.button_simular.clicked.connect(self.simularGauss)
        
        # Mostrando Ley de Gauss
        self.graficaGauss = Ley_Gauss()   
        self.graf_gauss.addWidget(self.graficaGauss)
        self.graficaGauss.graficar_gauss_muestra(valor)

        # Mostrando Ángulo Sólido
        self.graficaSolido = Angulo_Solido() 
        self.graf_ang_solid.addWidget(self.graficaSolido)
        self.graficaSolido.graficar_solido_muestra()

    #----------------- NUEVAS FUNCIONES -----------------------------------

    #-------- Función de cerrar----------------------------------------------
    def cerrarVentana(self):  
        quit()
    #-------- Función de cerrar (FIN) ---------------------------------------

    def simularGauss(self):
        self.graficaGauss.vaciar_grafica()    #Eliminamos los plt y axes existentes.   
        self.graf_gauss.removeWidget(self.graficaGauss)    # Eliminamos el widget creado anterioremente
        self.graficaGauss.deleteLater()
        self.graficaGauss = None

        self.graficaSolido.vaciar_grafica()    #Eliminamos los plt y axes existentes.   
        self.graf_ang_solid.removeWidget(self.graficaSolido)    # Eliminamos el widget creado anterioremente
        self.graficaSolido.deleteLater()
        self.graficaSolido = None

        # Asignamos los valores insertados.
        theta_cone = float(self.sBox_grados.text())

        # Mostrando Ley de Gauss
        self.graficaGauss = Ley_Gauss()   
        self.graf_gauss.addWidget(self.graficaGauss)
        self.graficaGauss.graficar_gauss(np.deg2rad(theta_cone), valor)

        # Mostrando Ángulo Sólido
        self.graficaSolido = Angulo_Solido() 
        self.graf_ang_solid.addWidget(self.graficaSolido)
        self.graficaSolido.graficar_solido(np.deg2rad(theta_cone))


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
import numpy as np

from Grafica_Practica07 import Cosenos_directores

class Prac10(QMainWindow):
    def __init__(self, parent=None):
        super(Prac10, self).__init__(parent)
        loadUi('Interfaces\Practica10.ui', self)

        #------------- NUEVAS APLICACIONES --------------------------------
        self.button_reiniciar.hide()

        self.button_cerrar.clicked.connect(self.cerrarVentana)      # Función del botón cerrar.
        self.button_calcular.clicked.connect(self.calcularValores)
        self.button_reiniciar.clicked.connect(self.reiniciarValores)
        
    #----------------- NUEVAS FUNCIONES -----------------------------------

    #-------- Función de cerrar----------------------------------------------
    def cerrarVentana(self):  
        self.parent().show()
        self.close()
    #-------- Función de cerrar (FIN) ---------------------------------------

    def calcularValores(self):
        self.button_reiniciar.show()
        self.button_calcular.setEnabled(False)

        rx = float(self.sBox_X.text())  
        ry = float(self.sBox_Y.text())  
        rz = float(self.sBox_Z.text())  

        magnitud = np.sqrt(pow(rx, 2) + pow(ry, 2) + pow(rz, 2))
    
        if (magnitud == 0):
            alpha = 0
            beta = 0
            gamma = 0
        else:
            alpha = np.arccos(np.absolute(rz) / magnitud)
            beta = np.arccos(np.absolute(rx) / magnitud)
            gamma = np.arccos(np.absolute(ry) / magnitud)
    
        alphaDeg = np.degrees(alpha)
        betaDeg = np.degrees(beta)
        gammaDeg = np.degrees(gamma)

        self.line_magnitud.setText(str(magnitud)) 
        self.line_grad_alpha.setText(str(alphaDeg) + "°")
        self.line_grad_beta.setText(str(betaDeg) + "°")
        self.line_grad_gamma.setText(str(gammaDeg) + "°")
        self.line_rad_alpha.setText(str(alpha) + " rad")
        self.line_rad_beta.setText(str(beta) + " rad")
        self.line_rad_gamma.setText(str(gamma) + " rad")

        self.graficaCos = Cosenos_directores()   # Creamos un Canvas para cada una de las gráficas.
        self.graf_cosenos.addWidget(self.graficaCos)     #Agregamos la gráfica al widget.
        self.graficaCos.graficar_vector_cos(magnitud, rx, ry, rz)   # Trabajamos con la gráfica

    def reiniciarValores(self):
        self.button_reiniciar.hide()
        self.button_calcular.setEnabled(True)

        self.sBox_X.setValue(0.00)
        self.sBox_Y.setValue(0.00)
        self.sBox_Z.setValue(0.00)

        self.line_magnitud.setText("")
        self.line_grad_alpha.setText("")
        self.line_grad_beta.setText("")
        self.line_grad_gamma.setText("")
        self.line_rad_alpha.setText("")
        self.line_rad_beta.setText("")
        self.line_rad_gamma.setText("")

        self.graficaCos.vaciar_grafica()    #Eliminamos los plt y axes existentes.   
        self.graf_cosenos.removeWidget(self.graficaCos)    # Eliminamos el widget creado anterioremente
        self.graficaCos.deleteLater()
        self.graficaCos = None

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = Prac10()
    window.show()
    sys.exit(app.exec_())
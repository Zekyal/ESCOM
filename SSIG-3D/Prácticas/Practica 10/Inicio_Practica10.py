import sys
from PyQt5 import uic, QtWidgets
import numpy as np

qtCreatorFile = "Practica10.ui" # Nombre del archivo aquí. Relative Path

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #------------- NUEVAS APLICACIONES --------------------------------
        self.button_reiniciar.hide()

        self.button_cerrar.clicked.connect(self.cerrarVentana)      # Función del botón cerrar.
        self.button_calcular.clicked.connect(self.calcularValores)
        self.button_reiniciar.clicked.connect(self.reiniciarValores)
        

    #----------------- NUEVAS FUNCIONES -----------------------------------

    #-------- Función de cerrar----------------------------------------------
    def cerrarVentana(self):  
        quit()
    #-------- Función de cerrar (FIN) ---------------------------------------

    def calcularValores(self):
        self.button_reiniciar.show()
        self.button_calcular.setEnabled(False)

        x = float(self.sBox_X.text())  
        y = float(self.sBox_Y.text())  
        z = float(self.sBox_Z.text())  

        magnitud = np.sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2))
    
        if (magnitud == 0):
            alpha = 0
            beta = 0
            gamma = 0
        else:
            alpha = np.arccos(np.absolute(z) / magnitud)
            beta = np.arccos(np.absolute(x) / magnitud)
            gamma = np.arccos(np.absolute(y) / magnitud)
    
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



if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
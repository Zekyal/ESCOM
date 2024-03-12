import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
import numpy as np
from PyQt5.QtWidgets import QFileDialog # Ayuda a la selección de una carpeta

import Errores
from Grafica_Practica07 import Cosenos_directores

class Prac07(QMainWindow):
    def __init__(self, parent=None):
        super(Prac07, self).__init__(parent)
        loadUi('Interfaces\Practica07.ui', self)

        #------------- NUEVAS APLICACIONES --------------------------------
        self.button_reiniciar.hide()
        self.button_guardar.hide()

        self.button_cerrar.clicked.connect(self.cerrarVentana)   # Función del botón cerrar.
        self.button_grad_alpha.clicked.connect(self.gradosAlpha)   
        self.button_rad_alpha.clicked.connect(self.radianesAlpha)
        self.button_grad_beta.clicked.connect(self.gradosBeta)   
        self.button_rad_beta.clicked.connect(self.radianesBeta) 
        self.button_grad_gamma.clicked.connect(self.gradosGamma)   
        self.button_rad_gamma.clicked.connect(self.radianesGamma)
        self.button_graficar.clicked.connect(self.graficarCosenos)
        self.button_guardar.clicked.connect(self.guardarCosenos)
        self.button_reiniciar.clicked.connect(self.reiniciar_Cosenos)
        

    #----------------- NUEVAS FUNCIONES -----------------------------------

    #-------- Función de cerrar--------------------------------------------------
    def cerrarVentana(self):  
        self.parent().show()
        self.close()
    #-------- Función de cerrar (FIN) -------------------------------------------

    #-------- Checando botones ---------------------------------------------------
    def gradosAlpha(self):
        self.quitarChecked(self.button_rad_alpha)

    def radianesAlpha(self):
        self.quitarChecked(self.button_grad_alpha)

    def gradosBeta(self):
        self.quitarChecked(self.button_rad_beta)

    def radianesBeta(self):
        self.quitarChecked(self.button_grad_beta)

    def gradosGamma(self):
        self.quitarChecked(self.button_rad_gamma)

    def radianesGamma(self):
        self.quitarChecked(self.button_grad_gamma)

    def quitarChecked(self, button):
        button.setChecked(False)
    #-------- Checando botones (FIN) -------------------------------------------------

    def graficarCosenos(self):

        if (self.sBox_magnitud.text() == '0.00'):
            Errores.Error_Magnitud(self)
        elif ((self.button_grad_alpha.isChecked() == False) and (self.button_rad_alpha.isChecked() == False)):
            Errores.Error_Tipo(self)
        elif ((self.button_grad_beta.isChecked() == False) and (self.button_rad_beta.isChecked() == False)):
            Errores.Error_Tipo(self)
        elif ((self.button_grad_gamma.isChecked() == False) and (self.button_rad_gamma.isChecked() == False)):
            Errores.Error_Tipo(self)
        else:
            self.button_reiniciar.show()
            self.button_guardar.show()
            self.button_graficar.setEnabled(False)

            magnitud = float(self.sBox_magnitud.text())
            alpha = float(self.sBox_alpha.text())
            beta = float(self.sBox_beta.text())
            gamma = float(self.sBox_gamma.text())
            if (self.button_grad_alpha.isChecked()):
                alpha = np.radians(alpha)   # Valor de theta se convierte a radianes
            if (self.button_grad_beta.isChecked()):
                beta = np.radians(beta)   # Valor de theta se convierte a radianes
            if (self.button_grad_gamma.isChecked()):
                gamma = np.radians(gamma)   # Valor de theta se convierte a radianes

            # Ejes del Vector
            # β es el angulo entre el vector y i
            rx = magnitud * np.cos(beta)
            # ɣ es el angulo entre el vector y j
            ry = magnitud * np.cos(gamma)
            # α es el angulo entre el vector y k
            rz = magnitud * np.cos(alpha)

            self.graficaCos = Cosenos_directores()   # Creamos un Canvas para cada una de las gráficas.
            self.graf_vector.addWidget(self.graficaCos)     #Agregamos la gráfica al widget.
            self.graficaCos.graficar_vector_cos(magnitud, rx, ry, rz)   # Trabajamos con la gráfica

    def guardarCosenos(self):
        self.guardar_grafica()
        if (direccion == ""):
            Errores.Error_Direccion(self)
        else:
            self.graficaCos.guardar_graf(direccion)

    def guardar_grafica(self):      # Función para seleccionar la carpeta de destino de un documento
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setOption(QFileDialog.ShowDirsOnly)
        global direccion
        direccion = dialog.getExistingDirectory(self, 'Escoge la carpeta de destino:', os.path.curdir)   # Esta es la dirección

    def reiniciar_Cosenos(self):
        self.graficaCos.vaciar_grafica()    #Eliminamos los plt y axes existentes.   
        self.graf_vector.removeWidget(self.graficaCos)    # Eliminamos el widget creado anterioremente
        self.graficaCos.deleteLater()
        self.graficaCos = None

        self.button_reiniciar.hide()
        self.button_guardar.hide()
        self.button_graficar.setEnabled(True)

        self.sBox_magnitud.setValue(0.0)
        self.sBox_alpha.setValue(0.0)
        self.sBox_beta.setValue(0.0)
        self.sBox_gamma.setValue(0.0)

        self.quitarChecked(self.button_rad_alpha)
        self.quitarChecked(self.button_grad_alpha)
        self.quitarChecked(self.button_rad_beta)
        self.quitarChecked(self.button_grad_beta)
        self.quitarChecked(self.button_rad_gamma)
        self.quitarChecked(self.button_grad_gamma)


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = Prac07()
    window.show()
    sys.exit(app.exec_())
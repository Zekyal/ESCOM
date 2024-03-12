import sys
import os
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QFileDialog # Ayuda a la selección de una carpeta

from Graficas_Practica06 import Componentes

qtCreatorFile = "Practica06.ui" # Nombre del archivo aquí. Relative Path

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #------------- NUEVAS APLICACIONES --------------------------------

        self.button_guardar.clicked.connect(self.seleccionar_carpeta)   # Función del botón para seleccionar una carpeta.
        self.button_cerrar.clicked.connect(self.cerrarVentana)   # Función del botón cerrar.
        self.button_graficar.clicked.connect(self.graficar_componentes) # Función de graficar
        self.button_reintentar.clicked.connect(self.reiniciar_componentes) # Reiniciar programa
        
    #----------------- NUEVAS FUNCIONES -----------------------------------

    #-------- Función de cerrar-------------------------------------------------
    def cerrarVentana(self):  
        quit()
    #-------- Función de cerrar (FIN) -------------------------------------------

    def seleccionar_carpeta(self): 
        # La creación de una ventana para guardar la dirección donde se guardará la imagen.
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setOption(QFileDialog.ShowDirsOnly)
        global directory
        directory = dialog.getExistingDirectory(self, 'Choose Directory', os.path.curdir)   # Esta es la dirección 
        # Habilitando los botones
        self.comp_i.setEnabled(True)
        self.comp_j.setEnabled(True)
        self.comp_k.setEnabled(True)
        self.button_graficar.setEnabled(True)

    def graficar_componentes(self):
        self.button_graficar.setEnabled(False)
        self.button_reintentar.setEnabled(True)
        # Insercion de valores
        i = float(self.comp_i.text())
        j = float(self.comp_j.text())
        k = float(self.comp_k.text())

        self.graficaComp = Componentes()   # Creamos un Canvas para cada una de las gráficas.
        self.grafica_componentes.addWidget(self.graficaComp)     #Agregamos la gráfica al widget.
        self.graficaComp.graficarVectorComp(i, j, k, directory)   # Trabajamos con la gráfica

    def reiniciar_componentes(self):
        #Deshabilitando botones
        self.button_reintentar.setEnabled(False)
        self.button_graficar.setEnabled(True)
        # Reiniciando los valores
        self.comp_i.setValue(0.0)
        self.comp_j.setValue(0.0)
        self.comp_k.setValue(0.0)
        # Eliminando la gráfica y Widget creado anteriormente.
        self.graficaComp.vaciar_grafica()    #Eliminamos los plt y axes existentes.   
        self.grafica_componentes.removeWidget(self.graficaComp)    # Eliminamos el widget creado anterioremente
        self.graficaComp.deleteLater()
        self.graficaComp = None

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
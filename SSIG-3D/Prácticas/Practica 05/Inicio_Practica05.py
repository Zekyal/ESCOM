import sys
import os
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QFileDialog # Ayuda a la selección de una carpeta

import Errores05

from Grafica_Practica05 import ley_Inercia

qtCreatorFile = "Practica05.ui" # Nombre del archivo aquí. Relative Path

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #------------- NUEVAS APLICACIONES --------------------------------
        # Ocultando frames
        self.frame_6.hide()

        # Mostrando una gráfica de prueba
        self.grafica1raLey = ley_Inercia()   # Creamos un Canvas para cada una de las gráficas.
        self.graf_1ra_ley.addWidget(self.grafica1raLey)     #Agregamos la gráfica al widget.
        self.grafica1raLey.graficar1raLey_muestra()   # Trabajamos con la gráfica

        # Funciones de los botones        
        self.button_cerrar.clicked.connect(self.cerrarVentana)   # Función del botón cerrar.
        self.linkButton_pag.clicked.connect(self.abrir_pagina)  # Función que abre una página web.
        self.button_comenzar.clicked.connect(self.comenzar) # Función para mostrar la inserción de datos.
        self.button_graficar.clicked.connect(self.graficar_1ra_ley) # Función para graficar
        self.button_guardar.clicked.connect(self.guardar_grafica_1raLey)   # Función para guardar gif
        self.button_reiniciar.clicked.connect(self.reiniciar_grafica)   # Función para reiniciar ejercicio

    #----------------- NUEVAS FUNCIONES -----------------------------------------------------------------------------------------------------------------------------

    #-------- Función de cerrar----------------------------------------------------------------------------------------
    def cerrarVentana(self):  
        quit()
    #-------- Función de cerrar (FIN) ---------------------------------------------------------------------------------

    #-------- Función de abrir una página web -------------------------------------------------------------------------
    def abrir_pagina(self):
        link = QUrl("https://rb.gy/wtbiuj") # Link  de la página de Khan Academy
        QDesktopServices.openUrl(QUrl(link))    # Abre la página en el navegador.
    #-------- Función de abrir una página web (FIN) -------------------------------------------------------------------

    #-------- Función de comenzar -------------------------------------------------------------------------------------
    def comenzar(self):
        self.frame_6.show()
        self.button_comenzar.setEnabled(False)
        self.grafica1raLey.vaciar_grafica()    #Eliminamos los plt y axes existentes.   
        self.graf_1ra_ley.removeWidget(self.grafica1raLey)    # Eliminamos el widget creado anterioremente
        self.grafica1raLey.deleteLater()
        self.grafica1raLey = None
    #-------- Función de comenzar (FIN) -------------------------------------------------------------------------------

    #-------- Función de graficar -------------------------------------------------------------------------------------
    def graficar_1ra_ley(self):
        self.button_graficar.setEnabled(False)
        self.button_guardar.setEnabled(True)
        self.button_reiniciar.setEnabled(True)
        Xo = float(self.sBox_Xo.text())
        Yo = float(self.sBox_Yo.text())
        Zo = float(self.sBox_Zo.text())
        V0x = float(self.sBox_Vox.text())
        V0y = float(self.sBox_Voy.text())
        V0z = float(self.sBox_Voz.text())
        tiempo = float(self.sBox_tiempo.text())

        velX = V0x
        velY = V0y
        velZ = V0z

        time = []
        posX = []
        posY = []
        posZ = []

        self.tabla_valores.setRowCount(int(tiempo)*10+1)   # crea las filas exactas en la tabla de tabla_pos

        for t in range(0, int(tiempo)*10+1, 1):
            time.append(t/10)
            self.tabla_valores.setItem(t, 0, QtWidgets.QTableWidgetItem(str(t/10)))    # Mete los valores a la tabla llamada "tabla_valores" en la columna Tiempo
            posX.append(Xo + V0x*float(t/10))
            self.tabla_valores.setItem(t, 1, QtWidgets.QTableWidgetItem(str(posX[t])))    # Mete los valores a la tabla llamada "tabla_valores" en la columna Posición X
            posY.append(Yo + V0y*float(t/10))
            self.tabla_valores.setItem(t, 2, QtWidgets.QTableWidgetItem(str(posY[t])))    # Mete los valores a la tabla llamada "tabla_valores" en la columna Posición Y
            posZ.append(Zo + V0z*float(t/10))
            self.tabla_valores.setItem(t, 3, QtWidgets.QTableWidgetItem(str(posZ[t])))    # Mete los valores a la tabla llamada "tabla_pos" en la columna Posición Z
            self.tabla_valores.setItem(t, 4, QtWidgets.QTableWidgetItem(str(velX)))    # Mete los valores a la tabla llamada "tabla_pos" en la columna Velocidad X
            self.tabla_valores.setItem(t, 5, QtWidgets.QTableWidgetItem(str(velY)))    # Mete los valores a la tabla llamada "tabla_pos" en la columna Velocidad Y
            self.tabla_valores.setItem(t, 6, QtWidgets.QTableWidgetItem(str(velZ)))    # Mete los valores a la tabla llamada "tabla_pos" en la columna Velocidad Z
            
        self.grafica1raLey = ley_Inercia()   # Creamos un Canvas para cada una de las gráficas.
        self.graf_1ra_ley.addWidget(self.grafica1raLey)     #Agregamos la gráfica al widget.
        self.grafica1raLey.graficar1raLey(posX, posY, posZ, velX, velY, velZ)   # Trabajamos con la gráfica

    #-------- Función de graficar (FIN) -------------------------------------------------------------------------------

    #-------- Función guardar grafica ---------------------------------------------------------------------------------
    def guardar_grafica(self):      # Función para seleccionar la carpeta de destino de un documento
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setOption(QFileDialog.ShowDirsOnly)
        global direccion
        direccion = dialog.getExistingDirectory(self, 'Escoge la carpeta de destino:', os.path.curdir)   # Esta es la dirección 

    #-------- Función de guardar GIF ----------------------------------------------------------------------------------

    def guardar_grafica_1raLey(self):
        self.guardar_grafica()
        #self.grafica1raLey.guardar_graf(direccion)
        if (direccion == ""):
            Errores05.Error_Direccion(self)
        else:
            self.grafica1raLey.guardar_graf(direccion)
    #-------- Función de guardar GIF (FIN) ----------------------------------------------------------------------------
    
    #-------- Función de reiniciar ejercicio --------------------------------------------------------------------------

    def reiniciar_grafica(self):
        self.button_graficar.setEnabled(True)
        self.tabla_valores.setRowCount(0)   # Elimina las filas
        self.grafica1raLey.vaciar_grafica()    #Eliminamos los plt y axes existentes.   
        self.graf_1ra_ley.removeWidget(self.grafica1raLey)    # Eliminamos el widget creado anterioremente
        self.grafica1raLey.deleteLater()
        self.grafica1raLey = None

    #-------- Función de reiniciar ejercicio (FIN) --------------------------------------------------------------------


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
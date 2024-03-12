# Práctica 02. Tiro Parabólico. (SSIS-3D)

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
import webbrowser as wb ## Abrir archivos

from Grafica_Practica02 import Canvas_grafica  # Archivo para realizar las gráficas

class Prac02(QMainWindow):
    def __init__(self, parent=None):
        super(Prac02, self).__init__(parent)
        loadUi('Interfaces\Practica02.ui', self)

        #------------- NUEVAS APLICACIONES --------------------------------

        self.button_cerrar.clicked.connect(self.cerrarVentana)   # Función del botón cerrar.
        self.button_graficar.clicked.connect(self.tiro_par)     # Inicia la graficación.
        self.button_reiniciar.clicked.connect(self.nueva_graf) # Crear una nueva gráfica.
        self.button_gif.clicked.connect(self.ver_gif)

    #----------------- NUEVAS FUNCIONES ----------------------------------------

    #-------- Función de cerrar-------------------------------------------------
    def cerrarVentana(self):
        if hasattr(self, 'graficaTiroPar'):
            self.graficaTiroPar.cerrarGraf()
        self.parent().show()
        self.close()
    #-------- Función de cerrar (FIN) -------------------------------------------

    #-------- Función de graficar Tiro Parabólico -------------------------------
    def tiro_par(self):

        # Desactivamos el boton de graficar patra evitar crear nuevas gráficas y se sobrepongan
        self.button_graficar.setEnabled(False)

        # Tomamos valores de las constantes en los spinbox
        x0 = float(self.sbox_posX.text())     
        y0 = float(self.sbox_posY.text())
        z0 = float(self.sbox_posZ.text())
        V0x = float(self.sbox_velX.text())
        V0y = float(self.sbox_velY.text())
        V0z = float(self.sbox_velZ.text())
        tiempo = float(self.sbox_tiempo.text())

        #Obtenemos todos los decimales dentro del valor dado de tiempo solicitado
        calculando = str(tiempo)
        decimales = calculando.split(".")

        entero = decimales[0][0]
        primerDec = decimales[1][0]

        # Se hace la comprobación dado que no considera en los casos de tener "0" en el segundo decimal        
        if (len(decimales[1]) == 1):    
            segDec = 0
        else:
            segDec = decimales[1][1:]

        posX = []   # Lista para guardar los valores de las posiciones de X
        posY = []   # Lista para guardar los valores de las posiciones de Y
        posZ = []   # Lista para guardar los valores de las posiciones de Z

        velX = []   # Lista para guardar los valores de las velocidades de X
        velY = []   # Lista para guardar los valores de las velocidades de Y
        velZ = []   # Lista para guardar los valores de las velocidades de Z

        gravedad = 9.81     # Valor de la gravedad.
        numero_filas = int(entero)*100 + int(primerDec)*10 + int(segDec) + 1 # checar

        self.tabla_pos.setRowCount(numero_filas)   # crea las filas exactas en la tabla de tabla_pos

        for t in range(0, numero_filas, 1):
            self.tabla_pos.setItem(t, 0, QtWidgets.QTableWidgetItem(str(t/100)))    # Mete los valores a la tabla llamada "tabla_pos" en la columna Tiempo
            posX.append(V0x*float(t/100) + x0)
            self.tabla_pos.setItem(t, 1, QtWidgets.QTableWidgetItem(str(posX[t])))    # Mete los valores a la tabla llamada "tabla_pos" en la columna Posición X
            posY.append(V0y*float(t/100) + y0)
            self.tabla_pos.setItem(t, 2, QtWidgets.QTableWidgetItem(str(posY[t])))    # Mete los valores a la tabla llamada "tabla_pos" en la columna Posición Y
            posZ.append(-1/2*gravedad*float(pow(t/100, 2)) + V0z*float(t/100) + z0)
            self.tabla_pos.setItem(t, 3, QtWidgets.QTableWidgetItem(str(posZ[t])))    # Mete los valores a la tabla llamada "tabla_pos" en la columna Posición Z
            velX.append(V0x)
            self.tabla_pos.setItem(t, 4, QtWidgets.QTableWidgetItem(str(velX[t])))    # Mete los valores a la tabla llamada "tabla_pos" en la columna Velocidad X
            velY.append(V0y)
            self.tabla_pos.setItem(t, 5, QtWidgets.QTableWidgetItem(str(velY[t])))    # Mete los valores a la tabla llamada "tabla_pos" en la columna Velocidad Y
            velZ.append(-gravedad*(t/100) + V0z)
            self.tabla_pos.setItem(t, 6, QtWidgets.QTableWidgetItem(str(velZ[t])))    # Mete los valores a la tabla llamada "tabla_pos" en la columna Velocidad Z


        ##Graficación
        # Dado que Qt Designer no cuenta con un botón específico para matplotlib, debemos crear una nueva clase 
        # a cada widget de matplot que agreguemos y agregar nuevas funciones a un Layout de la aplicación.

        self.graficaTiroPar = Canvas_grafica()   # Creamos un Canvas para cada una de las gráficas.
        self.graf_tiro_par.addWidget(self.graficaTiroPar)     #Agregamos la gráfica al widget.
        self.graficaTiroPar.graficarTiroParabolico(posX, posY, posZ, velX, velY, velZ, round(tiempo))   # Trabajamos con la gráfica

        # Activamos el boton de Reinicio
        self.button_reiniciar.setEnabled(True)
        self.button_gif.setEnabled(True)

        # Desactivamos los spinbox para evitar modificaciones
        self.sbox_posX.setEnabled(False)
        self.sbox_posY.setEnabled(False)
        self.sbox_posZ.setEnabled(False)
        self.sbox_velX.setEnabled(False)
        self.sbox_velY.setEnabled(False)
        self.sbox_velZ.setEnabled(False)
        self.sbox_tiempo.setEnabled(False)

    #-------- Función de graficar Tiro Parabólico ---------------------------------------

    #-------- Función de reinicio  ------------------------------------------------------
    def nueva_graf(self):
        self.graficaTiroPar.vaciar_grafica()    #Eliminamos los plt y axes existentes.   
        self.graf_tiro_par.removeWidget(self.graficaTiroPar)    # Eliminamos el widget creado anterioremente
        del self.graficaTiroPar 

        # Reactivamos el boton de graficar y los spinBox
        self.button_graficar.setEnabled(True)
        self.button_reiniciar.setEnabled(False)
        self.button_gif.setEnabled(False)
        self.sbox_posX.setEnabled(True)
        self.sbox_posY.setEnabled(True)
        self.sbox_posZ.setEnabled(True)
        self.sbox_velX.setEnabled(True)
        self.sbox_velY.setEnabled(True)
        self.sbox_velZ.setEnabled(True)
        self.sbox_tiempo.setEnabled(True)

    #-------- Función de reinicio (FIN) -------------------------------------------------

    #-------- Función de abrir gif ------------------------------------------------------
    def ver_gif(self):
        wb.open_new('Practica02_graf\Tiro Parabolico.gif')

    #-------- Función de abrir gif (FIN) ------------------------------------------------

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = Prac02()
    window.show()
    sys.exit(app.exec_())
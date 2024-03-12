# Práctica 04. Variación del Tiro Parabólico. (SSIS-3D)

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
import webbrowser as wb ## Abrir archivos

from Graficas_Practica04 import Canvas_grafica, Canvas_grafica2  # Archivo para realizar las gráficas

class Prac04(QMainWindow):
    def __init__(self, parent=None):
        super(Prac04, self).__init__(parent)
        loadUi('Interfaces\Practica04.ui', self)

        #------------- NUEVAS APLICACIONES --------------------------------
        
        self.button_cerrar.clicked.connect(self.cerrarVentana)   # Función del botón cerrar.
        self.button_graficar.clicked.connect(self.tiro_par)     # Inicia la graficación.
        self.button_reiniciar.clicked.connect(self.nueva_graf) # Crear una nueva gráfica.
        self.button_pos.clicked.connect(self.ver_pos)   # Abrir la imágen del Vector de Posición.
        self.button_vel.clicked.connect(self.ver_vel)   # Abrir la imágen del Vector de velocidad.

    #----------------- NUEVAS FUNCIONES -----------------------------------

    #-------- Función de cerrar-------------------------------------------------
    def cerrarVentana(self):  
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
        V0y = float(self.sbox_velX.text())
        V0z = float(self.sbox_velX.text())
        tiempo = float(self.sbox_tiempo.text())
        gravedad = 9.81     # Valor de la gravedad.

        posX = V0x*tiempo + x0   # Guarda los valores de la posición de X
        posY = V0y*tiempo + y0   # Guarda los valores de la posición de Y
        posZ = -1/2*gravedad*pow(tiempo, 2) + V0z*tiempo + z0   # Guarda los valores de la posición de Z

        velX = V0x   # Guarda los valores de la velocidad de X
        velY = V0y   # Guarda los valores de la velocidad de Y
        velZ = -gravedad*(tiempo) + V0z   # Guarda los valores de la velocidad de Z

        # Asignamos los valores coorespondientes a los labels
        self.label_posX.setText("Pos X = " + str(posX))
        self.label_posY.setText("Pos Y = " + str(posY))
        self.label_posZ.setText("Pos Z = " + str(posZ))
        self.label_velX.setText("Vel X = " + str(velX))
        self.label_velY.setText("Vel Y = " + str(velY))
        self.label_velZ.setText("Vel Z = " + str(velZ))

        ##Graficación
        # Dado que Qt Designer no cuenta con un botón específico para matplotlib, debemos crear una nueva clase 
        # a cada widget de matplot que agreguemos y agregar nuevas funciones a un Layout de la aplicación.

        self.graficaVectPos = Canvas_grafica()   # Creamos un Canvas para cada una de las gráficas.
        self.graf_vect_pos.addWidget(self.graficaVectPos)     #Agregamos la gráfica al widget.
        self.graficaVectPos.graficarVectorPos(posX, posY, posZ)   # Trabajamos con la gráfica

        self.graficaVectVel = Canvas_grafica2()
        self.graf_vect_vel.addWidget(self.graficaVectVel)     #Agregamos la gráfica al widget.
        self.graficaVectVel.graficarVectorVel(posX, posY, posZ, velX, velY, velZ)   # Trabajamos con la gráfica

        # Activamos el boton de Reinicio
        self.button_reiniciar.setEnabled(True)
        self.button_pos.setEnabled(True)
        self.button_vel.setEnabled(True)

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
        self.graficaVectPos.vaciar_grafica()    #Eliminamos los plt y axes existentes.   
        self.graf_vect_pos.removeWidget(self.graficaVectPos)    # Eliminamos el widget creado anterioremente
        self.graficaVectPos.deleteLater()
        self.graficaVectPos = None
        self.graficaVectVel.vaciar_grafica()    #Eliminamos los plt y axes existentes.   
        self.graf_vect_vel.removeWidget(self.graficaVectVel)    # Eliminamos el widget creado anterioremente
        self.graficaVectVel.deleteLater()
        self.graficaVectVel = None

        # Reactivamos el boton de graficar y los spinBox
        self.button_graficar.setEnabled(True)
        self.button_reiniciar.setEnabled(False)
        self.button_pos.setEnabled(False)
        self.button_vel.setEnabled(False)
        self.sbox_posX.setEnabled(True)
        self.sbox_posY.setEnabled(True)
        self.sbox_posZ.setEnabled(True)
        self.sbox_velX.setEnabled(True)
        self.sbox_velY.setEnabled(True)
        self.sbox_velZ.setEnabled(True)
        self.sbox_tiempo.setEnabled(True)

    #-------- Función de reinicio (FIN) -------------------------------------------------

    #-------- Función de abrir jpg Posición ------------------------------------------------------
    def ver_pos(self):
        wb.open_new('Practica04_grafs\VectorPosicion.jpg')

    #-------- Función de abrir gif (FIN) ------------------------------------------------

    #-------- Función de abrir jpg Velocidad ------------------------------------------------------
    def ver_vel(self):
        wb.open_new('Practica04_grafs\VectorVelocidad.jpg')

    #-------- Función de abrir gif (FIN) ------------------------------------------------

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = Prac04()
    window.show()
    sys.exit(app.exec_())
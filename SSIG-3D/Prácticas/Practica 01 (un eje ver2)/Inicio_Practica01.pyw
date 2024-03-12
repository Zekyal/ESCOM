# Práctica 01. Movimiento Rectilineo Uniforme. (SSIS-3D)

import sys
from PyQt5 import uic, QtWidgets
import sympy as sym     # Trabajo con los polinomios.
from sympy import *     # Operaciones con el polinomio (derivadas, integrales, sustituciones)
from PyQt5.QtCore import QThread, pyqtSignal    # Para el tiempo del cronómetro, velocímetro y acelerómetro
import time # Para el tiempo del cronómetro, velocímetro y acelerómetro

from Graficas import Canvas_grafica, Canvas_grafica2, Canvas_grafica3   # Graficación desde el archivo Graficas
import Errores01    # Mensajes de Error.

qtCreatorFile = "Practica01.ui" # Nombre del archivo de la Interfaz.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #------------- NUEVAS APLICACIONES EN LA INTERFAZ ---------------------------------------------------------#

        self.pushButton_cerrar.clicked.connect(self.cerrarVentana)      # Función del botón cerrar.
        self.bt_insertarUsuario.clicked.connect(self.insertarUsuario)   # Ingreso de Usuario.
        self.bt_grado.clicked.connect(self.obtenerGrado)        # Obtener grado y constantes.
        self.bt_graficar.clicked.connect(self.graficacion)      # Inicio de la graficación.

    #----------------- NUEVAS FUNCIONES ---------------------------------------------------------------------------#

    #-------- Función de cerrar----------------------------------------------
    def cerrarVentana(self):  
        quit()
    #-------- Función de cerrar (FIN) ---------------------------------------

    #-------- Función para Ingresar Usuario ---------------------------------
    def insertarUsuario(self):  
        usuario_nuevo = self.usuario.text()     # Tranforma el texto insertado en el espacio usuario_nuevo
        if usuario_nuevo == '':     # En caso de no insertar usuario
            Errores01.Error_Usuario(self)   # Muestra el mensaje de error
        else:
            usuario_saludo = "Bienvenido " + usuario_nuevo + "."    
            self.saludo.setText(usuario_saludo)     # Inserta el texto en el espacio de saludo

            #Para habilitar o deshabilitar los botones al avanzar en el proceso
            self.usuario.setEnabled(False)              
            self.bt_insertarUsuario.setEnabled(False)
            self.spin_grado.setEnabled(True)
            self.bt_grado.setEnabled(True)
    #-------- Función para Ingresar Usuario (FIN) ---------------------------

    #-------- Función para el grado y las constantes ------------------------
    def obtenerGrado(self): 
        grado_poli = int(self.spin_grado.text())  # Toma el valor del boton spin_grado 

        # En caso de escoger un polinomio de grado 2
        if grado_poli == 2:   
                self.dSpinBox_00.setEnabled(True)    # Habilita o deshabilita botones
                self.dSpinBox_01.setEnabled(True)
                self.dSpinBox_02.setEnabled(True)
                self.dSpinBox_03.setEnabled(False)
                self.dSpinBox_04.setEnabled(False)
                self.dSpinBox_05.setEnabled(False)
                self.dSpinBox_00.setProperty("value", 0)     # Regresa los botones a sus valores de default (0)
                self.dSpinBox_01.setProperty("value", 0)
                self.dSpinBox_03.setProperty("value", 0)
                self.dSpinBox_04.setProperty("value", 0)
                self.dSpinBox_05.setProperty("value", 0)

        # En caso de escoger un polinomio de grado 3
        elif grado_poli == 3:    
                self.dSpinBox_00.setEnabled(True)    # Habilita o deshabilita botones
                self.dSpinBox_01.setEnabled(True)
                self.dSpinBox_02.setEnabled(True)
                self.dSpinBox_03.setEnabled(True)
                self.dSpinBox_04.setEnabled(False)
                self.dSpinBox_05.setEnabled(False)
                self.dSpinBox_00.setProperty("value", 0)     # Regresa los botones a sus valores de default (0)
                self.dSpinBox_01.setProperty("value", 0)
                self.dSpinBox_02.setProperty("value", 0)
                self.dSpinBox_04.setProperty("value", 0)
                self.dSpinBox_05.setProperty("value", 0)

        # En caso de escoger un polinomio de grado 4
        elif grado_poli == 4:   
                self.dSpinBox_00.setEnabled(True)     # Habilita o deshabilita botones
                self.dSpinBox_01.setEnabled(True)
                self.dSpinBox_02.setEnabled(True)
                self.dSpinBox_03.setEnabled(True)
                self.dSpinBox_04.setEnabled(True)
                self.dSpinBox_05.setEnabled(False)
                self.dSpinBox_00.setProperty("value", 0)    # Regresa los botones a sus valores de default (0)
                self.dSpinBox_01.setProperty("value", 0)
                self.dSpinBox_02.setProperty("value", 0)
                self.dSpinBox_03.setProperty("value", 0)
                self.dSpinBox_05.setProperty("value", 0)
        
        # En caso de escoger un polinomio de grado 5
        elif grado_poli == 5:   
                self.dSpinBox_00.setEnabled(True)       # Habilita o deshabilita botones
                self.dSpinBox_01.setEnabled(True)
                self.dSpinBox_02.setEnabled(True)
                self.dSpinBox_03.setEnabled(True)
                self.dSpinBox_04.setEnabled(True)
                self.dSpinBox_05.setEnabled(True)      
                self.dSpinBox_00.setProperty("value", 0)    # Regresa los botones a sus valores de default (0)
                self.dSpinBox_01.setProperty("value", 0)
                self.dSpinBox_02.setProperty("value", 0)
                self.dSpinBox_03.setProperty("value", 0)
                self.dSpinBox_04.setProperty("value", 0)

        # Habilita el boton de bt_graficar
        self.bt_graficar.setEnabled(True)   
    #-------- Función para el grado y las constantes (FIN) -------------------

    #-------- Función para la graficación ------------------------------------
    def graficacion(self):

        # Deshabilita los botones del paso anterior
        self.spin_grado.setEnabled(False)   
        self.bt_grado.setEnabled(False)

        ## Creación de polinomio
        sym.init_printing()     # Para que funciones las variables en los polinomios
        x =Symbol("x")     # Declarando la variable "x"
        c00 = self.dSpinBox_00.text()    # Tomamos valores de las constantes en los spinbox
        c01 = self.dSpinBox_01.text()
        c02 = self.dSpinBox_02.text() 
        c03 = self.dSpinBox_03.text()
        c04 = self.dSpinBox_04.text()
        c05 = self.dSpinBox_05.text()
        grado_poli = int(self.spin_grado.text())

        if ((grado_poli == 2) and (float(c02) == 0)):
            Errores01.Error_Grado2(self)
        elif ((grado_poli == 3) and (float(c03) == 0)):
            Errores01.Error_Grado3(self)
        elif ((grado_poli == 4) and (float(c04) == 0)):
            Errores01.Error_Grado4(self)
        elif ((grado_poli == 5) and (float(c05) == 0)):
            Errores01.Error_Grado5(self)
        else:
            if float(c05) != 0:       # Creamos el polinomio según el grado y constantes seleccionadas, solo para 2 a 5 constantes
                fx = c05+"*"+str(x**5) + " + " + c04+"*"+str(x**4) + " + " + c03+"*"+str(x**3) + " + " + c02+"*"+str(x**2) + " + " + c01+"*"+str(x**1) + " + " + c00
            elif float(c04) != 0:
                fx = c04+"*"+str(x**4) + " + " + c03+"*"+str(x**3) + " + " + c02+"*"+str(x**2) + " + " + c01+"*"+str(x**1) + " + " + c00
            elif float(c03) != 0:
                fx = c03+"*"+str(x**3) + " + " + c02+"*"+str(x**2) + " + " + c01+"*"+str(x**1) + " + " + c00
            elif float(c02) != 0:
                fx = c02+"*"+str(x**2) + " + " + c01+"*"+str(x**1) + " + " + c00

            self.polinomio.setText(str(fx))     # Asigna el polinomio al recuadro llamado polinomio
            self.bt_graficar.setEnabled(False)  # Deshabilita el botón de graficar.

            ##Creación y llenado de la tabla de Velocidades
            # La velocidad es la primera derivada de nuestro polinomio.
            fdx = sym.diff(fx,x,1)  # Derivamos el polinomioX.
            global vel
            vel = []        # Lista para los valores de velocidad en X
            global t
            t = []          # Lista para los valores de tiempo
            for i in range(0, 100, 1):    # Hacemos las 20 repeticiones para guardar los valores en la tabla
                t.append(i/10)     # Ingresa los valores a la lista "t"
                vel.append(fdx.subs(x,i/10))   # Ingresa los valores a la lista "vel", haciendo las sustituciones en el polinomio
                self.tabla_vel.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i/10)))    # Mete los valores a la tabla llamada "tabla_vel" en la columna Tiempo
                self.tabla_vel.setItem(i, 1, QtWidgets.QTableWidgetItem(str(vel[i])))   # Mete los valores a la tabla llamada "tabla_vel" en la columna Posición

            ##Creación y llenado de la tabla de Posiciones
            # La posición es la integral de la velocidad o nuestro polinomio inicial.
            pos = []    # Lista para guardar los valores de posiciónX
            for k in range(0, 100, 1):
                fdp = integrate(fdx)    # Realiza la integral de nuestra función de velocidad en X "fdx"
                pos.append(fdp.subs(x,k/10))   # Ingresa los valores a la lista "pos", haciendo las sustituciones en el polinomio de X
                self.tabla_pos.setItem(k, 0, QtWidgets.QTableWidgetItem(str(k/10)))    # Mete los valores a la tabla llamada "tabla_pos" en la columna Tiempo
                self.tabla_pos.setItem(k, 1, QtWidgets.QTableWidgetItem(str(pos[k])))   # Mete los valores a la tabla llamada "tabla_pos" en la columna Posición

            ##Creación y llenado de la tabla de Aceleraciones
            # La aceleración es la segunda derivada de nuestro polinomio o la derivada de la velocidad.
            global ace
            fdx2 = sym.diff(fdx,x,1)    # realizamos la derivada de la velocidad en X.
            ace = []    # Lista para guardar los valores de la aceleración en X
            for j in range(0, 100, 1):
                ace.append(fdx2.subs(x,j/10))  # Ingresa los valores a la lista "ace", haciendo las sustituciones en el polinomio
                self.tabla_ace.setItem(j, 0, QtWidgets.QTableWidgetItem(str(j/10)))    # Mete los valores a la tabla llamada "tabla_ace" en la columna Tiempo
                self.tabla_ace.setItem(j, 1, QtWidgets.QTableWidgetItem(str(ace[j])))   # Mete los valores a la tabla llamada "tabla_ace" en la columna Aceleración

            ##Graficación
            # Dado que Qt Designer no cuenta con un botón específico para matplotlib, debemos crear una nueva clase 
            # a cada widget de matplot que agreguemos y agregar nuevas funciones a un Layout de la aplicación.

            self.graficaPosNor = Canvas_grafica()   # Creamos un Canvas para cada una de las gráficas.
            self.graf_pos_nor.addWidget(self.graficaPosNor)     #Agregamos la gráfica al widget.
            self.graficaPosNor.graficarPosicionNormal(pos, t)   # Trabajamos con la gráfica

            self.graficaVelNor = Canvas_grafica2() 
            self.graf_vel_nor.addWidget(self.graficaVelNor)
            self.graficaVelNor.graficarVelocidadNormal(pos, vel, t)  

            self.graficaAceNor = Canvas_grafica3()
            self.graf_ace_nor.addWidget(self.graficaAceNor)
            self.graficaAceNor.graficarAceleracionNormal(pos, ace, t)

            self.hilo_t = Hilo()    # Creamos un Hilo para cambiar los valores en el número LCD.
            self.hilo_t.nuevo_t.connect(self.displayTime)   # Función para ir cambiando los valores del cronómetro.
            self.hilo_t.start() # Inicia el hilo

            self.hilo_vel = Hilo2()
            self.hilo_vel.nueva_vel.connect(self.displayVel)    # Función para ir cambiando los valores del velocímetro.
            self.hilo_vel.start()

            self.hilo_ace = Hilo3()
            self.hilo_ace.nueva_ace.connect(self.displayAce)    # Función para ir cambiando los valores del acelerómetro.
            self.hilo_ace.start()

    #-------- Función para la graficación (FIN) -----------------------------------

    #-------- Funciónes para los medidores ----------------------------------------
    def displayTime(self, nuevo_t):
        self.lcd_tiempo.display(nuevo_t)    # Muestra el valor en el número LCD de tiempo.

    def displayVel(self, nueva_vel):
        self.lcd_vel.display(nueva_vel)     # Muestra el valor en el número LCD de velocidad.

    def displayAce(self, nueva_ace):
        self.lcd_ace.display(nueva_ace)     # Muestra el valor en el número LCD de aceleración.
    #-------- Funciónes para los medidores (FIN) ----------------------------------

#/////////////////// Clase Thread para el cronómetro /////////////////////////////////#
# No es posible crearlo en un archivo a parte, dado a la dificultad de pasar las variables
class Hilo(QThread):
    nuevo_t = pyqtSignal(float)     #señal que toma el valor del tiempo

    def __init__(self):
        super(Hilo, self).__init__()

    #Comienza el hilo y lo configuramos
    def run(self):
        i = 0
        while i < len(t):   # Ciclo en el que cambiamos los valores del cronómetro.
            self.nuevo_t.emit(t[i])
            i += 1
            if (i == len(t)-1):
                i = 0
            time.sleep(0.1)
#/////////////////// Clase Thread para el cronómetro (FIN) ///////////////////////////#

#/////////////////// Clase Thread para el velocímetro /////////////////////////////////#
class Hilo2(QThread):
    nueva_vel = pyqtSignal(float)   #señal que toma el valor de la velocidad

    def __init__(self):
        super(Hilo2, self).__init__()

    #Comienza el hilo y lo configuramos
    def run(self):
        i = 0
        while i < len(vel):     # Ciclo en el que cambiamos los valores del velocímetro.
            self.nueva_vel.emit(vel[i])
            i += 1
            if (i == len(vel)-1):
                i = 0
            time.sleep(0.1)
#/////////////////// Clase Thread para el velocímetro (FIN) ///////////////////////////#

#/////////////////// Clase Thread para el acelerómetro /////////////////////////////////#
class Hilo3(QThread):
    nueva_ace = pyqtSignal(float)   #señal que toma el valor de la aceleración

    def __init__(self):
        super(Hilo3, self).__init__()

    #Comienza el hilo y lo configuramos
    def run(self):
        i = 0
        while i < len(ace):     # Ciclo en el que cambiamos los valores del acelerómetro.
            self.nueva_ace.emit(ace[i])
            i += 1
            if (i == len(ace)-1):
                i = 0
            time.sleep(0.1)
#/////////////////// Clase Thread para el acelerómetro (FIN) ///////////////////////////#
        
#------------- Abre la aplicación ---------------------------------
if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
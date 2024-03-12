import sys
from PyQt5 import uic, QtWidgets
#from PyQt5.QtWidgets import QMessageBox ## Para las ventanas de errores
#from PyQt5.QtGui import QMovie ## Para producir gifs

import sympy as sym ## Trabajo con los polinomios
import matplotlib.pyplot as plt ## Creación de gráficas
import numpy as np
import webbrowser as wb ## Abrir archivos

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # Juntar matplotlib con las interfaces de Qt Designer
from sympy import * ## Operaciones con el polinomio (derivadas, integrales, sustituciones)
from matplotlib.animation import FuncAnimation #Animaciones de las gráficas

qtCreatorFile = "Practica01.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #------------- NUEVAS APLICACIONES EN LA INTERFAZ ---------------------------------------------------------#

        self.pushButton_cerrar.clicked.connect(self.cerrarVentana) # Función del botón cerrar.
        self.bt_insertarUsuario.clicked.connect(self.insertarUsuario) # Ingreso de Usuario.
        self.bt_grado.clicked.connect(self.obtenerGrado) # Obtener grado y constantes.
        self.bt_graficar.clicked.connect(self.graficacion) # Inicio de la graficación.
        self.pb_abrir_graf01.clicked.connect(self.ver_graf_01) # Abrir el gif de la gráfica de posiciones.
        self.pb_abrir_graf02.clicked.connect(self.ver_graf_02) # Abrir el gif de la gráfica de posiciones con vectores.
        self.pb_abrir_graf03.clicked.connect(self.ver_graf_03)  # Abrir el gif de la gráfica de velocidades.
        self.pb_abrir_graf04.clicked.connect(self.ver_graf_04)  # Abrir el gif de la gráfica de velocidades con vectores.
        self.pb_abrir_graf05.clicked.connect(self.ver_graf_05)  # Abrir el gif de la gráfica de aceleraciones.
        self.pb_abrir_graf06.clicked.connect(self.ver_graf_06)  # Abrir el gif de la gráfica de aceleraciones con vectores.

    #----------------- NUEVAS FUNCIONES ---------------------------------------------------------------------------#

    #-------- Función de cerrar----------------------------------------------
    def cerrarVentana(self):  
        quit()
    #-------- Función de cerrar (FIN) ---------------------------------------

    #-------- Función para Ingresar Usuario ---------------------------------
    def insertarUsuario(self):  ##
        usuario_nuevo = self.usuario.text()     # Tranforma el texto insertado en el espacio usuario_nuevo
        usuario_saludo = "Bienvenido " + usuario_nuevo + "."    
        self.saludo.setText(usuario_saludo)     # Inserta el texto en el espacio de saludo

        self.usuario.setEnabled(False)              #Para habilitar o deshabilitar los botones al avanzar en el proceso
        self.bt_insertarUsuario.setEnabled(False)
        self.spin_grado.setEnabled(True)
        self.spin_gradoY.setEnabled(True)
        self.bt_grado.setEnabled(True)
    #-------- Función para Ingresar Usuario (FIN) ---------------------------

    #-------- Función para el grado y las constantes ------------------------
    def obtenerGrado(self): 
        grado_poli = int(self.spin_grado.text())  # Toma el valor del boton spin_grado 
        grado_poliY = int(self.spin_gradoY.text())  # Toma el valor del boton spin_gradoY 

        if grado_poli == 2:   # En caso de escoger un polinomio de grado 2
                self.dSpinBox_00.setEnabled(True)    # Habilita botones
                self.dSpinBox_01.setEnabled(True)
                self.dSpinBox_02.setEnabled(True)
                self.dSpinBox_03.setEnabled(False)
                self.dSpinBox_04.setEnabled(False)
                self.dSpinBox_05.setEnabled(False)
                self.dSpinBox_00.setMinimum(-50)       # Pone un limite para los botones de las constantes
                self.dSpinBox_01.setMinimum(-50)
                self.dSpinBox_02.setMinimum(-50)    ## No debe ser 0 en este caso
                self.dSpinBox_03.setMinimum(-50)
                self.dSpinBox_04.setMinimum(-50)
                self.dSpinBox_05.setMinimum(-50)
                self.dSpinBox_00.setProperty("value", 0)     # Regresa los botones a sus valores de default (0)
                self.dSpinBox_01.setProperty("value", 0)
                self.dSpinBox_03.setProperty("value", 0)
                self.dSpinBox_04.setProperty("value", 0)
                self.dSpinBox_05.setProperty("value", 0)

        elif grado_poli == 3:    # En caso de escoger un polinomio de grado 3
                self.dSpinBox_00.setEnabled(True)    # Habilita botones
                self.dSpinBox_01.setEnabled(True)
                self.dSpinBox_02.setEnabled(True)
                self.dSpinBox_03.setEnabled(True)
                self.dSpinBox_04.setEnabled(False)
                self.dSpinBox_05.setEnabled(False)
                self.dSpinBox_00.setMinimum(-50)       # Pone un limite para los botones de las constantes
                self.dSpinBox_01.setMinimum(-50)
                self.dSpinBox_02.setMinimum(-50)
                self.dSpinBox_03.setMinimum(-50)      ## No debe ser 0 en este caso
                self.dSpinBox_04.setMinimum(-50)
                self.dSpinBox_05.setMinimum(-50)
                self.dSpinBox_00.setProperty("value", 0)     # Regresa los botones a sus valores de default (0)
                self.dSpinBox_01.setProperty("value", 0)
                self.dSpinBox_02.setProperty("value", 0)
                self.dSpinBox_04.setProperty("value", 0)
                self.dSpinBox_05.setProperty("value", 0)

        elif grado_poli == 4:   # En caso de escoger un polinomio de grado 4
                self.dSpinBox_00.setEnabled(True)     # Habilita botones
                self.dSpinBox_01.setEnabled(True)
                self.dSpinBox_02.setEnabled(True)
                self.dSpinBox_03.setEnabled(True)
                self.dSpinBox_04.setEnabled(True)
                self.dSpinBox_05.setEnabled(False)
                self.dSpinBox_00.setMinimum(-50)       # Pone un limite para los botones de las constantes
                self.dSpinBox_01.setMinimum(-50)
                self.dSpinBox_02.setMinimum(-50)
                self.dSpinBox_03.setMinimum(-50)
                self.dSpinBox_04.setMinimum(-50)      ## No debe ser 0 en este caso
                self.dSpinBox_05.setMinimum(-50)
                self.dSpinBox_00.setProperty("value", 0) # Regresa los botones a sus valores de default (0)
                self.dSpinBox_01.setProperty("value", 0)
                self.dSpinBox_02.setProperty("value", 0)
                self.dSpinBox_03.setProperty("value", 0)
                self.dSpinBox_05.setProperty("value", 0)
                
        elif grado_poli == 5:   # En caso de escoger un polinomio de grado 5
                self.dSpinBox_00.setEnabled(True)       # Habilita botones
                self.dSpinBox_01.setEnabled(True)
                self.dSpinBox_02.setEnabled(True)
                self.dSpinBox_03.setEnabled(True)
                self.dSpinBox_04.setEnabled(True)
                self.dSpinBox_05.setEnabled(True)
                self.dSpinBox_00.setMinimum(-50)       # Pone un limite para los botones de las constantes
                self.dSpinBox_01.setMinimum(-50)
                self.dSpinBox_02.setMinimum(-50)
                self.dSpinBox_03.setMinimum(-50)
                self.dSpinBox_04.setMinimum(-50)
                self.dSpinBox_05.setMinimum(-50)      ## No debe ser 0 en este caso
                self.dSpinBox_00.setProperty("value", 0)    # Regresa los botones a sus valores de default (0)
                self.dSpinBox_01.setProperty("value", 0)
                self.dSpinBox_02.setProperty("value", 0)
                self.dSpinBox_03.setProperty("value", 0)
                self.dSpinBox_04.setProperty("value", 0)

        ## Para las constantes en Y
        if grado_poliY == 2:   # En caso de escoger un polinomio de grado 2
                self.dSpinBoxY_00.setEnabled(True)    # Habilita botones
                self.dSpinBoxY_01.setEnabled(True)
                self.dSpinBoxY_02.setEnabled(True)
                self.dSpinBoxY_03.setEnabled(False)
                self.dSpinBoxY_04.setEnabled(False)
                self.dSpinBoxY_05.setEnabled(False)
                self.dSpinBoxY_00.setMinimum(-50)       # Pone un limite para los botones de las constantes
                self.dSpinBoxY_01.setMinimum(-50)
                self.dSpinBoxY_02.setMinimum(-50)    ## No debe ser 0 en este caso
                self.dSpinBoxY_03.setMinimum(-50)
                self.dSpinBoxY_04.setMinimum(-50)
                self.dSpinBoxY_05.setMinimum(-50)
                self.dSpinBoxY_00.setProperty("value", 0)     # Regresa los botones a sus valores de default (0)
                self.dSpinBoxY_01.setProperty("value", 0)
                self.dSpinBoxY_03.setProperty("value", 0)
                self.dSpinBoxY_04.setProperty("value", 0)
                self.dSpinBoxY_05.setProperty("value", 0)

        elif grado_poliY == 3:    # En caso de escoger un polinomio de grado 3
                self.dSpinBoxY_00.setEnabled(True)    # Habilita botones
                self.dSpinBoxY_01.setEnabled(True)
                self.dSpinBoxY_02.setEnabled(True)
                self.dSpinBoxY_03.setEnabled(True)
                self.dSpinBoxY_04.setEnabled(False)
                self.dSpinBoxY_05.setEnabled(False)
                self.dSpinBoxY_00.setMinimum(-50)       # Pone un limite para los botones de las constantes
                self.dSpinBoxY_01.setMinimum(-50)
                self.dSpinBoxY_02.setMinimum(-50)
                self.dSpinBoxY_03.setMinimum(-50)      ## No debe ser 0 en este caso
                self.dSpinBoxY_04.setMinimum(-50)
                self.dSpinBoxY_05.setMinimum(-50)
                self.dSpinBoxY_00.setProperty("value", 0)     # Regresa los botones a sus valores de default (0)
                self.dSpinBoxY_01.setProperty("value", 0)
                self.dSpinBoxY_02.setProperty("value", 0)
                self.dSpinBoxY_04.setProperty("value", 0)
                self.dSpinBoxY_05.setProperty("value", 0)

        elif grado_poliY == 4:   # En caso de escoger un polinomio de grado 4
                self.dSpinBoxY_00.setEnabled(True)     # Habilita botones
                self.dSpinBoxY_01.setEnabled(True)
                self.dSpinBoxY_02.setEnabled(True)
                self.dSpinBoxY_03.setEnabled(True)
                self.dSpinBoxY_04.setEnabled(True)
                self.dSpinBoxY_05.setEnabled(False)
                self.dSpinBoxY_00.setMinimum(-50)       # Pone un limite para los botones de las constantes
                self.dSpinBoxY_01.setMinimum(-50)
                self.dSpinBoxY_02.setMinimum(-50)
                self.dSpinBoxY_03.setMinimum(-50)
                self.dSpinBoxY_04.setMinimum(-50)      ## No debe ser 0 en este caso
                self.dSpinBoxY_05.setMinimum(-50)
                self.dSpinBoxY_00.setProperty("value", 0) # Regresa los botones a sus valores de default (0)
                self.dSpinBoxY_01.setProperty("value", 0)
                self.dSpinBoxY_02.setProperty("value", 0)
                self.dSpinBoxY_03.setProperty("value", 0)
                self.dSpinBoxY_05.setProperty("value", 0)
                
        elif grado_poliY == 5:   # En caso de escoger un polinomio de grado 5
                self.dSpinBoxY_00.setEnabled(True)       # Habilita botones
                self.dSpinBoxY_01.setEnabled(True)
                self.dSpinBoxY_02.setEnabled(True)
                self.dSpinBoxY_03.setEnabled(True)
                self.dSpinBoxY_04.setEnabled(True)
                self.dSpinBoxY_05.setEnabled(True)
                self.dSpinBoxY_00.setMinimum(-50)       # Pone un limite para los botones de las constantes
                self.dSpinBoxY_01.setMinimum(-50)
                self.dSpinBoxY_02.setMinimum(-50)
                self.dSpinBoxY_03.setMinimum(-50)
                self.dSpinBoxY_04.setMinimum(-50)
                self.dSpinBoxY_05.setMinimum(-50)      ## No debe ser 0 en este caso
                self.dSpinBoxY_00.setProperty("value", 0)    # Regresa los botones a sus valores de default (0)
                self.dSpinBoxY_01.setProperty("value", 0)
                self.dSpinBoxY_02.setProperty("value", 0)
                self.dSpinBoxY_03.setProperty("value", 0)
                self.dSpinBoxY_04.setProperty("value", 0)

        self.bt_graficar.setEnabled(True)   # Habilita el boton de bt_graficar
    #-------- Función para el grado y las constantes (FIN) -------------------

    #-------- Función para la graficación ------------------------------------
    def graficacion(self):
        self.spin_grado.setEnabled(False)   # Deshabilita los botones del paso anterior
        self.spin_gradoY.setEnabled(False)
        self.bt_grado.setEnabled(False)

        ## Creación de polinomio
        sym.init_printing()     # Para que funciones las variables en los polinomios
        x, y =symbols("x y")     # Declarando la variable "x"
        c00 = self.dSpinBox_00.text()    # Tomamos valores de las constantes en los spinbox
        c01 = self.dSpinBox_01.text()
        c02 = self.dSpinBox_02.text() 
        c03 = self.dSpinBox_03.text()
        c04 = self.dSpinBox_04.text()
        c05 = self.dSpinBox_05.text()
        cY00 = self.dSpinBoxY_00.text()    # Tomamos valores de las constantes en los spinbox
        cY01 = self.dSpinBoxY_01.text()
        cY02 = self.dSpinBoxY_02.text() 
        cY03 = self.dSpinBoxY_03.text()
        cY04 = self.dSpinBoxY_04.text()
        cY05 = self.dSpinBoxY_05.text()
        if float(c05) != 0:       # Creamos el polinomio según el grado y constantes seleccionadas, solo para 2 a 5 constantes
            fx = c05+"*"+str(x**5) + " + " + c04+"*"+str(x**4) + " + " + c03+"*"+str(x**3) + " + " + c02+"*"+str(x**2) + " + " + c01+"*"+str(x**1) + " + " + c00
        elif float(c04) != 0:
            fx = c04+"*"+str(x**4) + " + " + c03+"*"+str(x**3) + " + " + c02+"*"+str(x**2) + " + " + c01+"*"+str(x**1) + " + " + c00
        elif float(c03) != 0:
            fx = c03+"*"+str(x**3) + " + " + c02+"*"+str(x**2) + " + " + c01+"*"+str(x**1) + " + " + c00
        elif float(c02) != 0:
            fx = c02+"*"+str(x**2) + " + " + c01+"*"+str(x**1) + " + " + c00

        if float(cY05) != 0:       # Creamos el polinomio según el grado y constantes seleccionadas, solo para 2 a 5 constantes
            fY = cY05+"*"+str(y**5) + " + " + cY04+"*"+str(y**4) + " + " + cY03+"*"+str(y**3) + " + " + cY02+"*"+str(y**2) + " + " + cY01+"*"+str(y**1) + " + " + cY00
        elif float(cY04) != 0:
            fy = cY04+"*"+str(y**4) + " + " + cY03+"*"+str(y**3) + " + " + cY02+"*"+str(y**2) + " + " + cY01+"*"+str(y**1) + " + " + cY00
        elif float(cY03) != 0:
            fy = cY03+"*"+str(y**3) + " + " + cY02+"*"+str(y**2) + " + " + cY01+"*"+str(y**1) + " + " + cY00
        elif float(cY02) != 0:
            fy = cY02+"*"+str(y**2) + " + " + cY01+"*"+str(y**1) + " + " + cY00

        self.polinomio.setText(str(fx))     # Asigna el polinomio al recuadro llamado polinomio
        self.polinomioY.setText(str(fy))     # Asigna el polinomio al recuadro llamado polinomioY
        self.bt_graficar.setEnabled(False)  # Deshabilita el botón de graficar.

        ##Creación y llenado de la tabla de Velocidades
        # La velocidad es la primera derivada de nuestro polinomio.
        fdx = sym.diff(fx,x,1)  # Derivamos el polinomioX.
        fdy = sym.diff(fy,y,1)  # Derivamos el polinomioY.
        vel = []        # Lista para los valores de velocidad en X
        velY = []        # Lista para los valores de velocidad en Y
        t = []          # Lista para los valores de tiempo
        for i in range(0,20, 1):    # Hacemos las 20 repeticiones para guardar los valores en la tabla
            t.append(i)     # Ingresa los valores a la lista "t"
            vel.append(fdx.subs(x,i))   # Ingresa los valores a la lista "vel", haciendo las sustituciones en el polinomio
            velY.append(fdy.subs(y,i))   # Ingresa los valores a la lista "vel", haciendo las sustituciones en el polinomio
            self.tabla_vel.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i)))    # Mete los valores a la tabla llamada "tabla_vel" en la columna Tiempo
            self.tabla_vel.setItem(i, 1, QtWidgets.QTableWidgetItem(str(vel[i])))   # Mete los valores a la tabla llamada "tabla_vel" en la columna PosiciónX
            self.tabla_vel.setItem(i, 2, QtWidgets.QTableWidgetItem(str(velY[i])))   # Mete los valores a la tabla llamada "tabla_vel" en la columna PosiciónY

        ##Creación y llenado de la tabla de Posiciones
        # La posición es la integral de la velocidad o nuestro polinomio inicial.
        pos = []    # Lista para guardar los valores de posiciónX
        posY = []    # Lista para guardar los valores de posiciónY
        for k in range(0,20, 1):
            fdp = integrate(fdx)    # Realiza la integral de nuestra función de velocidad en X "fdx"
            fdpy = integrate(fdy)   # Realiza la integral de nuestra función de velocidad en Y "fdy"
            pos.append(fdp.subs(x,k))   # Ingresa los valores a la lista "pos", haciendo las sustituciones en el polinomio de X
            posY.append(fdpy.subs(y,k))   # Ingresa los valores a la lista "posY", haciendo las sustituciones en el polinomio de Y
            self.tabla_pos.setItem(k, 0, QtWidgets.QTableWidgetItem(str(k)))    # Mete los valores a la tabla llamada "tabla_pos" en la columna Tiempo
            self.tabla_pos.setItem(k, 1, QtWidgets.QTableWidgetItem(str(pos[k])))   # Mete los valores a la tabla llamada "tabla_pos" en la columna PosiciónX
            self.tabla_pos.setItem(k, 2, QtWidgets.QTableWidgetItem(str(posY[k])))   # Mete los valores a la tabla llamada "tabla_pos" en la columna PosiciónY

        ##Creación y llenado de la tabla de Aceleraciones
        # La aceleración es la segunda derivada de nuestro polinomio o la derivada de la velocidad.
        fdx2 = sym.diff(fdx,x,1)    # realizamos la derivada de la velocidad en X.
        fdy2 = sym.diff(fdy,y,1)    # realizamos la derivada de la velocidad en Y.
        ace = []    # Lista para guardar los valores de la aceleración en X
        aceY = []    # Lista para guardar los valores de la aceleración en Y
        for j in range(0,20, 1):
            ace.append(fdx2.subs(x,j))  # Ingresa los valores a la lista "ace", haciendo las sustituciones en el polinomio
            aceY.append(fdy2.subs(y,j))  # Ingresa los valores a la lista "ace", haciendo las sustituciones en el polinomio
            self.tabla_ace.setItem(j, 0, QtWidgets.QTableWidgetItem(str(j)))    # Mete los valores a la tabla llamada "tabla_ace" en la columna Tiempo
            self.tabla_ace.setItem(j, 1, QtWidgets.QTableWidgetItem(str(ace[j])))   # Mete los valores a la tabla llamada "tabla_ace" en la columna AceleraciónX
            self.tabla_ace.setItem(j, 2, QtWidgets.QTableWidgetItem(str(aceY[j])))   # Mete los valores a la tabla llamada "tabla_ace" en la columna AceleraciónY

        ##Distancia Total
        # se obtiene con la integral del polinomio de la velocidad
        desplazamiento = integrate(fdx, (x, float(t[0]), float(t[19])))     # realiza la integran definida en el tiempo definido
        self.distancia.setText(str(desplazamiento))     # Asigna el valor al recuadro "distancia"

        ##Graficación
        # Dado que Qt Designer no cuenta con un botón específico para matplotlib, debemos crear una nueva clase y agregar nuevas funciones a un Layout de la aplicación.
        self.graficaPosNor = Canvas_grafica()   # Creamos un Canvas para cada una de las gráficas.
        self.graficaVelNor = Canvas_grafica()   
        self.graficaAceNor = Canvas_grafica()
        self.graficaPosVec = Canvas_grafica()
        self.graficaVelVec = Canvas_grafica()
        self.graficaAceVec = Canvas_grafica()

        self.graficaPosNor.graficarPosicionNormal(pos, posY)       # Hacemos la graficación según lo que buscamos
        self.graficaVelNor.graficarVelocidadNormal(vel, velY)
        self.graficaAceNor.graficarAceleracionNormal(ace, aceY)
        self.graficaPosVec.graficarPosicionVectorVel(pos, vel, posY, velY)     # Se mueve de posición para evitar problemas con la función plt.arrow
        self.graficaVelVec.graficarPosicionVectorAce(pos, ace, posY, aceY)
        self.graficaAceVec.graficarPosicionVectores(pos, vel, ace, posY, velY, aceY)
        

        self.pb_abrir_graf01.setEnabled(True)  # Habilita el botón de ver nuestras gráficas con animaciones
        self.pb_abrir_graf02.setEnabled(True)  
        self.pb_abrir_graf03.setEnabled(True)  
        self.pb_abrir_graf04.setEnabled(True)  
        self.pb_abrir_graf05.setEnabled(True)  
        self.pb_abrir_graf06.setEnabled(True)  

    #-------- Funciónes para abrir los Gif ----------------------------------------
    
    def ver_graf_01(self):
        wb.open_new('Practica01_grafs\Posicion01.gif')

    def ver_graf_02(self):
        wb.open_new('Practica01_grafs\PosicionVectVel.gif')

    def ver_graf_03(self):
        wb.open_new('Practica01_grafs\Velocidad01.gif')

    def ver_graf_04(self):
        wb.open_new('Practica01_grafs\PosicionVectAce.gif')

    def ver_graf_05(self):
        wb.open_new('Practica01_grafs\Aceleracion01.gif')

    def ver_graf_06(self):
        wb.open_new('Practica01_grafs\PosicionVectores.gif')

    #-------- Funciónes para abrir los Gif (FIN) ----------------------------------

    #-------- Función para la graficación (FIN) -----------------------------------
        
#------------ Clase para el Canvas ----------------------------------------------------------------------------------#
class Canvas_grafica(FigureCanvas):
    #------------------ Función Inicial------------------------------------------
    def __init__(self, figure=None):

        self.fig, self.ax = plt.subplots()  # Se crea la tabla
        super().__init__(self.fig)

    #------------ Grafica de Posición (Puntos) ----------------------------------
    def graficarPosicionNormal(self, pos01, posY01):    # Se piden las variables de otra clase para poder trabajarlos.
        x_data1 = []    # Se crea un array vacio para insertar los valores de la lista "tiem01" -> "t"
        y_data1 = []    # Se crea un array vacio para insertar los valores de la lista "pos01" -> "pos"

        self.ax.set_title('Gráfica de Posiciones ', loc = "center", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        self.ax.set_xlabel("PosiciónX", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("PosiciónY", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})     # Inserta un nombre al eje Y
        self.ax.grid(axis = 'y', color = 'gray', linestyle = 'dashed')  # Asigna la cudarícula

        if float(pos01[19]) > 0:        # Ajusta los ejes en caso de tener valores negativos
            self.ax.set_xlim(float(-pos01[19]), float(pos01[19]))     # Inserta límites al eje X para los valores positivos
        else:
            self.ax.set_xlim(float(pos01[19]), float(-pos01[19]))     # Inserta límites al eje X para los valores negativos

        if float(posY01[19]) > 0:        # Ajusta los ejes en caso de tener valores negativos
            self.ax.set_ylim(float(-posY01[19]), float(posY01[19]))     # Inserta límites al eje Y para los valores positivos
        else:
            self.ax.set_ylim(float(posY01[19]), float(-posY01[19]))     # Inserta límites al eje Y para los valores negativos

        line, = self.ax.plot(0, 0, color = 'red', marker = 'o')  # Grafica los puntos con "o" (círculos)

        def animation_frame_Pos01(i):     # Función para realizar los frames de la animación
            x_data1.append(float(pos01[i]))  # Inserta punto a punto los valores a las listas vacias.
            y_data1.append(float(posY01[i]))

            line.set_xdata(x_data1)
            line.set_ydata(y_data1)
            return line,

        animationPos01 = FuncAnimation(self.fig, func=animation_frame_Pos01, frames=np.arange(0, 19, 1), interval=200, repeat = False) # Función para aplicar la animación
        animationPos01.save('Practica01_grafs\Posicion01.gif')   # Guarda la animación en un archivo de tipo ".gif"
    #------------ Grafica de Posición (FIN) -------------------------------------

    #------------ Grafica de Posición (Vectores) --------------------------------          
    def graficarPosicionVectorVel(self, pos01, vel01, posY01, velY01):
        x_data01 = []
        y_data01 = []
        
        self.ax.set_title('Gráfica de Posiciones (Vectores de Velocidad)', loc = "center", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'}) # Título de la Gráfica
        self.ax.set_xlabel("X", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("Y", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})  # Inserta un nombre al eje Y
        self.ax.grid(axis = 'y', color = 'gray', linestyle = 'dashed')  # Asigna la cudarícula
        plt.axis([0, float(pos01[19]), 0, float(posY01[19])])   # Asigna los límite a las gráfica
        plt.axis('on')

        if float(pos01[19]) > 0:        # Ajusta los ejes en caso de tener valores negativos
            self.ax.set_xlim(float(-pos01[19]), float(pos01[19]))     # Inserta límites al eje X para los valores positivos
        else:
            self.ax.set_xlim(float(pos01[19]), float(-pos01[19]))     # Inserta límites al eje X para los valores negativos

        if float(posY01[19]) > 0:        # Ajusta los ejes en caso de tener valores negativos
            self.ax.set_ylim(float(-posY01[19]), float(posY01[19]))     # Inserta límites al eje Y para los valores positivos
        else:
            self.ax.set_ylim(float(posY01[19]), float(-posY01[19]))     # Inserta límites al eje Y para los valores negativos

        line, = self.ax.plot(0, 0, color = 'purple', marker = 'v')  # Grafica

        for i in range(0,19):   # Se realiza tantos valores hay en la tabla_pos
            self.ax.quiver(float(pos01[i]), float(posY01[i]), float(vel01[i]), float(velY01[i]), color= ['blue'])   # Vector Velocidad.

        def animation_frame_Pos02(i):     # Función para realizar los frames de la animación
            x_data01.append(float(pos01[i]))  # Inserta punto a punto los valores a las listas vacias.
            y_data01.append(float(posY01[i]))

            line.set_xdata(x_data01)
            line.set_ydata(y_data01)
            return line,

        animationPos02 = FuncAnimation(self.fig, func=animation_frame_Pos02, frames=np.arange(0, 19, 1), interval=200, repeat = False) # Función para aplicar la animación
        animationPos02.save('Practica01_grafs\PosicionVectVel.gif')   # Guarda la animación en un archivo de tipo ".gif"
    #------------ Grafica de Posición Vectores (FIN) -------------------------------

    #------------ Grafica de Velocidad (Puntos) ------------------------------------
    def graficarVelocidadNormal(self, vel01, velY01):
        x_data3 = []    # Se crea un array vacio para insertar los valores de la lista "vel01" -> "vel"
        y_data3 = []    # Se crea un array vacio para insertar los valores de la lista "velY01" -> "velY"

        self.ax.set_title('Gráfica de Velocidades ', loc = "center", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})   # Título de la Gráfica
        self.ax.set_xlabel("VelocidadX", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("VelocidadY", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})    # Inserta un nombre al eje Y
        self.ax.grid(axis = 'y', color = 'gray', linestyle = 'dashed')  # Asigna la cudarícula

        if float(vel01[19]) > 0:        # Ajusta los ejes en caso de tener valores negativos
            self.ax.set_xlim(float(-vel01[19]), float(vel01[19]))     # Inserta límites al eje X para los valores positivos
        else:
            self.ax.set_xlim(float(vel01[19]), float(-vel01[19]))     # Inserta límites al eje X para los valores negativos

        if float(velY01[19]) > 0:        # Ajusta los ejes en caso de tener valores negativos
            self.ax.set_ylim(float(-velY01[19]), float(velY01[19]))     # Inserta límites al eje Y para los valores positivos
        else:
            self.ax.set_ylim(float(velY01[19]), float(-velY01[19]))     # Inserta límites al eje Y para los valores negativos

        line, = self.ax.plot(0, 0, color = 'blue', marker = 'o')  # Grafica los puntos con "o" (círculos)

        def animation_frame_Vel01(i):     # Función para realizar los frames de la animación
            x_data3.append(float(vel01[i]))  # Inserta punto a punto los valores a las listas vacias.
            y_data3.append(float(velY01[i]))

            line.set_xdata(x_data3)
            line.set_ydata(y_data3)
            return line,

        animationVel01 = FuncAnimation(self.fig, func=animation_frame_Vel01, frames=np.arange(0, 19, 1), interval=200, repeat = False) # Función para aplicar la animación
        animationVel01.save('Practica01_grafs\Velocidad01.gif')   # Guarda la animación en un archivo de tipo ".gif"
    #------------ Grafica de Velocidad (FIN) ----------------------------------------

    #------------ Grafica de Velocidad (Vectores) -----------------------------------
    def graficarPosicionVectorAce(self, pos01, ace01, posY01, aceY01):
        x_data02 = []
        y_data02 = []

        self.ax.set_title('Gráfica de Posiciones (Vectores de Aceleración)', loc = "center", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'}) # Título de la Gráfica
        self.ax.set_xlabel("X", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("Y", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})    # Inserta un nombre al eje Y
        self.ax.grid(axis = 'y', color = 'gray', linestyle = 'dashed')  # Asigna la cudarícula
        plt.axis([0, float(pos01[19]), 0, float(posY01[19])])   # Asigna los límite a las gráfica
        plt.axis('on')

        if float(pos01[19]) > 0:        # Ajusta los ejes en caso de tener valores negativos
            self.ax.set_xlim(float(-pos01[19]), float(pos01[19]))     # Inserta límites al eje X para los valores positivos
        else:
            self.ax.set_xlim(float(pos01[19]), float(-pos01[19]))     # Inserta límites al eje X para los valores negativos

        if float(posY01[19]) > 0:        # Ajusta los ejes en caso de tener valores negativos
            self.ax.set_ylim(float(-posY01[19]), float(posY01[19]))     # Inserta límites al eje Y para los valores positivos
        else:
            self.ax.set_ylim(float(posY01[19]), float(-posY01[19]))     # Inserta límites al eje Y para los valores negativos

        line, = self.ax.plot(0, 0, color = 'pink', marker = 'v')  # Grafica 

        for i in range(0,19):   # Se realiza tantos valores hay en la tabla_vel
            self.ax.quiver(float(pos01[i]), float(posY01[i]), float(ace01[i]), float(aceY01[i]), color= ['green'])  # Hace los vectores en la gráfica
            

        def animation_frame_Vel02(i):     # Función para realizar los frames de la animación
            x_data02.append(float(pos01[i]))  # Inserta punto a punto los valores a las listas vacias.
            y_data02.append(float(posY01[i]))

            line.set_xdata(x_data02)
            line.set_ydata(y_data02)
            return line,

        animationVel02 = FuncAnimation(self.fig, func=animation_frame_Vel02, frames=np.arange(0, 19, 1), interval=200, repeat = False) # Función para aplicar la animación
        animationVel02.save('Practica01_grafs\PosicionVectAce.gif')   # Guarda la animación en un archivo de tipo ".gif"
    #------------ Grafica de Velocidad Vectores (FIN) -------------------------------

    #------------ Grafica de Aceleración (Puntos) -----------------------------------
    def graficarAceleracionNormal(self, ace01, aceY01):
        x_data5 = []    # Se crea un array vacio para insertar los valores de la lista "tiem01" -> "t"
        y_data5 = []    # Se crea un array vacio para insertar los valores de la lista "ace01" -> "ace"

        #self.ax.plot(x, y, marker = 'o')    # Grafica los puntos x & y con "o" (círculos)
        self.ax.set_title('Gráfica de Aceleraciones ', loc = "center", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'}) # Título de la Gráfica
        self.ax.set_xlabel("AceleraciónX", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})  # Inserta el nombre al eje X
        self.ax.set_ylabel("AceleraciónY", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})  # Inserta un nombre al eje Y
        self.ax.grid(axis = 'y', color = 'gray', linestyle = 'dashed')  # Asigna la cudarícula

        if float(ace01[19]) > 0:        # Ajusta los ejes en caso de tener valores negativos
            self.ax.set_xlim(float(-ace01[19]), float(ace01[19]))     # Inserta límites al eje X para los valores positivos
        else:
            self.ax.set_xlim(float(ace01[19]), float(-ace01[19]))     # Inserta límites al eje X para los valores negativos

        if float(aceY01[19]) > 0:        # Ajusta los ejes en caso de tener valores negativos
            self.ax.set_ylim(float(-aceY01[19]), float(aceY01[19]))     # Inserta límites al eje Y para los valores positivos
        else:
            self.ax.set_ylim(float(aceY01[19]), float(-aceY01[19]))     # Inserta límites al eje Y para los valores negativos

        line, = self.ax.plot(0, 0, color = 'green', marker = 'o')  # Grafica los puntos con "o" (círculos)

        def animation_frame_Ace01(i):     # Función para realizar los frames de la animación
            x_data5.append(float(ace01[i]))  # Inserta punto a punto los valores a las listas vacias.
            y_data5.append(float(aceY01[i]))

            line.set_xdata(x_data5)
            line.set_ydata(y_data5)
            return line,

        animationAce01 = FuncAnimation(self.fig, func=animation_frame_Ace01, frames=np.arange(0, 19, 1), interval=200, repeat = False) # Función para aplicar la animación
        animationAce01.save('Practica01_grafs\Aceleracion01.gif')   # Guarda la animación en un archivo de tipo ".gif"s
    #------------ Grafica de Aceleración (FIN) --------------------------------------

    #------------ Grafica de Aceleración (Vectores) ---------------------------------
    def graficarPosicionVectores(self, pos01, vel01, ace01, posY01, velY01, aceY01):
        x_data03 = []
        y_data03 = []

        self.ax.set_title('Gráfica de Vectores (Velocidad y Aceleración)', loc = "center", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})   # Título de la Gráfica
        self.ax.set_xlabel("X", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})  # Inserta el nombre al eje X
        self.ax.set_ylabel("Y", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta un nombre al eje Y
        self.ax.grid(axis = 'y', color = 'gray', linestyle = 'dashed')  # Asigna la cuadrícula
        plt.axis([0, float(pos01[19]), 0, float(posY01[19])])    # Asigna los límite a las gráfica
        plt.axis('on')

        if float(pos01[19]) > 0:        # Ajusta los ejes en caso de tener valores negativos
            self.ax.set_xlim(float(-pos01[19]), float(pos01[19]))     # Inserta límites al eje X para los valores positivos
        else:
            self.ax.set_xlim(float(pos01[19]), float(-pos01[19]))     # Inserta límites al eje X para los valores negativos

        if float(posY01[19]) > 0:        # Ajusta los ejes en caso de tener valores negativos
            self.ax.set_ylim(float(-posY01[19]), float(posY01[19]))     # Inserta límites al eje Y para los valores positivos
        else:
            self.ax.set_ylim(float(posY01[19]), float(-posY01[19]))     # Inserta límites al eje Y para los valores negativos

        line, = self.ax.plot(0, 0, color = 'brown', marker = 'v')  # Grafica 

        for i in range(0,19):   # Se realiza tantos valores hay en la tabla_vel
            self.ax.quiver(float(pos01[i]), float(posY01[i]), float(vel01[i]), float(velY01[i]), color= ['red'])     # Hace los vectores en la gráfica
            self.ax.quiver(float(pos01[i]), float(posY01[i]), float(ace01[i]), float(aceY01[i]), color= ['green'])  # Hace los vectores en la gráfica

        def animation_frame_Ace02(i):     # Función para realizar los frames de la animación
            x_data03.append(float(pos01[i]))  # Inserta punto a punto los valores a las listas vacias.
            y_data03.append(float(posY01[i]))

            line.set_xdata(x_data03)
            line.set_ydata(y_data03)
            return line,

        animationVel02 = FuncAnimation(self.fig, func=animation_frame_Ace02, frames=np.arange(0, 19, 1), interval=200, repeat = False) # Función para aplicar la animación
        animationVel02.save('Practica01_grafs\PosicionVectores.gif')   # Guarda la animación en un archivo de tipo ".gif"
    #------------ Grafica de Velocidad Vectores (FIN) -------------------------------

        
#------------- Abre la aplicación ---------------------------------
if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
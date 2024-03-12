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
        #self.pb_abrir_graf02.clicked.connect(self.ver_graf_02) # Abrir el gif de la gráfica de posiciones con vectores.
        self.pb_abrir_graf03.clicked.connect(self.ver_graf_03)  # Abrir el gif de la gráfica de velocidades.
        #self.pb_abrir_graf04.clicked.connect(self.ver_graf_04)  # Abrir el gif de la gráfica de velocidades con vectores.
        self.pb_abrir_graf05.clicked.connect(self.ver_graf_05)  # Abrir el gif de la gráfica de aceleraciones.
        #self.pb_abrir_graf06.clicked.connect(self.ver_graf_06)  # Abrir el gif de la gráfica de aceleraciones con vectores.

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
        self.bt_grado.setEnabled(True)
    #-------- Función para Ingresar Usuario (FIN) ---------------------------

    #-------- Función para el grado y las constantes ------------------------
    def obtenerGrado(self): 
        grado_poli = int(self.spin_grado.text())  # Toma el valor del boton spin_grado 

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

        self.bt_graficar.setEnabled(True)   # Habilita el boton de bt_graficar
    #-------- Función para el grado y las constantes (FIN) -------------------

    #-------- Función para la graficación ------------------------------------
    def graficacion(self):
        self.spin_grado.setEnabled(False)   # Deshabilita los botones del paso anterior
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
        vel = []        # Lista para los valores de velocidad en X
        t = []          # Lista para los valores de tiempo
        for i in range(0, 50, 1):    # Hacemos las 20 repeticiones para guardar los valores en la tabla
            t.append(i)     # Ingresa los valores a la lista "t"
            vel.append(fdx.subs(x,i/10))   # Ingresa los valores a la lista "vel", haciendo las sustituciones en el polinomio
            self.tabla_vel.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i/10)))    # Mete los valores a la tabla llamada "tabla_vel" en la columna Tiempo
            self.tabla_vel.setItem(i, 1, QtWidgets.QTableWidgetItem(str(vel[i])))   # Mete los valores a la tabla llamada "tabla_vel" en la columna Posición


        ##Creación y llenado de la tabla de Posiciones
        # La posición es la integral de la velocidad o nuestro polinomio inicial.
        pos = []    # Lista para guardar los valores de posiciónX
        for k in range(0, 50, 1):
            fdp = integrate(fdx)    # Realiza la integral de nuestra función de velocidad en X "fdx"
            pos.append(fdp.subs(x,k/10))   # Ingresa los valores a la lista "pos", haciendo las sustituciones en el polinomio de X
            self.tabla_pos.setItem(k, 0, QtWidgets.QTableWidgetItem(str(k/10)))    # Mete los valores a la tabla llamada "tabla_pos" en la columna Tiempo
            self.tabla_pos.setItem(k, 1, QtWidgets.QTableWidgetItem(str(pos[k])))   # Mete los valores a la tabla llamada "tabla_pos" en la columna Posición

        ##Creación y llenado de la tabla de Aceleraciones
        # La aceleración es la segunda derivada de nuestro polinomio o la derivada de la velocidad.
        fdx2 = sym.diff(fdx,x,1)    # realizamos la derivada de la velocidad en X.
        ace = []    # Lista para guardar los valores de la aceleración en X
        for j in range(0, 50, 1):
            ace.append(fdx2.subs(x,j))  # Ingresa los valores a la lista "ace", haciendo las sustituciones en el polinomio
            self.tabla_ace.setItem(j, 0, QtWidgets.QTableWidgetItem(str(j/10)))    # Mete los valores a la tabla llamada "tabla_ace" en la columna Tiempo
            self.tabla_ace.setItem(j, 1, QtWidgets.QTableWidgetItem(str(ace[j])))   # Mete los valores a la tabla llamada "tabla_ace" en la columna Aceleración

        ##Distancia Total
        # se obtiene con la integral del polinomio de la velocidad
        #desplazamiento = integrate(fdx, (x, float(t[0]), float(t[19])))     # realiza la integran definida en el tiempo definido
        #self.distancia.setText(str(desplazamiento))     # Asigna el valor al recuadro "distancia"

        ##Graficación
        # Dado que Qt Designer no cuenta con un botón específico para matplotlib, debemos crear una nueva clase y agregar nuevas funciones a un Layout de la aplicación.
        self.graficaPosNor = Canvas_grafica()   # Creamos un Canvas para cada una de las gráficas.
        self.graficaVelNor = Canvas_grafica()   
        self.graficaAceNor = Canvas_grafica()
        #self.graficaPosVec = Canvas_grafica()
        #self.graficaVelVec = Canvas_grafica()
        #self.graficaAceVec = Canvas_grafica()

        self.graficaPosNor.graficarPosicionNormal(pos, t)       # Hacemos la graficación según lo que buscamos
        self.graficaVelNor.graficarVelocidadNormal(vel, t)
        self.graficaAceNor.graficarAceleracionNormal(ace, t)
        #self.graficaPosVec.graficarPosicionVectorVel(pos, vel, posY, velY)     # Se mueve de posición para evitar problemas con la función plt.arrow
        #self.graficaVelVec.graficarPosicionVectorAce(pos, ace, posY, aceY)
        #self.graficaAceVec.graficarPosicionVectores(pos, vel, ace, posY, velY, aceY)
        

        self.pb_abrir_graf01.setEnabled(True)  # Habilita el botón de ver nuestras gráficas con animaciones
        #self.pb_abrir_graf02.setEnabled(True)  
        self.pb_abrir_graf03.setEnabled(True)  
        #self.pb_abrir_graf04.setEnabled(True)  
        self.pb_abrir_graf05.setEnabled(True)  
        #self.pb_abrir_graf06.setEnabled(True)  

    #-------- Funciónes para abrir los Gif ----------------------------------------
    
    def ver_graf_01(self):
        wb.open_new('Practica01_grafs\Posicion01.gif')

    def ver_graf_03(self):
        wb.open_new('Practica01_grafs\Velocidad01.gif')

    def ver_graf_05(self):
        wb.open_new('Practica01_grafs\Aceleracion01.gif')

    #-------- Funciónes para abrir los Gif (FIN) ----------------------------------

    #-------- Función para la graficación (FIN) -----------------------------------
        
#------------ Clase para el Canvas ----------------------------------------------------------------------------------#
class Canvas_grafica(FigureCanvas):
    #------------------ Función Inicial------------------------------------------
    def __init__(self, figure=None):

        self.fig, self.ax = plt.subplots()  # Se crea la tabla
        super().__init__(self.fig)

    #------------ Grafica de Posición (Puntos) ----------------------------------
    def graficarPosicionNormal(self, pos01, tiem01):    # Se piden las variables de otra clase para poder trabajarlos.
        x_data1 = []    # Se crea un array vacio para insertar los valores de la lista "tiem01" -> "t"
        y_data1 = []    # Se crea un array vacio para insertar los valores de la lista "pos01" -> "pos"

        self.ax.set_title('Gráfica de Posiciones ', loc = "center", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        self.ax.set_xlabel("PosiciónX", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("PosiciónY", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})     # Inserta un nombre al eje Y
        self.ax.grid()  # Asigna la cudarícula

        self.ax.set_ylim(-1, 1)     # Inserta límites al eje Y 

        if float(max(pos01)) > 0:        # Ajusta los ejes en caso de tener valores negativos
            self.ax.set_xlim(float(-max(pos01)), float(max(pos01)))     # Inserta límites al eje X para los valores positivos
        else:
            self.ax.set_xlim(float(max(pos01)), float(-max(pos01))) 

        #line, = self.ax.plot(0, 0, color = 'yellow', marker = 'o')  # Grafica los puntos con "o" (círculos)

        def animation_frame_Pos01(i):     # Función para realizar los frames de la animación
            x_data1.append(float(pos01[i]))  # Inserta punto a punto los valores a las listas vacias.
            y_data1.append(float(tiem01[0]))

            #if float(pos01[i]) > 0:
                #line, = self.ax.plot(0, 0, color = 'yellow', marker = '>')  # Grafica los puntos con ">" 
            if (((pos01[i]) > 0) and (pos01[i+1] >= pos01[i])):
                line, = self.ax.plot(pos01[i], 0, color = 'yellow', marker = 'o')  # Grafica los puntos con ">" 
            #elif ((pos01[i] > 0) and (pos01[i+1] < pos01[i])):
                #line, = self.ax.plot(pos01[i], 0, color = '', marker = 'o')  # Grafica los puntos con "<" 
            else:
                line, = self.ax.plot(pos01[i], 0, color = 'yellow', marker = 'o')  # Grafica los puntos con "<" 

            line.set_xdata(x_data1)
            line.set_ydata(y_data1)
            return line,   

        animationPos01 = FuncAnimation(self.fig, func=animation_frame_Pos01, frames=np.arange(0, 49, 1), interval=200, repeat = False) # Función para aplicar la animación
        animationPos01.save('Practica01_grafs\Posicion01.gif')   # Guarda la animación en un archivo de tipo ".gif"
    #------------ Grafica de Posición (FIN) -------------------------------------

    #------------ Grafica de Velocidad (Puntos) ------------------------------------
    def graficarVelocidadNormal(self, vel01, tiem01):
        x_data3 = []    # Se crea un array vacio para insertar los valores de la lista "vel01" -> "vel"
        y_data3 = []    # Se crea un array vacio para insertar los valores de la lista "velY01" -> "velY"

        self.ax.set_title('Gráfica de Velocidades ', loc = "center", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})   # Título de la Gráfica
        self.ax.set_xlabel("Velocidad", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        #self.ax.set_ylabel("VelocidadY", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})    # Inserta un nombre al eje Y
        self.ax.grid()  # Asigna la cudarícula

        self.ax.set_ylim(-1, 1)     # Inserta límites al eje Y para los valores positivos

        if float(max(vel01)) > 0:        # Ajusta los ejes en caso de tener valores negativos
            self.ax.set_xlim(float(-max(vel01)), float(max(vel01)))     # Inserta límites al eje X para los valores positivos
        else:
            self.ax.set_xlim(float(max(vel01)), float(-max(vel01))) 

        def animation_frame_Vel01(i):     # Función para realizar los frames de la animación
            x_data3.append(float(vel01[i]))  # Inserta punto a punto los valores a las listas vacias.
            y_data3.append(float(tiem01[0]))

            if (((vel01[i]) > 0) and (vel01[i+1] >= vel01[i])):
                line, = self.ax.plot(vel01[i], 0, color = 'yellow', marker = '')  # Grafica los puntos con ">" 
            elif ((vel01[i] > 0) and (vel01[i+1] < vel01[i])):
                line, = self.ax.plot(vel01[i], 0, color = 'yellow', marker = '<')  # Grafica los puntos con "<" 
            else:
                line, = self.ax.plot(vel01[i], 0, color = 'yellow', marker = '<')  # Grafica los puntos con "<" 
            
            """""
            if float(vel01[i]) > 0:
                line, = self.ax.plot(0, 0, color = 'blue', marker = '>')  # Grafica los puntos con ">" 
            else:
                line, = self.ax.plot(0, 0, color = 'green', marker = '<')  # Grafica los puntos con "<" 
            """
            line.set_xdata(x_data3)
            line.set_ydata(y_data3)
            return line,

        animationVel01 = FuncAnimation(self.fig, func=animation_frame_Vel01, frames=np.arange(0, 19, 1), interval=200, repeat = False) # Función para aplicar la animación
        animationVel01.save('Practica01_grafs\Velocidad01.gif')   # Guarda la animación en un archivo de tipo ".gif"
    #------------ Grafica de Velocidad (FIN) ----------------------------------------

    #------------ Grafica de Aceleración (Puntos) -----------------------------------
    def graficarAceleracionNormal(self, ace01, tiem01):
        x_data5 = []    # Se crea un array vacio para insertar los valores de la lista "tiem01" -> "t"
        y_data5 = []    # Se crea un array vacio para insertar los valores de la lista "ace01" -> "ace"

        #self.ax.plot(x, y, marker = 'o')    # Grafica los puntos x & y con "o" (círculos)
        self.ax.set_title('Gráfica de Aceleraciones ', loc = "center", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'}) # Título de la Gráfica
        self.ax.set_xlabel("Aceleración", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})  # Inserta el nombre al eje X
        #self.ax.set_ylabel("AceleraciónY", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})  # Inserta un nombre al eje Y
        self.ax.grid()  # Asigna la cudarícula

        self.ax.set_ylim(-1, 1)     # Inserta límites al eje Y para los valores positivos

        if float(max(ace01)) > 0:        # Ajusta los ejes en caso de tener valores negativos
            self.ax.set_xlim(float(-max(ace01)), float(max(ace01)))     # Inserta límites al eje X para los valores positivos
        else:
            self.ax.set_xlim(float(max(ace01)), float(-max(ace01))) 

        def animation_frame_Ace01(i):     # Función para realizar los frames de la animación
            x_data5.append(float(ace01[i]))  # Inserta punto a punto los valores a las listas vacias.
            y_data5.append(float(tiem01[0]))

            if float(ace01[i]) > 0:
                line, = self.ax.plot(0, 0, color = 'brown', marker = '>')  # Grafica los puntos con ">" 
            else:
                line, = self.ax.plot(0, 0, color = 'orange', marker = '<')  # Grafica los puntos con "<" 

            line.set_xdata(x_data5)
            line.set_ydata(y_data5)
            return line,

        animationAce01 = FuncAnimation(self.fig, func=animation_frame_Ace01, frames=np.arange(0, 19, 1), interval=200, repeat = False) # Función para aplicar la animación
        animationAce01.save('Practica01_grafs\Aceleracion01.gif')   # Guarda la animación en un archivo de tipo ".gif"s
    #------------ Grafica de Aceleración (FIN) --------------------------------------

        
#------------- Abre la aplicación ---------------------------------
if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
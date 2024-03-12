# Práctica 03. Coordenadas Ortogonales. (SSIS-3D)

import sys
from PyQt5 import uic, QtWidgets

import numpy as np
from Coordenadas import Canvas_Grafica

qtCreatorFile = "Practica03.ui" # Nombre del archivo aquí. Relative Path

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #------------- NUEVAS APLICACIONES --------------------------------
        
        # Para abrir los módulos deseados.
        self.button_cart_esfe.clicked.connect(self.abrir_carte_esfe)    
        self.button_esfe_cart.clicked.connect(self.abrir_esfe_carte)    

        # Para Realizar las graficaciones Cartesianas -> Esféricas
        self.button_graf_cart_grad.clicked.connect(self.graficar_carte_esfe)

        # Para Realizar las graficaciones Esféricas -> Cartesianas
        self.button_graf_esfe.clicked.connect(self.graficar_esfe_carte)

        # Para borrar las gráficas
        self.button_nueva_graf1.clicked.connect(self.nueva_graf_carte_esfe)
        self.button_nueva_graf2.clicked.connect(self.nueva_graf_esfe_carte)
        
    #----------------- NUEVAS FUNCIONES -----------------------------------

    def abrir_carte_esfe(self):   # Función para abrir el módulo de Cartesianas -> Esféricas
        self.stackedWidget_coor.setCurrentWidget(self.coor_cartesianas)
        self.stackedWidget_grafs.setCurrentWidget(self.graf_cartesianas)
        self.button_cart_esfe.setEnabled(False)
        self.button_esfe_cart.setEnabled(True)

    def abrir_esfe_carte(self):   # Función para abrir el módulo de Esféricas -> Cartesianas
        self.stackedWidget_coor.setCurrentWidget(self.coor_esfericas)
        self.stackedWidget_grafs.setCurrentWidget(self.graf_esfericas)
        self.button_cart_esfe.setEnabled(True)
        self.button_esfe_cart.setEnabled(False)

    def graficar_carte_esfe(self):     # Función para graficar Cartesianas -> Esféricas

        # Tomamos los valores
        rx = float(self.sbox_rx_gra.text())
        ry = float(self.sbox_ry_gra.text())
        rz = float(self.sbox_rz_gra.text())

        # Coordenada 'r'
        r = np.sqrt(pow(rx, 2) + pow(ry, 2) + pow(rz, 2))

        # Coordenada 'theta'
        if(rz > 0):     # z > 0
            theta = np.arctan(np.sqrt(pow(rx, 2) + pow(ry, 2))/rz)
        elif(rz < 0):   # z < 0
            theta = np.pi + np.arctan(np.sqrt(pow(rx, 2) + pow(ry, 2))/rz)
        else:           # z = 0
            if(rx == 0 and ry == 0):    # z = x = y = 0
                theta = 0
            else:                       # z = 0 and xy =! 0                   
                theta = np.pi/2
    
        # Coordenada 'phi'
        if(rx > 0 ):    # x > 0
            phi = np.arctan(ry/rx)
        elif(rx < 0):   # x < 0
            if(ry >= 0):    # x < 0 and y >= 0 
                phi = np.arctan(ry/rx) + np.pi
            elif(ry < 0):   # x < 0 and y < 0
                phi = np.arctan(ry/rx) - np.pi
        else:           # x = 0 
            if(ry > 0):     # x = 0 and y > 0
                phi = np.pi/2
            elif(ry < 0):   # x = 0 and y < 0
                phi = -np.pi/2
            else:           # x = 0 and y = 0
                phi = 0

        #Asigna los valores a las lineas
        # Valores en Radianes
        self.r_grad.setText(str(r) + " rad")
        self.theta_rad.setText(str(theta) + " rad")
        self.phi_rad.setText(str(phi) + " rad")
        # Valores en Grados
        self.theta_grad.setText(str(np.degrees(theta))+ "°")
        self.phi_grad.setText(str(np.degrees(phi))+ "°")

        # Creamos un Canvas para cada una de las gráficas.
        self.graficaCarteEsfe = Canvas_Grafica()   # Creamos un Canvas para cada una de las gráficas.
        self.graf_carte_esfe.addWidget(self.graficaCarteEsfe)     #Agregamos la gráfica al widget.
        self.graficaCarteEsfe.graficarC(rx, ry, rz, phi)   # Trabajamos con la gráfica

        #Habilitando el botón de reinicio.
        self.button_graf_cart_grad.setEnabled(False)
        self.button_nueva_graf1.setEnabled(True)
        self.button_esfe_cart.setEnabled(False)

    def graficar_esfe_carte(self):     # Función para graficar Esféricas -> Cartesianas

        r = float(self.sbox_r.text())

        if self.cBox_theta_grad.checkState() == 2:      # Arroja 2 cuando esta marcado el checkbox y 0 cuando no
            theta = np.radians(float(self.sbox_theta.text()))   # Valor de theta se convierte a radianes
        else:
            theta = float(self.sbox_theta.text()) 
        
        if self.cBox_phi_grad.checkState() == 2:    # Arroja 2 cuando esta marcado el checkbox y 0 cuando no
            phi = np.radians(float(self.sbox_phi.text()))   # Valor de phi se convierte a radianes
        else:
            phi = float(self.sbox_phi.text())   

        # Formulas de conversion
        rx = r * np.sin(theta) * np.cos(phi) + 0
        ry = r * np.sin(theta) * np.sin(phi) + 0
        rz = r * np.cos(theta) + 0

        # Asignamos los valores
        self.rx_val.setText(str(rx))
        self.ry_val.setText(str(ry))
        self.rz_val.setText(str(rz))

        # Creamos un Canvas para cada una de las gráficas.
        self.graficaEsfeCarte = Canvas_Grafica()   # Creamos un Canvas para cada una de las gráficas.
        self.graf_esfe_carte.addWidget(self.graficaEsfeCarte)     #Agregamos la gráfica al widget.
        self.graficaEsfeCarte.graficarE(rx, ry, rz, phi)   # Trabajamos con la gráfica

        #Habilitando el botón de reinicio.
        self.button_graf_esfe.setEnabled(False)
        self.button_nueva_graf2.setEnabled(True)
        self.button_cart_esfe.setEnabled(False)

    def nueva_graf_carte_esfe(self):    # Función para crear nueva gráfica en el módulo Cartesianas -> Esféricas

        self.graficaCarteEsfe.vaciar_grafica()    #Eliminamos los plt y axes existentes.   
        self.graf_carte_esfe.removeWidget(self.graficaCarteEsfe)    # Eliminamos el widget creado anterioremente
        self.graficaCarteEsfe.deleteLater()
        self.graficaCarteEsfe = None

        # Limpiamos los valores
        # Valores en Radianes
        self.r_grad.setText("")
        self.theta_rad.setText("")
        self.phi_rad.setText("")
        # Valores en Grados
        self.theta_grad.setText("")
        self.phi_grad.setText("")

        # Reactivamos el boton de graficar y los spinBox
        self.button_graf_cart_grad.setEnabled(True)
        self.button_nueva_graf1.setEnabled(False)
        self.button_esfe_cart.setEnabled(True)

    def nueva_graf_esfe_carte(self):    # Función para crear nueva gráfica en el módulo Esféricas -> Cartesianas

        self.graficaEsfeCarte.vaciar_grafica()    #Eliminamos los plt y axes existentes.   
        self.graf_esfe_carte.removeWidget(self.graficaEsfeCarte)    # Eliminamos el widget creado anterioremente
        self.graficaEsfeCarte.deleteLater()
        self.graficaEsfeCarte = None

        # Limpiamos los valores
        self.rx_val.setText("")
        self.ry_val.setText("")
        self.rz_val.setText("")

        # Cambiamos el valor de los CheckBox
        self.cBox_theta_grad.setChecked(False)
        self.cBox_phi_grad.setChecked(False)

        # Reactivamos el boton de graficar y los spinBox
        self.button_graf_esfe.setEnabled(True)
        self.button_nueva_graf2.setEnabled(False)
        self.button_cart_esfe.setEnabled(True)

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
# Uniendo todas las prácticas en una sola aplicación.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from Inicio_Practica01 import Prac01
from Inicio_Practica02 import Prac02
from Inicio_Practica03 import Prac03
from Inicio_Practica04 import Prac04
from Inicio_Practica05 import Prac05
from Inicio_Practica06 import Prac06
from Inicio_Practica07 import Prac07
from Inicio_Practica08 import Prac08
from Inicio_Practica09 import Prac09
from Inicio_Practica10 import Prac10
from Inicio_Practica11 import Prac11
from Inicio_Practica12 import Prac12
from Inicio_Practica13 import Prac13

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        loadUi('Interfaces\Inicio.ui', self)

        #------------- NUEVAS APLICACIONES --------------------------------
        self.button_seccion1.hide()
        
        self.button_cerrar.clicked.connect(self.cerrarVentana)      # Función del botón cerrar.
        self.button_seccion1.clicked.connect(self.mostrar1raSeccion)
        self.button_seccion2.clicked.connect(self.mostrar2daSeccion)
        self.button_prac_01.clicked.connect(self.abrir_prac_01)      # Función abrir practica 01.
        self.button_prac_02.clicked.connect(self.abrir_prac_02)      # Función abrir practica 02.
        self.button_prac_03.clicked.connect(self.abrir_prac_03)      # Función abrir practica 03.
        self.button_prac_04.clicked.connect(self.abrir_prac_04)      # Función abrir practica 04.
        self.button_prac_05.clicked.connect(self.abrir_prac_05)      # Función abrir practica 05.
        self.button_prac_06.clicked.connect(self.abrir_prac_06)      # Función abrir practica 06.
        self.button_prac_07.clicked.connect(self.abrir_prac_07)      # Función abrir practica 07.
        self.button_prac_08.clicked.connect(self.abrir_prac_08)      # Función abrir practica 07.
        self.button_prac_09.clicked.connect(self.abrir_prac_09)      # Función abrir practica 09.
        self.button_prac_10.clicked.connect(self.abrir_prac_10)      # Función abrir practica 10.
        self.button_prac_11.clicked.connect(self.abrir_prac_11)      # Función abrir practica 11.
        self.button_prac_12.clicked.connect(self.abrir_prac_12)      # Función abrir practica 12.
        self.button_prac_13.clicked.connect(self.abrir_prac_13)      # Función abrir practica 13.

    #----------------- NUEVAS FUNCIONES -----------------------------------

    #-------- Función de cerrar----------------------------------------------
    def cerrarVentana(self):  
        quit()
    #-------- Función de cerrar (FIN) ---------------------------------------

    def mostrar1raSeccion(self):
        self.button_seccion1.hide()
        self.button_seccion2.show()
        self.stackedWidget_pracs.setCurrentWidget(self.primera_seccion)
    
    def mostrar2daSeccion(self):
        self.button_seccion1.show()
        self.button_seccion2.hide()
        self.stackedWidget_pracs.setCurrentWidget(self.segunda_seccion)

    #-------- Función de abrir la práctica 01 -------------------------------
    def abrir_prac_01(self):
        ventana = Prac01(self)
        ventana.show()

    #-------- Función de abrir la práctica 01 (FIN) -------------------------

    #-------- Función de abrir la práctica 02 -------------------------------
    def abrir_prac_02(self):
        ventana = Prac02(self)
        ventana.show()

    #-------- Función de abrir la práctica 02 (FIN) -------------------------

    #-------- Función de abrir la práctica 03 -------------------------------
    def abrir_prac_03(self):
        ventana = Prac03(self)
        ventana.show()

    #-------- Función de abrir la práctica 03 (FIN) -------------------------

    #-------- Función de abrir la práctica 04 -------------------------------
    def abrir_prac_04(self):
        ventana = Prac04(self)
        ventana.show()

    #-------- Función de abrir la práctica 04 (FIN) -------------------------

    #-------- Función de abrir la práctica 05 -------------------------------
    def abrir_prac_05(self):
        ventana = Prac05(self)
        ventana.show()

    #-------- Función de abrir la práctica 05 (FIN) -------------------------

    #-------- Función de abrir la práctica 06 -------------------------------
    def abrir_prac_06(self):
        ventana = Prac06(self)
        ventana.show()

    #-------- Función de abrir la práctica 06 (FIN) -------------------------

    #-------- Función de abrir la práctica 07 -------------------------------
    def abrir_prac_07(self):
        ventana = Prac07(self)
        ventana.show()

    #-------- Función de abrir la práctica 07 (FIN) -------------------------

    #-------- Función de abrir la práctica 08 -------------------------------
    def abrir_prac_08(self):
        ventana = Prac08(self)
        ventana.show()

    #-------- Función de abrir la práctica 08 (FIN) -------------------------

    #-------- Función de abrir la práctica 09 -------------------------------
    def abrir_prac_09(self):
        ventana = Prac09(self)
        ventana.show()

    #-------- Función de abrir la práctica 09 (FIN) -------------------------

    #-------- Función de abrir la práctica 10 -------------------------------
    def abrir_prac_10(self):
        ventana = Prac10(self)
        ventana.show()

    #-------- Función de abrir la práctica 10 (FIN) -------------------------

    #-------- Función de abrir la práctica 11 -------------------------------
    def abrir_prac_11(self):
        ventana = Prac11(self)
        ventana.show()

    #-------- Función de abrir la práctica 11 (FIN) -------------------------

    #-------- Función de abrir la práctica 12 -------------------------------
    def abrir_prac_12(self):
        ventana = Prac12(self)
        ventana.show()

    #-------- Función de abrir la práctica 12 (FIN) -------------------------

    #-------- Función de abrir la práctica 13 -------------------------------
    def abrir_prac_13(self):
        ventana = Prac13(self)
        ventana.show()

    #-------- Función de abrir la práctica 13 (FIN) -------------------------


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
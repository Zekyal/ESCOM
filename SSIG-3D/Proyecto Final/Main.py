# Archivo principal del programa SSIG-3D

import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5 import QtCore
from PyQt5.QtWidgets import QGraphicsDropShadowEffect # Ayuda a agregar sombras a los Widgets
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve # Efectos al mostrar u ocultar los widgets
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QFileDialog # Ayuda a la selección de una carpeta
import win32com.client as win32     # Pasar datos de tabla a un excel
import numpy as np

import matplotlib as mpl        # Para ajustar un número aceptable de simulaciones de matplotlib
mpl.rc('figure', max_open_warning = 60)

from Vectores import Vectores, Vectores_Suma_Vect, Vectores_Punto_Vect, Vectores_Cruz_Vect  # Archivo para el módulo de Vectores
from Leyes_de_Newton import Primera_Ley, Segunda_Ley, Tercera_Ley     # Archivo para el módulo de Leyes de Newton
from Angulo_Solido import Angulo_Solido     # Archivo para el módulo de Ángulo Sólido
from Tiro_Parabolico import Tiro_Parabolico     # Archivo para el módulo de Tiro Parabólico
from Coordenadas_Ortogonales import Coordenadas_Cartesianas, Coordenadas_Esfericas, Coordenadas_Cilindricas     # Archivo para el módulo de Coordenadas Ortogonales
from Campo_Electrico import Campo_Electrico, Camp_Elec_Flujos, Camp_Elec_Dipolo, Camp_Elec_Potencial   # Archivo para el módulo de Campo Eléctrico
from Campo_Magnetico import Campo_Magnetico, Camp_Magne_Cables_Par, Espira_Magne, Espiras_Magnes, Dipolo_Magne_2d, Dipolo_Magne_3d  # Archivo para el módulo de Campo Magnético

# Todas las prácticas agregadas
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
from Inicio_Practica14 import Prac14
from Inicio_Practica15 import Prac15
from Inicio_Practica16 import Prac16
from Inicio_Practica17 import Prac17
from Inicio_Practica18 import Prac18
from Inicio_Practica19 import Prac19
from Inicio_Practica20 import Prac20
from Inicio_Practica21 import Prac21
from Inicio_Practica22 import Prac22
from Inicio_Practica23 import Prac23
from Inicio_Practica24 import Prac24

import Errores  # Archivo que contiene los mensajes de error.

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        loadUi('SSIG-3D.ui', self)

        #------------- NUEVAS APLICACIONES ------------------------------------------------------------------------------------------------------------------------

        #************* Estética de la Interfaz *******************************************************************************************************************#
        self.pushButton_mostrar.clicked.connect(self.mover_menu)
        self.pushButton_ocultar.clicked.connect(self.mover_menu)
        # Ocultando los botones
        self.pushButton_minimo.hide()
        self.pushButton_mostrar.hide()
        # Sombra a los Widgets
        self.sombra_frame(self.button_inicio)
        self.sombra_frame(self.combo_vect)
        self.sombra_frame(self.combo_newt)
        self.sombra_frame(self.button_parab)
        self.sombra_frame(self.combo_coor)
        self.sombra_frame(self.button_angu)
        self.sombra_frame(self.button_elec)
        self.sombra_frame(self.button_magne)
        self.sombra_frame(self.button_practicas)
        self.sombra_frame(self.button_referencias)
        self.sombra_frame(self.pushButton_ocultar)
        self.sombra_frame(self.pushButton_mostrar)
        self.sombra_frame(self.stackedWidget_central)
        self.sombra_frame(self.stackedWidget_derecha)
        # Control de la barra de títulos
        self.pushButton_minimizar.clicked.connect(self.control_minimizar)
        self.pushButton_minimo.clicked.connect(self.control_normal)
        self.pushButton_maximo.clicked.connect(self.control_maximizar)
        self.pushButton_cerrar.clicked.connect(self.control_cerrar)
        # Eliminar la barra de título
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)  
        #************* Estética de la Interfaz (FIN) ***************************************************************************************************************#

        # Mostrar páginas 
        self.button_inicio.clicked.connect(self.abrir_inicio)
        self.combo_vect.activated.connect(self.abrir_vectores)
        self.combo_newt.activated.connect(self.abrir_leyes)
        self.button_parab.clicked.connect(self.abrir_tiro_par)
        self.combo_coor.activated.connect(self.abrir_coordenadas)
        self.button_angu.clicked.connect(self.abrir_ang_sol)
        self.button_elec.clicked.connect(self.abrir_camp_elec)
        self.button_magne.clicked.connect(self.abrir_camp_magne)
        self.button_practicas.clicked.connect(self.abrir_practicas)
        self.button_referencias.clicked.connect(self.abrir_referencias)

        #************* Módulo de Inicio ****************************************************************************************************************************#

        # Ocultando el botón de cerrar sesión.
        self.button_cerrar_sesion.hide()

        # Agregar el usuario
        self.button_usuario.clicked.connect(self.insertar_usuario)

        # Cerrando Sesión
        self.button_cerrar_sesion.clicked.connect(self.cerrar_sesion)

        #************* Módulo de Inicio (FIN) **********************************************************************************************************************#

        #************* Módulo de Vectores **************************************************************************************************************************#

        # Ocultado las secciones
        self.ocultar_frame(self.frame_vect_ejemplo)
        self.ocultar_frame(self.button_guardar_vect)
        self.ocultar_frame(self.button_reiniciar_vect)
        self.ocultar_frame(self.frame_sum_vect_ejemplo)
        self.ocultar_frame(self.frame_sum_vect)
        self.ocultar_frame(self.button_guardar_sum_vect)
        self.ocultar_frame(self.button_reiniciar_sum_vect)
        self.ocultar_frame(self.frame_punto_vect)
        self.ocultar_frame(self.button_guardar_punto_vect)
        self.ocultar_frame(self.button_reiniciar_punto_vect)
        self.ocultar_frame(self.frame_cruz_vect)
        self.ocultar_frame(self.button_guardar_cruz_vect)
        self.ocultar_frame(self.button_reiniciar_cruz_vect)
        
        #Nombres de los LCD para pasar
        global val_magnitud, val_alpha, val_beta, val_gamma, val_alpha_g, val_beta_g, val_gamma_g
        val_magnitud = self.lcdNu_magnitud_vect
        val_alpha = self.lcdNu_r_alpha_vect
        val_beta = self.lcdNu_r_beta_vect
        val_gamma = self.lcdNu_r_gamma_vect
        val_alpha_g = self.lcdNu_g_alpha_vect
        val_beta_g = self.lcdNu_g_beta_vect
        val_gamma_g = self.lcdNu_g_gamma_vect

        # Ejemplo de la sección Vector
        self.button_inicio_vect.clicked.connect(self.iniciar_vector)
        self.button_realizar_vect.clicked.connect(self.realizar_vector)
        self.button_guardar_vect.clicked.connect(self.guardar_vector)
        self.button_reiniciar_vect.clicked.connect(self.reiniciar_vector)

        # Ejemplo de la sección de "Suma"
        self.button_inicio_sum_vect.clicked.connect(self.iniciar_suma_vectores)
        self.button_paso2_sum_vect.clicked.connect(self.mostrar_suma_vectores)
        self.button_realizar_sum_vect.clicked.connect(self.realizar_suma_vectores)
        self.button_guardar_sum_vect.clicked.connect(self.guardar_suma_vectores)
        self.button_reiniciar_sum_vect.clicked.connect(self.reiniciar_suma_vectores)

        # Ejemplo de la sección de "Producto Punto"
        self.button_inicio_punto_vect.clicked.connect(self.iniciar_punto_vectores)
        self.button_realizar_punto_vect.clicked.connect(self.realizar_punto_vector)
        self.button_guardar_punto_vect.clicked.connect(self.guardar_punto_vect)
        self.button_reiniciar_punto_vect.clicked.connect(self.reiniciar_punto_vector)

        # Ejemplo de la sección de "Producto Cruz"
        self.button_inicio_cruz_vect.clicked.connect(self.iniciar_cruz_vectores)
        self.button_realizar_cruz_vect.clicked.connect(self.realizar_cruz_vector)
        self.button_guardar_cruz_vect.clicked.connect(self.guardar_cruz_vect)
        self.button_reiniciar_cruz_vect.clicked.connect(self.reiniciar_cruz_vector)

        # Sección de las prácticas
        self.button_p1_vect.clicked.connect(self.abrir_prac06)
        self.button_p2_vect.clicked.connect(self.abrir_prac07)
        self.button_p3_vect.clicked.connect(self.abrir_prac10)
        self.button_p4_vect.clicked.connect(self.abrir_prac01)
        self.button_p5_vect.clicked.connect(self.abrir_prac08)
        self.button_p6_vect.clicked.connect(self.abrir_prac21)

        #************* Módulo de Vectores (FIN) *******************************************************************************************************************#

        #************* Módulo de Leyes de Newton ******************************************************************************************************************#

        # Ocultando secciones
        self.ocultar_frame(self.frame_prim_ley)
        self.ocultar_frame(self.button_guardar_prim_ley)
        self.ocultar_frame(self.button_reiniciar_prim_ley)

        # Ejemplo de la sección de "1ra Ley: Inercia"
        self.button_inicio_prim_ley.clicked.connect(self.iniciar_primera_ley)
        self.button_realizar_prim_ley.clicked.connect(self.realizar_primera_ley)
        self.button_guardar_prim_ley.clicked.connect(self.guardar_primera_ley)
        self.button_reiniciar_prim_ley.clicked.connect(self.reiniciar_primera_ley)
        self.button_export_prim_ley.clicked.connect(self.exportar_tabla_primera_ley)

        # Ejemplo de la sección de "2da Ley: Dinámica"
        self.button_seg_ley.clicked.connect(self.mostrar_segunda_ley)

        # Ejemplo de la sección de "3ra Ley: Reacción"
        self.button_ter_ley.clicked.connect(self.mostrar_tercera_ley)

        # Sección de las prácticas
        self.button_p1_ley_newt.clicked.connect(self.abrir_prac05)
        self.button_p2_ley_newt.clicked.connect(self.abrir_prac09)
        self.button_p3_ley_newt.clicked.connect(self.abrir_prac12)
        self.button_p4_ley_newt.clicked.connect(self.abrir_prac23)
        self.button_p5_ley_newt.clicked.connect(self.abrir_prac24)

        #************* Módulo de Leyes de Newton (FIN) ************************************************************************************************************#

        #************* Módulo de Tiro Parabólico ******************************************************************************************************************#

        # Ocultado las secciones
        self.ocultar_frame(self.frame_tiro_par)
        self.ocultar_frame(self.button_guardar_tiro_par)
        self.ocultar_frame(self.button_reiniciar_tiro_par)

        # Ejemplo
        self.button_inicio_tiro_par.clicked.connect(self.iniciar_tiro_parabolico)
        self.button_realizar_tiro_par.clicked.connect(self.realizar_tiro_parabolico)
        self.button_guardar_tiro_par.clicked.connect(self.guardar_tiro_parabolico)
        self.button_reiniciar_tiro_par.clicked.connect(self.reiniciar_tiro_parabolico)
        self.button_export_tiro_par.clicked.connect(self.exportar_tabla_tiro_par)

        # Sección de las prácticas
        self.button_p1_tiro_par.clicked.connect(self.abrir_prac02)
        self.button_p2_tiro_par.clicked.connect(self.abrir_prac04)
        self.button_p3_tiro_par.clicked.connect(self.abrir_prac15)
        self.button_p4_tiro_par.clicked.connect(self.abrir_prac16)
        self.button_p5_tiro_par.clicked.connect(self.abrir_prac14)

        #************* Módulo de Tiro Parabólico (FIN) ************************************************************************************************************#

        #************* Módulo de Coordenadas Ortogonales **********************************************************************************************************#

        # Ocultado las secciones
        self.ocultar_frame(self.frame_coor_carte)
        self.ocultar_frame(self.button_guardar_coor_carte)
        self.ocultar_frame(self.button_reiniciar_coor_carte)
        self.ocultar_frame(self.frame_coor_esfe)
        self.ocultar_frame(self.button_guardar_coor_esfe)
        self.ocultar_frame(self.button_reiniciar_coor_esfe)
        self.ocultar_frame(self.frame_coor_cilin)
        self.ocultar_frame(self.button_guardar_coor_cilin)
        self.ocultar_frame(self.button_reiniciar_coor_cilin)

        # Ejemplo de Coordenadas Cartesianas
        self.button_inicio_coor_carte.clicked.connect(self.iniciar_coordenada_cartesiana)
        self.button_realizar_coor_carte.clicked.connect(self.realizar_coordenada_cartesiana)
        self.button_guardar_coor_carte.clicked.connect(self.guardar_coordenada_cartesiana)
        self.button_reiniciar_coor_carte.clicked.connect(self.reiniciar_coordenada_cartesiana)

        # Ejemplo de Coordenadas Esféricas
        self.button_inicio_coor_esfe.clicked.connect(self.iniciar_coordenada_esferica)
        self.button_realizar_coor_esfe.clicked.connect(self.realizar_coordenada_esferica)
        self.button_guardar_coor_esfe.clicked.connect(self.guardar_coordenada_esferica)
        self.button_reiniciar_coor_esfe.clicked.connect(self.reiniciar_coordenada_esferica)

        # Ejemplo de Coordenadas Cilíndricas
        self.button_inicio_coor_cilin.clicked.connect(self.iniciar_coordenada_cilindrica)
        self.button_realizar_coor_cilin.clicked.connect(self.realizar_coordenada_cilindrica)
        self.button_guardar_coor_cilin.clicked.connect(self.guardar_coordenada_cilindrica)
        self.button_reiniciar_coor_cilin.clicked.connect(self.reiniciar_coordenada_cilindrica)

        # Sección de las prácticas
        self.button_p1_coor_ortog.clicked.connect(self.abrir_prac03)
        self.button_p2_coor_ortog.clicked.connect(self.abrir_prac19)

        #************* Módulo de Coordenadas Ortogonales (FIN) ****************************************************************************************************#

        #************* Módulo de Ángulo Sólido ********************************************************************************************************************#

        # Ocultado las secciones
        self.ocultar_frame(self.frame_ang_solido)
        self.ocultar_frame(self.button_guardar_ang_solido)
        self.ocultar_frame(self.button_reiniciar_ang_solido)

        # Ejemplo de Ángulo Sólido
        self.button_inicio_ang_solido.clicked.connect(self.iniciar_angulo_solido)
        self.button_realizar_ang_solido.clicked.connect(self.realizar_angulo_solido)
        self.button_guardar_ang_solido.clicked.connect(self.guardar_angulo_solido)
        self.button_reiniciar_ang_solido.clicked.connect(self.reiniciar_angulo_solido)

        # Sección de las prácticas
        self.button_p1_ang_solido.clicked.connect(self.abrir_prac13)
        self.button_p2_ang_solido.clicked.connect(self.abrir_prac22)

        #************* Módulo de Ángulo Sólido (FIN) **************************************************************************************************************#

        #************* Módulo de Campo Eléctrico ******************************************************************************************************************#

        # Funciones botones de los diagramas
        self.button_d1_camp_electrico.clicked.connect(self.mostrar_campo_electrico)
        self.button_d2_camp_electrico.clicked.connect(self.mostrar_lineas_flujo)
        self.button_d3_camp_electrico.clicked.connect(self.mostrar_dipolo_electrico)
        self.button_d4_camp_electrico.clicked.connect(self.mostrar_potencial_electrostatico)

        # Sección de las prácticas
        self.button_p1_camp_electrico.clicked.connect(self.abrir_prac18)
        self.button_p2_camp_electrico.clicked.connect(self.abrir_prac11)
        self.button_p3_camp_electrico.clicked.connect(self.abrir_prac20)

        #************* Módulo de Campo Eléctrico (FIN) ************************************************************************************************************#

        #************* Módulo de Campo Magnético ******************************************************************************************************************#
        
        # Funciones botones de los diagramas
        self.button_d1_camp_magnetico.clicked.connect(self.mostrar_campo_magnetico_cable)
        self.button_d2_camp_magnetico.clicked.connect(self.mostrar_campo_magnetico_cables)
        self.button_d3_camp_magnetico.clicked.connect(self.mostrar_espira)
        self.button_d4_camp_magnetico.clicked.connect(self.mostrar_espiras)
        self.button_d5_camp_magnetico.clicked.connect(self.mostrar_dipolo_magnetico)

        # Sección de las prácticas
        self.button_p1_camp_magnetico.clicked.connect(self.abrir_prac17)

        #************* Módulo de Campo Magnético (FIN) ************************************************************************************************************#

    #----------------- NUEVAS FUNCIONES ----------------------------------------------------------------------------------------------------------------------------

    #///////////////   Funciones generales de la Interfaz   /////////////////////////////////////////////////////////////////////////////////#

    def mover_menu(self):       # Función para ocultar el menú lateral y los botones
        if True:
            width = self.frame_izquierda.width()
            normal = 0
            if width == 0:
                extender = 300
                self.pushButton_ocultar.show()
                self.pushButton_mostrar.hide()
            else:
                self.pushButton_ocultar.hide()
                self.pushButton_mostrar.show()
                extender = normal
            self.animacion = QPropertyAnimation(self.frame_izquierda, b"maximumWidth")
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setDuration(500)
            self.animacion.setEasingCurve(QEasingCurve.OutInBack)
            self.animacion.start()

    def sombra_frame(self, frame):      # Función para agregar sombra a los widgets
        sombra = QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(30)
        sombra.setXOffset(8)
        sombra.setYOffset(8)
        sombra.setColor(QColor(20, 200, 220, 255))
        frame.setGraphicsEffect(sombra)

    def habilitar_boton(self, frame):   # Función para habilitar un botón.
        frame.setEnabled(True)

    def deshabilitar_boton(self, frame):   # Función para deshabilitar un botón.
        frame.setEnabled(False)

    def ocultar_frame(self, frame):     # Función para ocultar un frame
        frame.hide()
    
    def mostrar_frame(self, frame):     # Función para mostrar un frame
        frame.show()

    def control_minimizar(self):    # Función para minimizar ventana
        self.showMinimized()

    def control_normal(self):   # Función para ajustar al tamaño normal de la ventana
        self.showNormal()
        self.pushButton_minimo.hide()
        self.pushButton_maximo.show()

    def control_maximizar(self):    # Función para expandir la ventana
        self.showMaximized()
        self.pushButton_maximo.hide()
        self.pushButton_minimo.show()

    def control_cerrar(self):   # Función para cerrar la ventana.
        quit()

    def guardar_grafica(self):      # Función para seleccionar la carpeta de destino de un documento
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setOption(QFileDialog.ShowDirsOnly)
        global direccion
        direccion = dialog.getExistingDirectory(self, 'Escoge la carpeta de destino:', os.path.curdir)   # Esta es la dirección

    def abrir_inicio(self):         # Función para abrir el módulo de Inicio.
        self.ajustar_index_combos()     # Regresamos los combos a su valor inicial.
        self.quitar_style_buttons()     # Desenmarcando los botones.
        self.button_inicio.setStyleSheet("border: 3px solid rgb(0, 252, 167);")
        self.stackedWidget_central.setCurrentWidget(self.inicio_central)
        self.stackedWidget_derecha.setCurrentWidget(self.inicio_derecha)
    
    def abrir_vectores(self):   # Función para abrir los módulos de Vectores
        opcion_vect = self.combo_vect.currentText()
        self.quitar_style_buttons()     # Desenmarcando los botones.
        self.combo_vect.setStyleSheet("border: 3px solid rgb(0, 252, 167);")
        self.ajustar_index_combo_vect()
        if opcion_vect == '               Vectores':
            self.stackedWidget_central.setCurrentWidget(self.vect_central)
            self.stackedWidget_derecha.setCurrentWidget(self.vect_derecha)
        elif opcion_vect == '                 Suma ':
            self.stackedWidget_central.setCurrentWidget(self.sum_vect_central)
            self.stackedWidget_derecha.setCurrentWidget(self.sum_vect_derecha)
        elif opcion_vect == '         Producto Interno ':
            self.stackedWidget_central.setCurrentWidget(self.prod_int_vect_central)
            self.stackedWidget_derecha.setCurrentWidget(self.prod_int_vect_derecha)
        elif opcion_vect == '            Producto Cruz':
            self.stackedWidget_central.setCurrentWidget(self.prod_cruz_vect_central)
            self.stackedWidget_derecha.setCurrentWidget(self.prod_cruz_vect_derecha)

    def abrir_leyes(self):   # Función para abrir los módulos de Leyes de Newton
        opcion_newt = self.combo_newt.currentText()
        self.quitar_style_buttons()     # Desenmarcando los botones.
        self.combo_newt.setStyleSheet("border: 3px solid rgb(0, 252, 167);")
        self.ajustar_index_combo_newt()
        if opcion_newt== '        Leyes de Newton':
            self.stackedWidget_central.setCurrentWidget(self.ley_newt_central)
            self.stackedWidget_derecha.setCurrentWidget(self.ley_newt_derecha)
        elif opcion_newt== '              1ra: Inercia':
            self.stackedWidget_central.setCurrentWidget(self.prim_ley_newt_central)
            self.stackedWidget_derecha.setCurrentWidget(self.prim_ley_newt_derecha)
        elif opcion_newt == '            2da: Dinámica':
            self.stackedWidget_central.setCurrentWidget(self.seg_ley_newt_central)
            self.stackedWidget_derecha.setCurrentWidget(self.seg_ley_newt_derecha)
        elif opcion_newt == '    3ra: Reacción y Acción':
            self.stackedWidget_central.setCurrentWidget(self.ter_ley_newt_central)
            self.stackedWidget_derecha.setCurrentWidget(self.ter_ley_newt_derecha)

    def abrir_tiro_par(self):   # Función para abir los módulos de Tiro parabólico
        self.ajustar_index_combos()
        self.quitar_style_buttons()     # Desenmarcando los botones.
        self.button_parab.setStyleSheet("border: 3px solid rgb(0, 252, 167);")
        self.stackedWidget_central.setCurrentWidget(self.tiro_par_central)
        self.stackedWidget_derecha.setCurrentWidget(self.tiro_par_derecha)

    def abrir_coordenadas(self):   # Función para abrir los módulos de Coordenadas Ortogonales
        opcion_coor = self.combo_coor.currentText()
        self.quitar_style_buttons()     # Desenmarcando los botones.
        self.combo_coor.setStyleSheet("border: 3px solid rgb(0, 252, 167);")
        self.ajustar_index_combo_coor()
        if opcion_coor== 'Coordenadas Ortogonales':
            self.stackedWidget_central.setCurrentWidget(self.coor_ortog_central)
            self.stackedWidget_derecha.setCurrentWidget(self.coor_ortog_derecha)
        elif opcion_coor== ' Coordenadas Cartesianas':
            self.stackedWidget_central.setCurrentWidget(self.coor_carte_central)
            self.stackedWidget_derecha.setCurrentWidget(self.coor_carte_derecha)
        elif opcion_coor == '   Coordenadas Esféricas':
            self.stackedWidget_central.setCurrentWidget(self.coor_esfe_central)
            self.stackedWidget_derecha.setCurrentWidget(self.coor_esfe_derecha)
        elif opcion_coor == '  Coordenadas Cilíndricas':
            self.stackedWidget_central.setCurrentWidget(self.coor_cilin_central)
            self.stackedWidget_derecha.setCurrentWidget(self.coor_cilin_derecha)

    def abrir_ang_sol(self):   # Función para abir los módulos de Ángulo Sólido
        self.ajustar_index_combos()
        self.quitar_style_buttons()     # Desenmarcando los botones.
        self.button_angu.setStyleSheet("border: 3px solid rgb(0, 252, 167);")
        self.stackedWidget_central.setCurrentWidget(self.ang_solido_central)
        self.stackedWidget_derecha.setCurrentWidget(self.ang_solido_derecha)

    def abrir_camp_elec(self):   # Función para abir los módulos de Campo Eléctrico
        self.ajustar_index_combos()
        self.quitar_style_buttons()     # Desenmarcando los botones.
        self.button_elec.setStyleSheet("border: 3px solid rgb(0, 252, 167);")
        self.stackedWidget_central.setCurrentWidget(self.camp_electrico_central)
        self.stackedWidget_derecha.setCurrentWidget(self.camp_electrico_derecha)


    def abrir_camp_magne(self):   # Función para abir los módulos de Campo Magnético
        self.ajustar_index_combos()
        self.quitar_style_buttons()     # Desenmarcando los botones.
        self.button_magne.setStyleSheet("border: 3px solid rgb(0, 252, 167);")
        self.stackedWidget_central.setCurrentWidget(self.camp_magnetico_central)
        self.stackedWidget_derecha.setCurrentWidget(self.camp_magnetico_derecha)

    def abrir_practicas(self):
        self.ajustar_index_combos()     # Regresamos los combos a su valor inicial.
        self.quitar_style_buttons()     # Desenmarcando los botones.
        self.button_practicas.setStyleSheet("border: 3px solid rgb(0, 252, 167);")
        self.stackedWidget_central.setCurrentWidget(self.practicas_central)
        self.stackedWidget_derecha.setCurrentWidget(self.inicio_derecha)

    def abrir_referencias(self):
        self.ajustar_index_combos()     # Regresamos los combos a su valor inicial.
        self.quitar_style_buttons()     # Desenmarcando los botones.
        self.button_referencias.setStyleSheet("border: 3px solid rgb(0, 252, 167);")
        self.stackedWidget_central.setCurrentWidget(self.referencias_central)
        self.stackedWidget_derecha.setCurrentWidget(self.inicio_derecha)

    def quitar_style_buttons(self):     # Función para desenmarcar los botones.
        self.button_inicio.setStyleSheet("")
        self.combo_vect.setStyleSheet("")
        self.combo_newt.setStyleSheet("")
        self.button_parab.setStyleSheet("")
        self.combo_coor.setStyleSheet("")
        self.button_angu.setStyleSheet("")
        self.button_elec.setStyleSheet("")
        self.button_magne.setStyleSheet("")
        self.button_practicas.setStyleSheet("")
        self.button_referencias.setStyleSheet("")

    def ajustar_index_combos(self):     # Ajustar el valor de los combo box
        self.combo_vect.setCurrentIndex(0)
        self.combo_newt.setCurrentIndex(0)
        self.combo_coor.setCurrentIndex(0)

    def ajustar_index_combo_vect(self):     # Ajustar el valor de los combo box en el combo_vect
        self.combo_newt.setCurrentIndex(0)
        self.combo_coor.setCurrentIndex(0)
    
    def ajustar_index_combo_newt(self):     # Ajustar el valor de los combo box en el combo_newt
        self.combo_vect.setCurrentIndex(0)
        self.combo_coor.setCurrentIndex(0)

    def ajustar_index_combo_coor(self):     # Ajustar el valor de los combo box en el combo_coor
        self.combo_vect.setCurrentIndex(0)
        self.combo_newt.setCurrentIndex(0)

    def borrar_grafica(self, objeto, frame):    # Función para borrar las simulaciones
        objeto.vaciar_grafica()    #Eliminamos los plt y axes existentes.   
        frame.removeWidget(objeto)    # Eliminamos el widget creado anterioremente
        objeto.deleteLater()
        objeto = None

    def borrar_simu(self, objeto, frame):   # Para las simulaciones de campo eléctrico y magnético
        objeto.vaciar_grafica()    #Eliminamos los plt y axes existentes.   
        frame.removeWidget(objeto)    # Eliminamos el widget creado anterioremente
        del objeto  # Eliminar el atributo objeto de la instancia self

    def exportar_tabla_excel(self, tabla, nombre):      # Función parab exportar las tablas a excel
        xlApp = win32.Dispatch('Excel.Application')
        xlApp.Visible = True

        # Crea el archivo en excel
        wb = xlApp.Workbooks.Add()

        # Crea la hoja en excel
        ws = wb.worksheets.add
        ws.name = nombre

        rows = []
        columnHeaders = []

        # Obtiene el nombre de las columnas
        for j in range(tabla.model().columnCount()):
            columnHeaders.append(tabla.horizontalHeaderItem(j).text())

        # Obtiene todo el contenido de la tabla
        for row in range(tabla.rowCount()):
            record = []
            for col in range(tabla.columnCount()):
                record.append(tabla.item(row, col).text())
            rows.append(record)

        # Lo inserta en un excel
        ws.Range(
            ws.cells(2, 1),
            ws.cells(len(rows)+1, len(columnHeaders))
        ).value = rows

        # Inserta las etiquetas de las columnas
        ws.Range(
            ws.cells(1, 1),
            ws.cells(1, len(columnHeaders))
        ).value = columnHeaders

    #////////////   Funciones generales de la Interfaz (FIN)   //////////////////////////////////////////////////////////////////////////////#

    #////////////////////////   Inicio   /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

    def insertar_usuario(self):
        global usuario
        usuario = self.lineEdit_usuario.text()      # Tomamos el valor de usuario para toda la aplicación.
        if usuario == '':
            self.label_titulo.setText("SSIG-3D.")
            self.deshabilitar_boton(self.combo_vect)
            self.deshabilitar_boton(self.combo_newt)
            self.deshabilitar_boton(self.button_parab)
            self.deshabilitar_boton(self.button_angu)
            self.deshabilitar_boton(self.combo_coor)
            self.deshabilitar_boton(self.button_elec)
            self.deshabilitar_boton(self.button_magne)
            Errores.Error_Usuario(self)
        else:
            self.lineEdit_usuario.setText("")       
            self.label_titulo.setText("SSIG-3D. Usuario: " + usuario)
            self.lineEdit_usuario.hide()
            self.button_usuario.hide()
            self.button_cerrar_sesion.show()
            self.habilitar_boton(self.combo_vect)
            self.habilitar_boton(self.combo_newt)
            self.habilitar_boton(self.button_parab)
            self.habilitar_boton(self.button_angu)
            self.habilitar_boton(self.combo_coor)
            self.habilitar_boton(self.button_elec)
            self.habilitar_boton(self.button_magne)     

    def cerrar_sesion(self):
            self.label_titulo.setText("SSIG-3D.")
            self.lineEdit_usuario.show()
            self.button_usuario.show()
            self.button_cerrar_sesion.hide()
            self.deshabilitar_boton(self.combo_vect)
            self.deshabilitar_boton(self.combo_newt)
            self.deshabilitar_boton(self.button_parab)
            self.deshabilitar_boton(self.button_angu)
            self.deshabilitar_boton(self.combo_coor)
            self.deshabilitar_boton(self.button_elec)
            self.deshabilitar_boton(self.button_magne)
            Errores.Informacion_Cerrar_Sesion(self)

    #////////////////////////   Inicio (FIN)   /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

    #////////////////////////   Vectores "VECTOR"   ////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

    def iniciar_vector(self):    # Función del botón "Comenzar".
        self.ocultar_frame(self.button_inicio_vect)
        self.mostrar_frame(self.frame_vect_ejemplo)
        self.lcdNu_magnitud_vect.display(0)
        self.lcdNu_r_alpha_vect.display(0)
        self.lcdNu_r_beta_vect.display(0)
        self.lcdNu_r_gamma_vect.display(0)
        self.lcdNu_g_alpha_vect.display(0)
        self.lcdNu_g_beta_vect.display(0)
        self.lcdNu_g_gamma_vect.display(0)

    def realizar_vector(self):
        #Asignación de los valores insertados
        rx = float(self.sBox_vect_X.text())        
        ry = float(self.sBox_vect_Y.text())
        rz = float(self.sBox_vect_Z.text())

        magnitud = np.sqrt(pow(rx, 2) + pow(ry, 2) + pow(rz, 2))

        if(magnitud == 0):
            Errores.Error_Vector_magnitud(self)
        else:
            Errores.Advertencia_ResultadosVector(self)
            self.mostrar_frame(self.button_guardar_vect)
            self.mostrar_frame(self.button_reiniciar_vect)
            self.ocultar_frame(self.button_realizar_vect)

            self.graficaVect = Vectores()
            self.graf_vect.addWidget(self.graficaVect)
            self.graficaVect.graficar_vector(rx, ry, rz, val_magnitud, val_alpha, val_beta, val_gamma, val_alpha_g, val_beta_g, val_gamma_g, usuario)

    def guardar_vector(self):       # Función del botón "Guardar Gráfica (JPG)"
        Errores.Advertencia_PosicionSimulacion(self)
        Errores.Advertencia_Direccion(self)
        self.guardar_grafica()
        if (direccion == ""):
            Errores.Error_Direccion(self)
        else:
            self.graficaVect.guardar_graf(direccion)

    def reiniciar_vector(self):      # Función del botón "Reiniciar".
        # Reseteando valores
        self.sBox_vect_X.setValue(0.0)
        self.sBox_vect_Y.setValue(0.0)
        self.sBox_vect_Z.setValue(0.0)
        self.ocultar_frame(self.button_guardar_vect)
        self.ocultar_frame(self.button_reiniciar_vect)
        self.mostrar_frame(self.button_realizar_vect)
        self.borrar_grafica(self.graficaVect, self.graf_vect)
        self.lcdNu_magnitud_vect.display(0)
        self.lcdNu_r_alpha_vect.display(0)
        self.lcdNu_r_beta_vect.display(0)
        self.lcdNu_r_gamma_vect.display(0)
        self.lcdNu_g_alpha_vect.display(0)
        self.lcdNu_g_beta_vect.display(0)
        self.lcdNu_g_gamma_vect.display(0)

    #////////////////////////   Vectores "VECTOR" (FIN)   //////////////////////////////////////////////////////////////////////////////////////////////////////////#

    #////////////////////////   Vectores "SUMA"   //////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
    
    def iniciar_suma_vectores(self):    # Función del botón "Comenzar".
        #self.deshabilitar_boton(self.button_inicio_sum_vect)
        self.ocultar_frame(self.button_inicio_sum_vect)
        self.mostrar_frame(self.frame_sum_vect_ejemplo)
        #self.borrar_grafica(self.graficaVectSum, self.graf_sum_vect)

    def mostrar_suma_vectores(self):    # Función del botón "Siguiente".
            self.habilitar_boton(self.button_realizar_sum_vect)
            self.ocultar_frame(self.button_paso2_sum_vect)
            self.deshabilitar_boton(self.cBox_2_vect)   
            self.deshabilitar_boton(self.cBox_3_vect)
            self.mostrar_frame(self.frame_sum_vect)
            self.mostrar_frame(self.button_realizar_sum_vect)
            if self.cBox_2_vect.checkState() == 2:      # Deshabilitamos los valores del vector 3 en caso de trabajar con 2.
                self.deshabilitar_boton(self.sBox_sum_vect_X3)
                self.deshabilitar_boton(self.sBox_sum_vect_Y3)
                self.deshabilitar_boton(self.sBox_sum_vect_Z3)
            
    def realizar_suma_vectores(self):   # Función del botón "Suma de Vectores".
        self.mostrar_frame(self.button_guardar_sum_vect)
        self.mostrar_frame(self.button_reiniciar_sum_vect)
        self.ocultar_frame(self.button_realizar_sum_vect)

        # Asignamos los valores insertados.
        x1 = float(self.sBox_sum_vect_X1.text())        
        y1 = float(self.sBox_sum_vect_Y1.text())
        z1 = float(self.sBox_sum_vect_Z1.text())
        x2 = float(self.sBox_sum_vect_X2.text())
        y2 = float(self.sBox_sum_vect_Y2.text())
        z2 = float(self.sBox_sum_vect_Z2.text())
        x3 = float(self.sBox_sum_vect_X3.text())
        y3 = float(self.sBox_sum_vect_Y3.text())
        z3 = float(self.sBox_sum_vect_Z3.text())

        self.graficaVectSum = Vectores_Suma_Vect()
        self.graf_sum_vect.addWidget(self.graficaVectSum)

        if self.cBox_2_vect.checkState() == 2:      # En el caso de trabajar con 2.
            self.graficaVectSum.graficar_vectores_suma_2v(x1, y1, z1, x2, y2, z2, usuario)
        else:
            self.graficaVectSum.graficar_vectores_suma_3v(x1, y1, z1, x2, y2, z2, x3, y3, z3, usuario)

    def guardar_suma_vectores(self):        # Función del botón "Guardar Gráfica (JPG)"
        Errores.Advertencia_PosicionSimulacion(self)
        Errores.Advertencia_Direccion(self)
        self.guardar_grafica()
        if (direccion == ""):
            Errores.Error_Direccion(self)
        else:
            self.graficaVectSum.guardar_graf(direccion)

    def reiniciar_suma_vectores(self):      # Función del botón "Reiniciar".
        # Reseteando valores
        self.sBox_sum_vect_X1.setValue(0.0)
        self.sBox_sum_vect_Y1.setValue(0.0)
        self.sBox_sum_vect_Z1.setValue(0.0)
        self.sBox_sum_vect_X2.setValue(0.0)
        self.sBox_sum_vect_Y2.setValue(0.0)
        self.sBox_sum_vect_Z2.setValue(0.0)
        self.sBox_sum_vect_X3.setValue(0.0)
        self.sBox_sum_vect_Y3.setValue(0.0)
        self.sBox_sum_vect_Z3.setValue(0.0)
        self.ocultar_frame(self.frame_sum_vect)
        self.ocultar_frame(self.button_guardar_sum_vect)
        self.ocultar_frame(self.button_reiniciar_sum_vect)
        self.habilitar_boton(self.cBox_2_vect)
        self.habilitar_boton(self.cBox_3_vect)
        self.mostrar_frame(self.button_paso2_sum_vect)
        if self.cBox_2_vect.checkState() == 2:      # Se habilitan botones para evitar errores
            self.habilitar_boton(self.sBox_sum_vect_X3)
            self.habilitar_boton(self.sBox_sum_vect_Y3)
            self.habilitar_boton(self.sBox_sum_vect_Z3)
        self.borrar_grafica(self.graficaVectSum, self.graf_sum_vect)
            
    #////////////////////////   Vectores "SUMA" (FIN)   ////////////////////////////////////////////////////////////////////////////////////////////////////////////#

    #////////////////////////   Vectores "PRODUCTO PUNTO"   ////////////////////////////////////////////////////////////////////////////////////////////////////////#

    def iniciar_punto_vectores(self):   # Función del botón "Comenzar".
        self.ocultar_frame(self.button_inicio_punto_vect)
        self.mostrar_frame(self.frame_punto_vect)

    def realizar_punto_vector(self):    # Función del botón "Producto Punto de Vectores".
        self.mostrar_frame(self.button_guardar_punto_vect)
        self.mostrar_frame(self.button_reiniciar_punto_vect)
        self.ocultar_frame(self.button_realizar_punto_vect)

        # Asignamos los valores insertados.
        x1 = float(self.sBox_punto_vect_X1.text())        
        y1 = float(self.sBox_punto_vect_Y1.text())
        z1 = float(self.sBox_punto_vect_Z1.text())
        x2 = float(self.sBox_punto_vect_X2.text())        
        y2 = float(self.sBox_punto_vect_Y2.text())
        z2 = float(self.sBox_punto_vect_Z2.text())

        self.graficaVectPunto = Vectores_Punto_Vect()
        self.graf_punto_vect.addWidget(self.graficaVectPunto)
        self.graficaVectPunto.graficar_vector_punto(x1, y1, z1, x2, y2, z2, usuario)

    def guardar_punto_vect(self):       # Función del botón "Guardar Gráfica (JPG)"
        Errores.Advertencia_PosicionSimulacion(self)
        Errores.Advertencia_Direccion(self)
        self.guardar_grafica()
        if (direccion == ""):
            Errores.Error_Direccion(self)
        else:
            self.graficaVectPunto.guardar_graf(direccion)

    def reiniciar_punto_vector(self):        # Función del botón "Reiniciar".
        # Reiniciando los valores
        self.sBox_punto_vect_X1.setValue(0.0)
        self.sBox_punto_vect_Y1.setValue(0.0)
        self.sBox_punto_vect_Z1.setValue(0.0)
        self.sBox_punto_vect_X2.setValue(0.0)
        self.sBox_punto_vect_Y2.setValue(0.0)
        self.sBox_punto_vect_Z2.setValue(0.0)
        self.mostrar_frame(self.button_realizar_punto_vect)
        self.ocultar_frame(self.button_reiniciar_punto_vect)
        self.ocultar_frame(self.button_guardar_punto_vect)
        self.borrar_grafica(self.graficaVectPunto, self.graf_punto_vect)
            
    #////////////////////////   Vectores "PRODUCTO PUNTO" (FIN)   ///////////////////////////////////////////////////////////////////////////////////////////////////#

    #////////////////////////   Vectores "PRODUCTO CRUZ"   //////////////////////////////////////////////////////////////////////////////////////////////////////////#

    def iniciar_cruz_vectores(self):    # Función del botón "Comenzar".
        #self.deshabilitar_boton(self.button_inicio_cruz_vect)
        self.ocultar_frame(self.button_inicio_cruz_vect)
        self.mostrar_frame(self.frame_cruz_vect)
        #self.borrar_grafica(self.graficaVectCruz, self.graf_cruz_vect)

    def realizar_cruz_vector(self):     # Función del botón "Producto Cruz de Vectores".
        self.mostrar_frame(self.button_guardar_cruz_vect)
        self.mostrar_frame(self.button_reiniciar_cruz_vect)
        #self.deshabilitar_boton(self.button_realizar_cruz_vect)
        self.ocultar_frame(self.button_realizar_cruz_vect)

        # Asignamos los valores insertados.
        x1 = float(self.sBox_cruz_vect_X1.text())        
        y1 = float(self.sBox_cruz_vect_Y1.text())
        z1 = float(self.sBox_cruz_vect_Z1.text())
        x2 = float(self.sBox_cruz_vect_X2.text())        
        y2 = float(self.sBox_cruz_vect_Y2.text())
        z2 = float(self.sBox_cruz_vect_Z2.text())

        self.graficaVectCruz = Vectores_Cruz_Vect()
        self.graf_cruz_vect.addWidget(self.graficaVectCruz)
        self.graficaVectCruz.graficar_vector_cruz(x1, y1, z1, x2, y2, z2, usuario)

    def guardar_cruz_vect(self):    # Función del botón "Guardar Gráfica (JPG)"
        Errores.Advertencia_PosicionSimulacion(self)
        Errores.Advertencia_Direccion(self)
        self.guardar_grafica()
        if (direccion == ""):
            Errores.Error_Direccion(self)
        else:
            self.graficaVectCruz.guardar_graf(direccion)

    def reiniciar_cruz_vector(self):    # Función del botón "Reiniciar".
        # Reiniciando los valores
        self.sBox_cruz_vect_X1.setValue(0.0)
        self.sBox_cruz_vect_Y1.setValue(0.0)
        self.sBox_cruz_vect_Z1.setValue(0.0)
        self.sBox_cruz_vect_X2.setValue(0.0)
        self.sBox_cruz_vect_Y2.setValue(0.0)
        self.sBox_cruz_vect_Z2.setValue(0.0)
        #self.habilitar_boton(self.button_realizar_cruz_vect)
        self.mostrar_frame(self.button_realizar_cruz_vect)
        self.ocultar_frame(self.button_guardar_cruz_vect)
        self.ocultar_frame(self.button_reiniciar_cruz_vect)
        self.borrar_grafica(self.graficaVectCruz, self.graf_cruz_vect)

    #////////////////////////   Vectores "PRODUCTO CRUZ" (FIN)   ////////////////////////////////////////////////////////////////////////////////////////////////////#

    #////////////////////////   Vectores "Prácticas"   //////////////////////////////////////////////////////////////////////////////////////////////////////////////#

    def abrir_prac06(self):      # El número implica el orden en que fueron realizadas
        ventana = Prac06(self)
        ventana.show()
    
    def abrir_prac07(self):
        ventana = Prac07(self)
        ventana.show()

    def abrir_prac10(self):
        ventana = Prac10(self)
        ventana.show()

    def abrir_prac08(self):
        ventana = Prac08(self)
        ventana.show()
    
    def abrir_prac01(self):
        ventana = Prac01(self)
        ventana.show()

    def abrir_prac21(self):
        ventana = Prac21(self)
        ventana.show()

    #////////////////////////   Vectores "Prácticas" (FIN)   ////////////////////////////////////////////////////////////////////////////////////////////////////////#

    #////////////////////////   Leyes de Newton "1RA: INERCIA"   ////////////////////////////////////////////////////////////////////////////////////////////////////#

    def iniciar_primera_ley(self):    # Función del botón "Comenzar".
        self.ocultar_frame(self.button_inicio_prim_ley)
        self.mostrar_frame(self.frame_prim_ley)
        self.ocultar_frame(self.button_export_prim_ley)

    def realizar_primera_ley(self):      # Función del botón "1ra Ley: Inercia".
        Errores.Advertencia_TablaResultados(self)

        self.mostrar_frame(self.button_guardar_prim_ley)
        self.mostrar_frame(self.button_reiniciar_prim_ley)
        self.mostrar_frame(self.button_export_prim_ley)
        self.ocultar_frame(self.button_realizar_prim_ley)

        V0x = float(self.sBox_prim_ley_Vox.text())
        V0y = float(self.sBox_prim_ley_Voy.text())
        V0z = float(self.sBox_prim_ley_Voz.text())
        tiempo = float(self.sBox_prim_ley_t.text())

        self.graficaPrimLey = Primera_Ley()
        self.graf_prim_ley.addWidget(self.graficaPrimLey)
        self.graficaPrimLey.graficar_primera_ley(V0x, V0y, V0z, tiempo, usuario, self.tabla_prim_ley)

    def guardar_primera_ley(self):      # Función del botón "Guardar Gráfica (GIF y JPG)"
        Errores.Advertencia_PosicionSimulacion(self)
        Errores.Advertencia_Direccion(self)
        self.guardar_grafica()
        if (direccion == ""):
            Errores.Error_Direccion(self)
        else:
            self.graficaPrimLey.guardar_graf(direccion)

    def reiniciar_primera_ley(self):        # Función del botón "Reiniciar".
        # Reiniciando los valores
        self.sBox_prim_ley_Vox.setValue(0.0)
        self.sBox_prim_ley_Voy.setValue(0.0)
        self.sBox_prim_ley_Voz.setValue(0.0)
        self.sBox_prim_ley_t.setValue(0)
        self.tabla_prim_ley.setRowCount(0)   # Eliminamos las filas de la tabla
        self.mostrar_frame(self.button_realizar_prim_ley)
        self.ocultar_frame(self.button_guardar_prim_ley)
        self.ocultar_frame(self.button_reiniciar_prim_ley)
        self.borrar_grafica(self.graficaPrimLey, self.graf_prim_ley)
    
    def exportar_tabla_primera_ley(self):        # Función del botón "Exportar tabla (Excel)".
        self.exportar_tabla_excel(self.tabla_prim_ley, 'Ley Inercia')

    def mostrar_segunda_ley(self):  # Mostrando 2da ley Dinámica
        self.graficaSegLey = Segunda_Ley()
        self.graf_seg_ley.addWidget(self.graficaSegLey)
        self.graficaSegLey.graficar_seg_ley_muestra()

        self.ocultar_frame(self.button_seg_ley)

    def mostrar_tercera_ley(self):   #Mostrando 3ra ley Acción/Reacción de muestra
        self.graficaTerLey = Tercera_Ley()
        self.graf_ter_ley.addWidget(self.graficaTerLey)
        self.graficaTerLey.graficar_tercera_ley()

        self.ocultar_frame(self.button_ter_ley)

    #////////////////////////   Leyes de Newton "Prácticas"   ////////////////////////////////////////////////////////////////////////////////////////////////////////#

    def abrir_prac05(self):
        ventana = Prac05(self)
        ventana.show()

    def abrir_prac09(self):
        ventana = Prac09(self)
        ventana.show()

    def abrir_prac12(self):
        ventana = Prac12(self)
        ventana.show()

    def abrir_prac23(self):
        ventana = Prac23(self)
        ventana.show()

    def abrir_prac24(self):
        ventana = Prac24(self)
        ventana.show()

    #////////////////////////   Leyes de Newton "Prácticas" (FIN)   //////////////////////////////////////////////////////////////////////////////////////////////////#

    #////////////////////////   Tiro Parabólico   ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

    def iniciar_tiro_parabolico(self):       # Función del botón "Comenzar".
        self.deshabilitar_boton(self.button_inicio_tiro_par)
        self.mostrar_frame(self.frame_tiro_par)
        self.ocultar_frame(self.button_export_tiro_par)
        self.tabla_tiro_par.setRowCount(0)   # Eliminamos las filas de la tabla

    def realizar_tiro_parabolico(self):     # Función del botón "Tiro Parabólico".
        Errores.Advertencia_TablaResultados(self)

        self.mostrar_frame(self.button_guardar_tiro_par)
        self.mostrar_frame(self.button_reiniciar_tiro_par)
        self.mostrar_frame(self.button_export_tiro_par)
        self.ocultar_frame(self.button_realizar_tiro_par)

        x0 = float(self.sBox_tiro_par_Xo.text())
        y0 = float(self.sBox_tiro_par_Yo.text())
        z0 = float(self.sBox_tiro_par_Zo.text())
        V0x = float(self.sBox_tiro_par_Vox.text())
        V0y = float(self.sBox_tiro_par_Voy.text())
        V0z = float(self.sBox_tiro_par_Voz.text())
        tiempo = float(self.sBox_tiro_par_t.text())

        self.graficaTiroPar = Tiro_Parabolico()
        self.graf_tiro_par.addWidget(self.graficaTiroPar)
        self.graficaTiroPar.graficar_tiro_parabolico(x0, y0, z0, V0x, V0y, V0z, tiempo, usuario, self.tabla_tiro_par)

    def guardar_tiro_parabolico(self):          # Función del botón "Guardar Gráfica (GIF y JPG)"
        Errores.Advertencia_PosicionSimulacion(self)
        Errores.Advertencia_Direccion(self)
        self.guardar_grafica()
        if (direccion == ""):
            Errores.Error_Direccion(self)
        else:
            self.graficaTiroPar.guardar_graf(direccion)

    def reiniciar_tiro_parabolico(self):        # Función del botón "Reiniciar".
        # Reiniciando los valores
        self.sBox_tiro_par_Xo.setValue(0.0)
        self.sBox_tiro_par_Yo.setValue(0.0)
        self.sBox_tiro_par_Zo.setValue(0.0)
        self.sBox_tiro_par_Vox.setValue(0.0)
        self.sBox_tiro_par_Voy.setValue(0.0)
        self.sBox_tiro_par_Voz.setValue(0.0)
        self.sBox_tiro_par_t.setValue(0)
        self.tabla_tiro_par.setRowCount(0)   # Eliminamos las filas de la tabla
        self.mostrar_frame(self.button_realizar_tiro_par)
        self.ocultar_frame(self.button_guardar_tiro_par)
        self.ocultar_frame(self.button_reiniciar_tiro_par)
        self.borrar_grafica(self.graficaTiroPar, self.graf_tiro_par)

    def exportar_tabla_tiro_par(self):          # Función del botón "Exportar tabla (Excel)".
        self.exportar_tabla_excel(self.tabla_tiro_par, 'Tiro Parabólico')

    #////////////////////////   Tiro Parabólico (FIN)   /////////////////////////////////////////////////////////////////////////////////////////////////////////////#

    #////////////////////////   Tiro Parabólico "Prácticas"   ///////////////////////////////////////////////////////////////////////////////////////////////////////#

    def abrir_prac02(self):
        ventana = Prac02(self)
        ventana.show()

    def abrir_prac04(self):
        ventana = Prac04(self)
        ventana.show()

    def abrir_prac14(self):
        ventana = Prac14(self)
        ventana.show()

    def abrir_prac15(self):
        ventana = Prac15(self)
        ventana.show()

    def abrir_prac16(self):
        ventana = Prac16(self)
        ventana.show()

    #////////////////////////   Tiro Parabólico "Prácticas" (FIN)   /////////////////////////////////////////////////////////////////////////////////////////////////#

    #////////////////////////   Coordenadas Ortogonales "Coordenadas Cartesianas"   /////////////////////////////////////////////////////////////////////////////////#

    def iniciar_coordenada_cartesiana(self):            # Función del botón "Comenzar".
        self.ocultar_frame(self.button_inicio_coor_carte)
        self.mostrar_frame(self.frame_coor_carte)

    def realizar_coordenada_cartesiana(self):    # Función del botón "Coordenada Cartesiana".
        # Asignamos los valores insertados.
        rx = float(self.sBox_coor_carte_rx.text())        
        ry = float(self.sBox_coor_carte_ry.text())
        rz = float(self.sBox_coor_carte_rz.text())

        magnitud = np.sqrt(pow(rx, 2) + pow(ry, 2) + pow(rz, 2))

        if(magnitud == 0):
            Errores.Error_Vector_magnitud(self)
        if(rx == 0 or ry == 0 or rz == 0):
            Errores.Error_Coordenadas_valores(self)
        else:
            self.mostrar_frame(self.button_guardar_coor_carte)
            self.mostrar_frame(self.button_reiniciar_coor_carte)
            self.ocultar_frame(self.button_realizar_coor_carte)

            self.graficaCarte = Coordenadas_Cartesianas()
            self.graf_coor_carte.addWidget(self.graficaCarte)
            self.graficaCarte.graficar_coor_carte(rx, ry, rz, usuario)

    def guardar_coordenada_cartesiana(self):         # Función del botón "Guardar Gráfica (JPG)"
        Errores.Advertencia_PosicionSimulacion(self)
        Errores.Advertencia_Direccion(self)
        self.guardar_grafica()
        if (direccion == ""):
            Errores.Error_Direccion(self)
        else:
            self.graficaCarte.guardar_graf(direccion)

    def reiniciar_coordenada_cartesiana(self):      # Función del botón "Reiniciar".
        # Reiniciando los valores
        self.sBox_coor_carte_rx.setValue(0.0)
        self.sBox_coor_carte_ry.setValue(0.0)
        self.sBox_coor_carte_rz.setValue(0.0)
        self.mostrar_frame(self.button_realizar_coor_carte)
        self.ocultar_frame(self.button_guardar_coor_carte)
        self.ocultar_frame(self.button_reiniciar_coor_carte)
        self.borrar_grafica(self.graficaCarte, self.graf_coor_carte)

    #////////////////////////   Coordenadas Ortogonales "Coordenadas Cartesianas" (FIN)   ///////////////////////////////////////////////////////////////////////////#
                
    #////////////////////////   Coordenadas Ortogonales "Coordenadas Esféricas"   ///////////////////////////////////////////////////////////////////////////////////#

    def iniciar_coordenada_esferica(self):          # Función del botón "Comenzar".
        self.ocultar_frame(self.button_inicio_coor_esfe)
        self.mostrar_frame(self.frame_coor_esfe)

    def realizar_coordenada_esferica(self):    # Función del botón "Coordenada Esférica".
        # Asignamos los valores insertados.
        x = float(self.sBox_coor_esfe_X.text())        
        y = float(self.sBox_coor_esfe_Y.text())
        z = float(self.sBox_coor_esfe_Z.text())

        r = np.sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2))

        if(r == 0):
            Errores.Error_Vector_magnitud(self)
        if(x == 0 or y == 0 or z == 0):
            Errores.Error_Coordenadas_valores(self)
        else:
            self.mostrar_frame(self.button_guardar_coor_esfe)
            self.mostrar_frame(self.button_reiniciar_coor_esfe)
            self.ocultar_frame(self.button_realizar_coor_esfe)

            self.graficaEsfe = Coordenadas_Esfericas()
            self.graf_coor_esfe.addWidget(self.graficaEsfe)
            self.graficaEsfe.graficar_coor_esfe(x, y, z, usuario)

    def guardar_coordenada_esferica(self):          # Función del botón "Guardar Gráfica (JPG)"
        Errores.Advertencia_PosicionSimulacion(self)
        Errores.Advertencia_Direccion(self)
        self.guardar_grafica()
        if (direccion == ""):
            Errores.Error_Direccion(self)
        else:
            self.graficaEsfe.guardar_graf(direccion)

    def reiniciar_coordenada_esferica(self):        # Función del botón "Reiniciar".
        # Reiniciando los valores
        self.sBox_coor_esfe_X.setValue(0.0)
        self.sBox_coor_esfe_Y.setValue(0.0)
        self.sBox_coor_esfe_Z.setValue(0.0)
        self.mostrar_frame(self.button_realizar_coor_esfe)
        self.ocultar_frame(self.button_guardar_coor_esfe)
        self.ocultar_frame(self.button_reiniciar_coor_esfe)
        self.borrar_grafica(self.graficaEsfe, self.graf_coor_esfe)

    #////////////////////////   Coordenadas Ortogonales "Coordenadas Esféricas" (FIN)   /////////////////////////////////////////////////////////////////////////////#

    #////////////////////////   Coordenadas Ortogonales "Coordenadas Cilíndricas"   /////////////////////////////////////////////////////////////////////////////////#

    def iniciar_coordenada_cilindrica(self):          # Función del botón "Comenzar".
        self.ocultar_frame(self.button_inicio_coor_cilin)
        self.mostrar_frame(self.frame_coor_cilin)

    def realizar_coordenada_cilindrica(self):    # Función del botón "Coordenada Cilíndrica".
        # Asignamos los valores insertados.
        x = float(self.sBox_coor_cilin_X.text())        
        y = float(self.sBox_coor_cilin_Y.text())
        z = float(self.sBox_coor_cilin_Z.text())

        r = np.sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2))

        if(r == 0):
            Errores.Error_Vector_magnitud(self)
        if(x == 0 or y == 0 or z == 0):
            Errores.Error_Coordenadas_valores(self)
        else:
            self.mostrar_frame(self.button_guardar_coor_cilin)
            self.mostrar_frame(self.button_reiniciar_coor_cilin)
            self.ocultar_frame(self.button_realizar_coor_cilin)

            self.graficaCilin = Coordenadas_Cilindricas()
            self.graf_coor_cilin.addWidget(self.graficaCilin)
            self.graficaCilin.graficar_coor_cilin(x, y, z, usuario)

    def guardar_coordenada_cilindrica(self):          # Función del botón "Guardar Gráfica (JPG)"
        Errores.Advertencia_PosicionSimulacion(self)
        Errores.Advertencia_Direccion(self)
        self.guardar_grafica()
        if (direccion == ""):
            Errores.Error_Direccion(self)
        else:
            self.graficaCilin.guardar_graf(direccion)

    def reiniciar_coordenada_cilindrica(self):        # Función del botón "Reiniciar".
        # Reiniciando los valores
        self.sBox_coor_cilin_X.setValue(0.0)
        self.sBox_coor_cilin_Y.setValue(0.0)
        self.sBox_coor_cilin_Z.setValue(0.0)
        self.mostrar_frame(self.button_realizar_coor_cilin)
        self.ocultar_frame(self.button_guardar_coor_cilin)
        self.ocultar_frame(self.button_reiniciar_coor_cilin)
        self.borrar_grafica(self.graficaCilin, self.graf_coor_cilin)

    #////////////////////////   Coordenadas Ortogonales "Coordenadas Cilíndricas" (FIN)   ///////////////////////////////////////////////////////////////////////////#

    #////////////////////////   Coordenadas Ortogonales "Prácticas"   ///////////////////////////////////////////////////////////////////////////////////////////////#

    def abrir_prac03(self):
        ventana = Prac03(self)
        ventana.show()

    def abrir_prac19(self):
        ventana = Prac19(self)
        ventana.show()

    #////////////////////////   Coordenadas Ortogonales "Prácticas" (FIN)   /////////////////////////////////////////////////////////////////////////////////////////#

    #////////////////////////   Ángulo Sólido   /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

    def iniciar_angulo_solido(self):          # Función del botón "Comenzar".
        self.ocultar_frame(self.button_inicio_ang_solido)
        self.mostrar_frame(self.frame_ang_solido)

    def realizar_angulo_solido(self):    # Función del botón "Coordenada Esférica".
        # Asignamos los valores insertados.
        theta = float(self.sBox_ang_solido_theta.text())        

        self.mostrar_frame(self.button_guardar_ang_solido)
        self.mostrar_frame(self.button_reiniciar_ang_solido)
        self.ocultar_frame(self.button_realizar_ang_solido)

        self.graficaAngSol = Angulo_Solido()
        self.graf_ang_solido.addWidget(self.graficaAngSol)
        self.graficaAngSol.graficar_ang_solido(np.deg2rad(theta), usuario)

    def guardar_angulo_solido(self):          # Función del botón "Guardar Gráfica (JPG)"
        Errores.Advertencia_PosicionSimulacion(self)
        Errores.Advertencia_Direccion(self)
        self.guardar_grafica()
        if (direccion == ""):
            Errores.Error_Direccion(self)
        else:
            self.graficaAngSol.guardar_graf(direccion)

    def reiniciar_angulo_solido(self):        # Función del botón "Reiniciar".
        # Reiniciando los valores
        self.sBox_ang_solido_theta.setValue(0.0)
        self.mostrar_frame(self.button_realizar_ang_solido)
        self.ocultar_frame(self.button_guardar_ang_solido)
        self.ocultar_frame(self.button_reiniciar_ang_solido)
        self.borrar_grafica(self.graficaAngSol, self.graf_ang_solido)

    #////////////////////////   Ángulo Sólido (FIN)   ///////////////////////////////////////////////////////////////////////////////////////////////////////////////#

    #////////////////////////   Ángulo Sólido "Prácticas" ///////////////////////////////////////////////////////////////////////////////////////////////////////////#

    def abrir_prac13(self):
        ventana = Prac13(self)
        ventana.show()

    def abrir_prac22(self):
        ventana = Prac22(self)
        ventana.show()

    #////////////////////////   Ángulo Sólido "Prácticas" (FIN)   ///////////////////////////////////////////////////////////////////////////////////////////////////#

    #////////////////////////   Campo Eléctrico   ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

    def mostrar_campo_electrico(self):
        self.limpiar_simu_elec()
        self.ocultar_frame(self.button_d1_camp_electrico)
        self.mostrar_frame(self.button_d2_camp_electrico)
        self.mostrar_frame(self.button_d3_camp_electrico)
        self.mostrar_frame(self.button_d4_camp_electrico)

        if not hasattr(self, 'graficaCampElec'):
            # Mostrando un campo eléctrico 
            self.graficaCampElec = Campo_Electrico()    
            self.graf_camp_electrico.addWidget(self.graficaCampElec)
            self.graficaCampElec.graficar_camp_elect()

        self.stackedWidget_camp_elec_derecha.setCurrentWidget(self.Ley_de_coulumb)

    def mostrar_lineas_flujo(self):
        self.limpiar_simu_elec()
        self.ocultar_frame(self.button_d2_camp_electrico)
        self.mostrar_frame(self.button_d1_camp_electrico)
        self.mostrar_frame(self.button_d3_camp_electrico)
        self.mostrar_frame(self.button_d4_camp_electrico)

        if not hasattr(self, 'graficaLineaFlujo'):
            self.graficaLineaFlujo = Camp_Elec_Flujos()
            self.graf_camp_electrico2.addWidget(self.graficaLineaFlujo)
            self.graficaLineaFlujo.graficar_lineas_flujos()

        self.stackedWidget_camp_elec_derecha.setCurrentWidget(self.Lineas_de_flujo_elec)

    def mostrar_dipolo_electrico(self):
        self.limpiar_simu_elec()
        self.ocultar_frame(self.button_d3_camp_electrico)
        self.mostrar_frame(self.button_d1_camp_electrico)
        self.mostrar_frame(self.button_d2_camp_electrico)
        self.mostrar_frame(self.button_d4_camp_electrico)

        if not hasattr(self, 'graficaDipolo'):
            self.graficaDipolo = Camp_Elec_Dipolo()
            self.graf_camp_electrico3.addWidget(self.graficaDipolo)
            self.graficaDipolo.graficar_dipolo()
        
        self.stackedWidget_camp_elec_derecha.setCurrentWidget(self.Dipolo_elec)

    def mostrar_potencial_electrostatico(self):
        self.limpiar_simu_elec()
        self.ocultar_frame(self.button_d4_camp_electrico)
        self.mostrar_frame(self.button_d1_camp_electrico)
        self.mostrar_frame(self.button_d2_camp_electrico)
        self.mostrar_frame(self.button_d3_camp_electrico)

        if not hasattr(self, 'graficaPotencial'):
            self.graficaPotencial = Camp_Elec_Potencial()
            self.graf_camp_electrico4.addWidget(self.graficaPotencial)
            self.graficaPotencial.graficar_potencial()
        
        self.stackedWidget_camp_elec_derecha.setCurrentWidget(self.Potencial_elec)

    def limpiar_simu_elec(self):
        if hasattr(self, 'graficaCampElec'):
            self.borrar_simu(self.graficaCampElec, self.graf_camp_electrico)
        if hasattr(self, 'graficaLineaFlujo'):
            self.borrar_simu(self.graficaLineaFlujo, self.graf_camp_electrico2)
        if hasattr(self, 'graficaDipolo'):
            self.borrar_simu(self.graficaDipolo, self.graf_camp_electrico3)
        if hasattr(self, 'graficaPotencial'):
            self.borrar_simu(self.graficaPotencial, self.graf_camp_electrico4)

    #////////////////////////   Campo Eléctrico (FIN)   /////////////////////////////////////////////////////////////////////////////////////////////////////////////#

    #////////////////////////   Campo Eléctrico "Prácticas"   ///////////////////////////////////////////////////////////////////////////////////////////////////////#

    def abrir_prac11(self):
        ventana = Prac11(self)
        ventana.show()

    def abrir_prac18(self):
        ventana = Prac18(self)
        ventana.show()

    def abrir_prac20(self):
        ventana = Prac20(self)
        ventana.show()

    #////////////////////////   Campo Eléctrico "Prácticas" (FIN)   /////////////////////////////////////////////////////////////////////////////////////////////////#

    #////////////////////////   Campo Magnético   ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

    def mostrar_campo_magnetico_cable(self):
        self.limpiar_simu_magne()
        self.ocultar_frame(self.button_d1_camp_magnetico)
        self.mostrar_frame(self.button_d2_camp_magnetico)
        self.mostrar_frame(self.button_d3_camp_magnetico)
        self.mostrar_frame(self.button_d4_camp_magnetico)
        self.mostrar_frame(self.button_d5_camp_magnetico)

        if not hasattr(self, 'graficaCampMagne'):
            self.graficaCampMagne = Campo_Magnetico()    
            self.graf_camp_magnetico.addWidget(self.graficaCampMagne)
            self.graficaCampMagne.graficar_camp_magne()

        self.stackedWidget_camp_magne_derecha.setCurrentWidget(self.Camp_magnetico_cable)

    def mostrar_campo_magnetico_cables(self):
        self.limpiar_simu_magne()
        self.ocultar_frame(self.button_d2_camp_magnetico)
        self.mostrar_frame(self.button_d1_camp_magnetico)
        self.mostrar_frame(self.button_d3_camp_magnetico)
        self.mostrar_frame(self.button_d4_camp_magnetico)

        if not hasattr(self, 'graficaCampCables'):
            self.graficaCampCables = Camp_Magne_Cables_Par()  
            self.graf_camp_magnetico2.addWidget(self.graficaCampCables)
            self.graficaCampCables.graficar_cables()

        self.stackedWidget_camp_magne_derecha.setCurrentWidget(self.Camp_magnetico_cables)

    def mostrar_espira(self):
        self.limpiar_simu_magne()
        self.ocultar_frame(self.button_d3_camp_magnetico)
        self.mostrar_frame(self.button_d1_camp_magnetico)
        self.mostrar_frame(self.button_d2_camp_magnetico)
        self.mostrar_frame(self.button_d4_camp_magnetico)
        self.mostrar_frame(self.button_d5_camp_magnetico)

        if not hasattr(self, 'graficaCampEspira'):
            self.graficaEspira = Espira_Magne()
            self.graf_camp_magnetico3.addWidget(self.graficaEspira)
            self.graficaEspira.graficar_espira()

        self.stackedWidget_camp_magne_derecha.setCurrentWidget(self.Espira_magnetica)

    def mostrar_espiras(self):
        self.limpiar_simu_magne()
        self.ocultar_frame(self.button_d4_camp_magnetico)
        self.mostrar_frame(self.button_d1_camp_magnetico)
        self.mostrar_frame(self.button_d2_camp_magnetico)
        self.mostrar_frame(self.button_d3_camp_magnetico)
        self.mostrar_frame(self.button_d5_camp_magnetico)

        if not hasattr(self, 'graficaCampEspiras'):
            self.graficaEspiras = Espiras_Magnes()
            self.graf_camp_magnetico4.addWidget(self.graficaEspiras)
            self.graficaEspiras.graficar_espiras()

        self.stackedWidget_camp_magne_derecha.setCurrentWidget(self.Espiras_magneticas)

    def mostrar_dipolo_magnetico(self):
        self.limpiar_simu_magne()
        self.ocultar_frame(self.button_d5_camp_magnetico)
        self.mostrar_frame(self.button_d1_camp_magnetico)
        self.mostrar_frame(self.button_d2_camp_magnetico)
        self.mostrar_frame(self.button_d3_camp_magnetico)
        self.mostrar_frame(self.button_d4_camp_magnetico)

        if not hasattr(self, 'graficaDipoloMagne2D'):
            self.graficaDipoloMagne2D = Dipolo_Magne_2d()
            self.graf_camp_magnetico5.addWidget(self.graficaDipoloMagne2D)
            self.graficaDipoloMagne2D.graficar_dipolo_2d()
        
        if not hasattr(self, 'graficaDipoloMagne3D'):
            self.graficaDipoloMagne3D = Dipolo_Magne_3d()
            self.graf_camp_magnetico6.addWidget(self.graficaDipoloMagne3D)
            self.graficaDipoloMagne3D.graficar_dipolo_3d()

        self.stackedWidget_camp_magne_derecha.setCurrentWidget(self.Dipolo_magnetico)

    def limpiar_simu_magne(self):
        if hasattr(self, 'graficaEspira'):
            self.borrar_simu(self.graficaEspira, self.graf_camp_magnetico3)
        if hasattr(self, 'graficaEspiras'):
            self.borrar_simu(self.graficaEspiras, self.graf_camp_magnetico4)
        if hasattr(self, 'graficaDipoloMagne2D'):
            self.borrar_simu(self.graficaDipoloMagne2D, self.graf_camp_magnetico5)
            
    #////////////////////////   Campo Magnético (FIN)   /////////////////////////////////////////////////////////////////////////////////////////////////////////////#

    #////////////////////////   Campo Magnético "Prácticas"   ///////////////////////////////////////////////////////////////////////////////////////////////////////#

    def abrir_prac17(self):
        ventana = Prac17(self)
        ventana.show()

    #////////////////////////   Campo Magnético "Prácticas" (FIN)   /////////////////////////////////////////////////////////////////////////////////////////////////#


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
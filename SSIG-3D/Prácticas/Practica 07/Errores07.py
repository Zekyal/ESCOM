# Práctica 07. Archivo con las funciones de mensajes de Error.

from PyQt5.QtWidgets import QMessageBox ## Para las ventanas de errores

# Función para el caso de no seleccionar el tipo de los Cosenos.
def Error_Tipo(self):    
    msg_box = QMessageBox()     # Crea el objeto de tipo QMessageBox
    msg_box.setWindowTitle("Error de selección de tipo de α, β y ɣ.")     # Inserta título a la ventana
    msg_box.setText("Favor de seleccionar el tipo de valor de los cosenos.")     # Texto de la ventana
    msg_box.setInformativeText("Seleccione el botón de 'Grados' o 'Radianes' para todos los Cosenos.")
    msg_box.setIcon(QMessageBox.Information)        # Agrega un ícono a la ventana (Predeterminados)
    msg_box.exec_()     # Muestra la ventana de error

# Función para el caso de insertar un valor de 0 a la MAgnitud.
def Error_Magnitud(self):    
    msg_box = QMessageBox()     # Crea el objeto de tipo QMessageBox
    msg_box.setWindowTitle("Error en valor de la MAgnitud")     # Inserta título a la ventana
    msg_box.setText("Insertar un valor a 'Magnitud |v|' mayor de 0.")     # Texto de la ventana
    msg_box.setIcon(QMessageBox.Information)        # Agrega un ícono a la ventana (Predeterminados)
    msg_box.exec_()     # Muestra la ventana de error

# Función para el caso de cancelar al seleccionar dirección.
def Error_Direccion(self):    
    msg_box = QMessageBox()     # Crea el objeto de tipo QMessageBox
    msg_box.setWindowTitle("Error al seleccionar destino de su gráfica.")     # Inserta título a la ventana
    msg_box.setText("Favor de seleccionar una carpeta válida.")     # Texto de la ventana
    msg_box.setIcon(QMessageBox.Critical)        # Agrega un ícono a la ventana (Predeterminados)
    msg_box.exec_()     # Muestra la ventana de error

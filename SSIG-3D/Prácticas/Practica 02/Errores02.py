# Práctica 02. Archivo con las funciones de mensajes de Error.

from PyQt5.QtWidgets import QMessageBox ## Para las ventanas de errores

# Función para el caso de no insertar un usuario.
def Error_Usuario(self):    
    msg_box = QMessageBox()     # Crea el objeto de tipo QMessageBox
    msg_box.setWindowTitle("Error de Nombre de Usuario.")     # Inserta título a la ventana
    msg_box.setText("Favor de insertar un nombre de usuario.")     # Texto de la ventana
    msg_box.setIcon(QMessageBox.Information)        # Agrega un ícono a la ventana (Predeterminados)
    msg_box.exec_()     # Muestra la ventana de error

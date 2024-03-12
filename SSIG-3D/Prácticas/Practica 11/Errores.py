# Archivo con las funciones de mensajes de Error.

from PyQt5.QtWidgets import QMessageBox ## Para las ventanas de errores

# Función de error en caso de que la magnitud del vector |v| = 0.
def Error_Carga(self):    
    msg_box = QMessageBox()     # Crea el objeto de tipo QMessageBox
    msg_box.setWindowTitle("Error al insertar valor de carga.")     # Inserta título a la ventana
    msg_box.setText("Inserte valores mayores o menores a 0.")     # Texto de la ventana
    msg_box.setIcon(QMessageBox.Critical)        # Agrega un ícono a la ventana (Predeterminados)
    msg_box.exec_()     # Muestra la ventana de error
# Práctica 05. Archivo con las funciones de mensajes de Error.

from PyQt5.QtWidgets import QMessageBox ## Para las ventanas de errores

# Función para el caso de cancelar al seleccionar dirección.
def Error_Direccion(self):    
    msg_box = QMessageBox()     # Crea el objeto de tipo QMessageBox
    msg_box.setWindowTitle("Error al seleccionar destino de su gráfica.")     # Inserta título a la ventana
    msg_box.setText("Favor de seleccionar una carpeta válida.")     # Texto de la ventana
    msg_box.setIcon(QMessageBox.Critical)        # Agrega un ícono a la ventana (Predeterminados)
    msg_box.exec_()     # Muestra la ventana de error
